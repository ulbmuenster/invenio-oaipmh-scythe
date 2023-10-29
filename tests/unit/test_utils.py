# SPDX-FileCopyrightText: 2015 Mathias Loesch
#
# SPDX-License-Identifier: BSD-3-Clause

from lxml import etree

from oaipmh_scythe.utils import xml_to_dict

xml = "<root><a>One</a><b>Two</b><c>Three</c><c>Four</c><d/></root>"


def test_xml_to_dict() -> None:
    actual = xml_to_dict(etree.XML(xml))
    expected = {"a": ["One"], "b": ["Two"], "c": ["Three", "Four"], "d": [None]}
    assert actual == expected
