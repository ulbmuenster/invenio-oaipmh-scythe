from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from oaipmh_scythe.iterator import OAIItemIterator, OAIResponseIterator
from oaipmh_scythe.models import Record
from oaipmh_scythe.response import OAIResponse

if TYPE_CHECKING:
    from oaipmh_scythe import Scythe


@pytest.fixture
def oairesponse_iterator(harvester: Scythe) -> OAIResponseIterator:
    params = {"verb": "ListRecords"}
    return OAIResponseIterator(harvester, params)


@pytest.fixture
def oaiitem_iterator(harvester: Scythe) -> OAIItemIterator:
    params = {"verb": "ListRecords"}
    return OAIItemIterator(harvester, params)


def test_oairesponse_iterator_str(oairesponse_iterator: OAIResponseIterator) -> None:
    expected = "ListRecords"
    assert expected in str(oairesponse_iterator)


def test_oairesponse_iterator_next(oairesponse_iterator: OAIResponseIterator) -> None:
    response = oairesponse_iterator.next()
    assert isinstance(response, OAIResponse)


def test_oaiitem_iterator(oaiitem_iterator: OAIItemIterator) -> None:
    response = oaiitem_iterator.next()
    assert isinstance(response, Record)
