from conftest import oairesponse_from_file

from oaipmh_scythe.models import Header, Identify, MetadataFormat, Record, ResumptionToken, Set


def test_resumptiontoken_str() -> None:
    token_string = "some-token"
    token = ResumptionToken(token_string)
    assert token_string in str(token)


def test_identify_repr() -> None:
    identify_response = oairesponse_from_file("Identify.xml", params={})
    identify = Identify(identify_response)
    assert "<Identify>" == repr(identify)


def test_header_repr() -> None:
    record_response = oairesponse_from_file("GetRecord.xml", params={})
    header_element = record_response.xml.find(".//{http://www.openarchives.org/OAI/2.0/}header")
    header = Header(header_element)
    expected = "oai:test.example.com:1996652"
    assert repr(header).startswith("<Header")
    assert expected in repr(header)
    assert "[deleted]>" not in repr(header)


def test_header_deleted_repr() -> None:
    record_response = oairesponse_from_file("GetRecordDeleted.xml", params={})
    header_element = record_response.xml.find(".//{http://www.openarchives.org/OAI/2.0/}header")
    header = Header(header_element)
    assert repr(header).endswith("[deleted]>")


def test_record_repr() -> None:
    record_response = oairesponse_from_file("GetRecord.xml", params={})
    record_element = record_response.xml.find(".//{http://www.openarchives.org/OAI/2.0/}GetRecord")
    record = Record(record_element)
    expected = "oai:test.example.com:1996652"
    assert repr(record).startswith("<Record")
    assert expected in repr(record)
    assert "[deleted]>" not in repr(record)


def test_record_deleted_repr() -> None:
    record_response = oairesponse_from_file("GetRecordDeleted.xml", params={})
    record_element = record_response.xml.find(".//{http://www.openarchives.org/OAI/2.0/}GetRecord")
    record = Record(record_element)
    assert repr(record).endswith("[deleted]>")


def test_set_repr() -> None:
    listsets_response = oairesponse_from_file("ListSets.xml", params={})
    set_element = listsets_response.xml.find(".//{http://www.openarchives.org/OAI/2.0/}set")
    expected = "All BI publications (already published)"
    _set = Set(set_element)
    assert repr(_set).startswith("<Set")
    assert expected in repr(_set)


def test_metadataformat_repr() -> None:
    listmetadataformats_response = oairesponse_from_file("ListMetadataFormats.xml", params={})
    mdf_element = listmetadataformats_response.xml.find(".//{http://www.openarchives.org/OAI/2.0/}metadataFormat")
    metadataformat = MetadataFormat(mdf_element)
    expected = "epicur"
    assert repr(metadataformat).startswith("<MetadataFormat")
    assert expected in repr(metadataformat)
