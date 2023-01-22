import pytest
from megaverse import logic


def test_make_coordinates_no_filter_predicate():
    """it should output empty when there is no predicate"""
    goal_map = [
        ['SPACE', 'POLYANET', 'SPACE'],
        ['SPACE', 'SPACE', 'POLYANET'],
    ]
    actual = logic.make_coordinates(goal_map, None)
    expected = []

    assert actual == expected


def test_make_coordinates_filter_predicate():
    """it should output empty when there is no predicate"""
    goal_map = [
        ['SPACE', 'POLYANET', 'SPACE'],
        ['SPACE', 'SPACE', 'POLYANET'],
    ]
    actual = logic.make_coordinates(goal_map, lambda cell: cell == 'POLYANET')
    expected = [
        (0, 1),
        (1, 2),
    ]

    assert actual == expected


def test_make_entity_polyanet():
    """it should make a polyanet"""
    entity_source = 'POLYANET'
    actual = logic.make_entity(entity_source)
    expected = {
        'type': 'polyanet',
    }

    assert actual == expected


def test_make_entity_soloon():
    """it should make a soloon"""
    entity_source = 'BLUE_SOLOON'
    actual = logic.make_entity(entity_source)
    expected = {
        'type': 'soloon',
        'details': {
            'color': 'blue'
        }
    }

    assert actual == expected


def test_make_entity_cometh():
    """it should make a cometh entity"""
    entity_source = 'RIGHT_COMETH'
    actual = logic.make_entity(entity_source)
    expected = {
        'type': 'cometh',
        'details': {
            'direction': 'right'
        }
    }

    assert actual == expected


def test_make_entity_invalid_source():
    """it should raise an exception"""
    entity_source = 'ALIEN'

    with pytest.raises(ValueError) as excinfo:
        logic.make_entity(entity_source)

    assert 'Invalid entity: ALIEN' in str(excinfo)

