import pytest
from hexgrid import get_pattern_dimensions, DEFAULT_WIDTH, DEFAULT_HEIGHT


@pytest.fixture
def cmd_args():
    args = {
        'no dims': ['hexgrid.py'],
        'tiny dims': ['hexgrid.py', '2', '3'],
        'non numeric': ['hexgrid.py', 'cat', '3'],
        'too few': ['hexgrid.py', '10'],
        'too many': ['hexgrid.py', '30', '30', '40']
    }
    return args


def test_default_dimensions_are_used_when_none_are_given(cmd_args):
    assert get_pattern_dimensions(cmd_args['no dims']) == (DEFAULT_WIDTH, DEFAULT_HEIGHT)


def test_dimensions_smaller_than_minimum_are_rejected(cmd_args):
    with pytest.raises(SystemExit):
        get_pattern_dimensions(cmd_args['tiny dims'])


def test_non_numeric_dimensions_are_rejected(cmd_args):
    with pytest.raises(SystemExit):
        get_pattern_dimensions(cmd_args['non numeric'])


def test_too_few_dimensions_are_rejected(cmd_args):
    with pytest.raises(SystemExit):
        get_pattern_dimensions(cmd_args['too few'])


def test_too_many_dimensions_are_rejected(cmd_args):
    with pytest.raises(SystemExit):
        get_pattern_dimensions(cmd_args['too many'])
