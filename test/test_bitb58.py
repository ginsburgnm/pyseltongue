# -*- coding: utf-8 -*-
"""
    BitcoinToB58SecretSharer
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

from pyseltongue import BitcoinToB58SecretSharer
from .test_base import ShamirSharingTest

class BitcoinToB58SecretSharerTest(ShamirSharingTest):
    """Test the BitcoinToB58SecretSharer class"""
    def __init__(self, *args, **kwargs):
        ShamirSharingTest.__init__(self, *args, **kwargs)
        self.sharer_class = BitcoinToB58SecretSharer

    def test_b58_to_b58_sharing(self):
        """Test b58 sharing"""
        self.split_and_recover_secret(
            3, 5, "5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS"
        )
        self.split_and_recover_secret_alt_parts(
            3, 5, "5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS"
        )
