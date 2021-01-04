# -*- coding: utf-8 -*-
"""
    BitcoinToB32SecretSharer
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

from pyseltongue import BitcoinToB32SecretSharer
from .test_base import ShamirSharingTest

class BitcoinToB32SecretSharerTest(ShamirSharingTest):
    """Test the BitcoinToB32SecretSharer class"""
    def __init__(self, *args, **kwargs):
        ShamirSharingTest.__init__(self, *args, **kwargs)
        self.sharer_class = BitcoinToB32SecretSharer

    def test_b58_to_b32_sharing(self):
        """Test b32 sharing"""
        self.split_and_recover_secret(
            3, 5, "5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS"
        )
        self.split_and_recover_secret_alt_parts(
            3, 5, "5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS"
        )
