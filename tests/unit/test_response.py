import pytest
from conftest import MockHttpResponse
from lxml import etree

from oaipmh_scythe.response import OAIResponse


@pytest.fixture(scope="module")
def http_response() -> MockHttpResponse:
    return MockHttpResponse("ListRecords.xml")


@pytest.fixture(scope="module")
def oai_response(http_response) -> OAIResponse:
    params = {"verb": "ListRecords"}
    return OAIResponse(http_response, params)


def test_oairesponse_raw(oai_response: OAIResponse) -> None:
    assert isinstance(oai_response.raw, str)
    expected = "<identifier>oai:test.example.com:1585310</identifier>"
    assert expected in oai_response.raw


def test_oairesponse_xml(oai_response: OAIResponse) -> None:
    assert isinstance(oai_response.xml, etree._Element)
    expected = "{http://www.openarchives.org/OAI/2.0/}OAI-PMH"
    assert oai_response.xml.tag == expected


def test_oairesponse_str(oai_response: OAIResponse) -> None:
    expected = "ListRecords"
    assert expected in str(oai_response)
