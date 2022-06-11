"""Tests the correct behavior of the bagels game"""

import pytest
from bagels import show_hints
from collections import namedtuple


@pytest.fixture
def n_digits():
    Ndigit = namedtuple("Ndigit", 'one two three')
    return Ndigit('008', '016', '256')


def test_guess_with_no_correct_number_gives_bagels(n_digits):
    assert show_hints(n_digits.three, '108') == 'Bagels'


def test_a_guess_in_the_correct_spot_gives_fermi(n_digits):
    assert show_hints(n_digits.one, '043') == 'Fermi'
    assert show_hints(n_digits.one, '003') == 'Fermi Fermi'


def test_a_correct_guess_in_the_wrong_spot_gives_pico(n_digits):
    assert show_hints(n_digits.three, '520') == 'Pico Pico'


def test_an_empty_guess_gives_bagels(n_digits):
    assert show_hints(n_digits.one, '') == 'Bagels'
