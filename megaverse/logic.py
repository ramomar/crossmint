from . import entities


def make_coordinates(goal_map, predicate):
    if not predicate:
        return []

    rows = len(goal_map)
    cols = len(goal_map[0])
    result = []

    for x in range(rows):
        for y in range(cols):
            if predicate(goal_map[x][y]):
                result.append((x, y))

    return result


def make_cometh_entity(string):
    direction, _ = string.split('_')

    return {
        'type': entities.COMETH.lower(),
        'details':{
                'direction': direction.lower(),
        }
    }


def make_soloon_entity(string):
    color, _ = string.split('_')

    return {
        'type': entities.SOLOON.lower(),
        'details': {
            'color': color.lower(),
        }
    }


def make_polyanet_entity(string):
    return {
        'type': entities.POLYANET.lower()
    }


def make_entity(entity_source):
    matchers = [
        (entities.SOLOON, lambda s: entities.SOLOON in s),
        (entities.COMETH, lambda s: entities.COMETH in s),
        (entities.POLYANET, lambda s: entities.POLYANET in s),
    ]
    matches = [entity for (entity, matcher) in matchers if matcher(entity_source)]

    if not matches or len(matches) > 1:
        raise ValueError(f'Invalid entity: {entity_source}')

    makers = {
        entities.SOLOON: make_soloon_entity,
        entities.COMETH: make_cometh_entity,
        entities.POLYANET: make_polyanet_entity,
    }
    maker = makers[matches[0]]

    return maker(entity_source)

