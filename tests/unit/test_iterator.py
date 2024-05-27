# SPDX-FileCopyrightText: 2023 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

import pytest

from invenio_oaipmh_scythe import OAIResponse, Scythe
from invenio_oaipmh_scythe.iterator import OAIItemIterator, OAIResponseIterator
from invenio_oaipmh_scythe.models import Header

query = {"verb": "ListIdentifiers", "metadataPrefix": "oai_dc"}


@pytest.mark.default_cassette("list_identifiers.yaml")
@pytest.mark.vcr()
def test_iterator_str(scythe: Scythe) -> None:
    iterator = OAIResponseIterator(scythe, query)
    assert str(iterator) == "<OAIResponseIterator ListIdentifiers>"


@pytest.mark.default_cassette("list_identifiers.yaml")
@pytest.mark.vcr()
def test_oai_response_iterator(scythe: Scythe) -> None:
    iterator = OAIResponseIterator(scythe, query)
    responses = list(iterator)
    assert isinstance(responses[0], OAIResponse)
    # there are 3 canned responses in list_identifiers.yaml
    assert len(responses) == 3


@pytest.mark.default_cassette("list_identifiers.yaml")
@pytest.mark.vcr()
def test_oai_item_iterator(scythe: Scythe) -> None:
    iterator = OAIItemIterator(scythe, query)
    headers = list(iterator)
    assert isinstance(headers[0], Header)
    # there are 9 canned identifiers in list_identifiers.yaml
    assert len(headers) == 9


@pytest.mark.default_cassette("list_identifiers.yaml")
@pytest.mark.vcr()
def test_oai_item_iterator_ignore_deleted(scythe: Scythe) -> None:
    iterator = OAIItemIterator(scythe, query, ignore_deleted=True)
    headers = list(iterator)
    assert isinstance(headers[0], Header)
    # there are 9 canned responses in list_identifiers.yaml
    # one of them is manually set to "status=deleted"
    assert len(headers) == 8
