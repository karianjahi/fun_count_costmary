#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `fun_counting` package."""

import pytest

from fun_counting.fun_counting import Counter

"""
test count words
"""
import pytest


class TestCounter:
    """
    testing Counter class
    """

    def test_one_word(self):
        """
        Testing one word only
        :return: None
        """
        text = "word"
        assert Counter(text).count_words() == 1

    def test_multiple(self):
        """
        Testing multiple words
        """
        text = "These are four words"
        assert Counter(text).count_words() == 4

    def test_html(self):
        """
        Testing html text
        """
        text = "<h1> I study data science at spiced </h1>"
        assert Counter(text).count_words() == 6

    def test_html_with_attributes(self):
        """
        Testing html with attributes
        """
        text = '<h1 class="spiced"> I study data science at spiced </h1>'
        assert Counter(text).count_words() == 6


# Test parameterization: Running many tests in one
my_tests = [
    ('word', 1),
    ('These are four words', 4),
    ('<h1> I study data science at spiced </h1>', 6),
    ('<h1 class="spiced"> I study data science at spiced </h1>', 6)
]


@pytest.mark.parametrize('input, output', my_tests)
def test_all(input, output):
    assert Counter(input).count_words() == output
