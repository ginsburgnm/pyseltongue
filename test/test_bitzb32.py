# -*- coding: utf-8 -*-
"""
    BitcoinToZB32SecretSharer
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

from pyseltongue import BitcoinToZB32SecretSharer
from .test_base import ShamirSharingTest

class BitcoinToZB32SecretSharerTest(ShamirSharingTest):
    """Test the BitcoinToZB32SecretSharer class"""
    def __init__(self, *args, **kwargs):
        ShamirSharingTest.__init__(self, *args, **kwargs)
        self.sharer_class = BitcoinToZB32SecretSharer

    def test_b58_to_zb32_sharing(self):
        """Test zb32 sharing"""
        self.split_and_recover_secret(
            3, 5, "5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS"
        )
        self.split_and_recover_secret_alt_parts(
            3, 5, "5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS"
        )
