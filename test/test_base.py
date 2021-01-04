# -*- coding: utf-8 -*-
"""
    Secret Sharing
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

from random import shuffle
from unittest import TestCase

class ShamirSharingTest(TestCase):
    """Base sharer test class"""
    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        self.sharer_class = None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def split_and_recover_secret(self, minimum, number, secret):
        """Base function to test each sharer class"""
        shares = self.sharer_class.split_secret(secret, minimum, number)
        shuffle(shares)
        recovered_secret = self.sharer_class.recover_secret(shares[0:minimum])
        assert recovered_secret == secret

    def split_and_recover_secret_alt_parts(self, minimum, number, secret):
        """Base function to test each sharer class with different parts"""
        shares = self.sharer_class.split_secret(secret, minimum, number)
        length_of_shares = len(shares)
        if length_of_shares > 2:
            recovered_secret = self.sharer_class.recover_secret(
                shares[length_of_shares-minimum:]
            )
        else:
            recovered_secret = self.sharer_class.recover_secret(shares[0:minimum])
        assert recovered_secret == secret
