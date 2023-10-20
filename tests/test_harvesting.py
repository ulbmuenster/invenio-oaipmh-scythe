# SPDX-FileCopyrightText: 2015 Mathias Loesch
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from lxml import etree

from oaipmh_scythe import Scythe, exceptions
from oaipmh_scythe.iterator import OAIResponseIterator

if TYPE_CHECKING:
    from unittest.mock import MagicMock


from conftest import MockHttpResponseWrongEncoding


def test_oairesponse(harvester: Scythe) -> None:
    response = harvester.harvest(verb="ListRecords", metadataPrefix="oai_dc")
    assert isinstance(response.xml, etree._Element)
    assert isinstance(response.raw, str)


def test_broken_xml(harvester: Scythe) -> None:
    response = harvester.harvest(verb="ListRecords", resumptionToken="ListRecordsBroken.xml")
    assert response.xml is None
    assert isinstance(response.raw, str)


def test_list_records(harvester: Scythe) -> None:
    records = harvester.list_records(metadataPrefix="oai_dc")
    assert len(list(records)) == 8


def test_list_records_ignore_deleted(harvester: Scythe) -> None:
    records = harvester.list_records(metadataPrefix="oai_dc", ignore_deleted=True)
    num_records = len(list(records))
    assert num_records == 4


def test_list_sets(harvester: Scythe) -> None:
    set_iterator = harvester.list_sets()
    sets = list(set_iterator)
    expected = 131
    assert len(sets) == expected
    assert dict(sets[0])


def test_list_metadata_formats(harvester: Scythe) -> None:
    mdf_iterator = harvester.list_metadataformats()
    mdfs = list(mdf_iterator)
    expected = 5
    assert len(mdfs) == expected
    assert dict(mdfs[0])


def test_list_identifiers(harvester: Scythe) -> None:
    records = harvester.list_identifiers(metadataPrefix="oai_dc")
    expected = 4
    num_identifiers = len(list(records))
    assert num_identifiers == expected


def test_list_identifiers_ignore_deleted(harvester: Scythe) -> None:
    records = harvester.list_identifiers(metadataPrefix="oai_dc", ignore_deleted=True)
    # There are 2 deleted headers in the test data
    expected = 2
    num_records = len(list(records))
    assert num_records == expected


def test_identify(harvester: Scythe) -> None:
    identify = harvester.identify()
    assert identify.repositoryName == "A Test Repository"
    assert identify.baseURL == "http://test.example.com/oai"
    assert identify.adminEmail == "john.doe@example.com"
    assert identify.earliestDatestamp == "1970-01-01T00:00:00Z"
    assert identify.deletedRecord == "persistent"
    assert identify.granularity == "YYYY-MM-DD"
    assert identify.sampleIdentifier == "oai:test.example.com:2342"
    assert hasattr(identify, "description")
    assert hasattr(identify, "oai_identifier")
    assert hasattr(identify, "description")
    assert dict(identify)


def test_get_record(harvester: Scythe) -> None:
    oai_id = "oai:test.example.com:1996652"
    record = harvester.get_record(identifier=oai_id)
    assert record.header.identifier == oai_id
    assert oai_id in record.raw
    expected = "2011-09-05T12:51:52Z"
    assert record.header.datestamp == expected
    assert isinstance(record.xml, etree._Element)
    assert dict(record) == record.metadata
    expected = "John Doe"
    assert expected in record.metadata["creator"]
    assert str(record)
    assert bytes(record)
    assert dict(record.header)


def test_badargument(harvester: Scythe) -> None:
    with pytest.raises(exceptions.BadArgument):
        harvester.list_records(metadataPrefix="oai_dc", error="badArgument")


def test_cannotdisseminateformat(harvester: Scythe) -> None:
    with pytest.raises(exceptions.CannotDisseminateFormat):
        harvester.list_records(metadataPrefix="oai_dc", error="cannotDisseminateFormat")


def test_iddoesnotexist(harvester: Scythe) -> None:
    with pytest.raises(exceptions.IdDoesNotExist):
        harvester.list_records(metadataPrefix="oai_dc", error="idDoesNotExist")


def test_nosethierarchy(harvester: Scythe) -> None:
    with pytest.raises(exceptions.NoSetHierarchy):
        harvester.list_records(metadataPrefix="oai_dc", error="noSetHierarchy")


def test_badresumptiontoken(harvester: Scythe) -> None:
    with pytest.raises(exceptions.BadResumptionToken):
        harvester.list_records(metadataPrefix="oai_dc", error="badResumptionToken")


def test_norecordsmatch(harvester: Scythe) -> None:
    with pytest.raises(exceptions.NoRecordsMatch):
        harvester.list_records(metadataPrefix="oai_dc", error="noRecordsMatch")


def test_undefined_oai_error_xml(harvester: Scythe) -> None:
    with pytest.raises(exceptions.OAIError):
        harvester.list_records(metadataPrefix="oai_dc", error="undefinedError")


def test_oairesponseiterator(harvester: Scythe) -> None:
    harvester.iterator = OAIResponseIterator
    records = list(harvester.list_records(metadataPrefix="oai_dc"))
    expected = 4
    assert len(records) == expected


def test_wrong_encoding(mock_get: MagicMock) -> None:
    harvester = Scythe("https://localhost")
    mock_response = MockHttpResponseWrongEncoding("GetRecord_utf8test.xml")
    mock_get.return_value = mock_response
    oai_id = "oai:test.example.com:1996652"
    record = harvester.get_record(identifier=oai_id)
    assert record.header.identifier == oai_id
    assert oai_id in record.raw
    expected = "2011-09-05T12:51:52Z"
    assert record.header.datestamp == expected
    assert isinstance(record.xml, etree._Element)
    assert dict(record) == record.metadata
    expected = "某人"
    assert expected in record.metadata["creator"]
    assert str(record)
    assert bytes(record)
    assert dict(record.header)
