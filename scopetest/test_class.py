from unittest import TestCase

import pytest


class TestOne(TestCase):

    @pytest.fixture(autouse=True)
    def use_fixtures(self, thingy, thingy_byclass):
        self.thingy = thingy
        self.byclass = thingy_byclass

    def test_fu(self):
        print()
        print('TestOne::test_fu  thingy  {:f}'.format(self.thingy))
        print('TestOne::test_fu  byclass {:f}'.format(self.byclass))

    def test_ba(self):
        print()
        print('TestOne::test_ba  thingy  {:f}'.format(self.thingy))
        print('TestOne::test_ba  byclass {:f}'.format(self.byclass))


class TestTwo(TestCase):

    @pytest.fixture(autouse=True)
    def use_fixtures(self, thingy, thingy_byclass):
        self.thingy = thingy
        self.byclass = thingy_byclass

    def test_fu(self):
        print()
        print('TestTwo::test_fu  thingy  {:f}'.format(self.thingy))
        print('TestTwo::test_fu  byclass {:f}'.format(self.byclass))

    def test_bar(self):
        print()
        print('TestTwo::test_ba  thingy  {:f}'.format(self.thingy))
        print('TestTwo::test_ba  byclass {:f}'.format(self.byclass))

