# -*- coding: utf-8 -*-
"""
    plaintext
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

from pyseltongue import PlaintextToHexSecretSharer
from .test_base import ShamirSharingTest

class PlaintextToHexSecretSharerTest(ShamirSharingTest):
    """Test the PlaintextToHexSecretSharer class"""
    def __init__(self, *args, **kwargs):
        ShamirSharingTest.__init__(self, *args, **kwargs)
        self.sharer_class = PlaintextToHexSecretSharer

    def test_printable_ascii_to_hex_sharing(self):
        """Test printable ascii"""
        self.split_and_recover_secret(
            3, 5, "correct horse battery staple"
        )
        self.split_and_recover_secret_alt_parts(
            3, 5, "correct horse battery staple"
        )

    def test_zero_leading_ascii_to_hex_sharing(self):
        """Test leading 0 issue"""
        self.split_and_recover_secret(
            3, 5, '0B4A30EEFEBA6783EA68F79AD5DC85E4DDCD83D4'
        )
        self.split_and_recover_secret_alt_parts(
            3, 5, '0B4A30EEFEBA6783EA68F79AD5DC85E4DDCD83D4'
        )

    def test_f_leading_ascii_to_hex_sharing(self):
        """Test leading 0 issue"""
        self.split_and_recover_secret(
            3, 5, 'f6b00c143f637e83f0eb2366888d1c02878dc32366148648f08fea67c8704cdd'
        )
        self.split_and_recover_secret_alt_parts(
            3, 5, 'f6b00c143f637e83f0eb2366888d1c02878dc32366148648f08fea67c8704cdd'
        )
