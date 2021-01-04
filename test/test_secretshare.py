# -*- coding: utf-8 -*-
"""
    Secret Sharing
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

from utilitybelt import base64_chars
from pyseltongue import SecretSharer
from .test_base import ShamirSharingTest

class SecretShareTest(ShamirSharingTest):
    """Test the SecretSharer class"""
    def __init__(self, *args, **kwargs):
        ShamirSharingTest.__init__(self, *args, **kwargs)
        self.sharer_class = SecretSharer

    def test_hex_to_hex_sharing(self):
        """Test hex string"""
        self.split_and_recover_secret(
            3, 5, "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
        self.split_and_recover_secret_alt_parts(
            3, 5, "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )

    def test_2_of_3_sharing(self):
        """Test 2 shares of 3"""
        self.split_and_recover_secret(
            2, 3, "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
        self.split_and_recover_secret_alt_parts(
            2, 3, "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )

    def test_4_of_7_sharing(self):
        """Test 4 shares of 7"""
        self.split_and_recover_secret(
            4, 7, "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
        self.split_and_recover_secret_alt_parts(
            4, 7, "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )

    def test_5_of_9_sharing(self):
        """Test 5 shares of 9"""
        self.split_and_recover_secret(
            5, 9, "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
        self.split_and_recover_secret_alt_parts(
            5, 9, "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )

    def test_2_of_2_sharing(self):
        """Test 2 shares of 2"""
        self.split_and_recover_secret(
            2, 2, "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
        self.split_and_recover_secret_alt_parts(
            2, 2, "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )

    def test_hex_to_base64_sharing(self):
        """Test using a different char set"""
        self.sharer_class.share_charset = base64_chars
        self.split_and_recover_secret(
            3, 5, "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
        self.split_and_recover_secret_alt_parts(
            3, 5, "c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"
        )
