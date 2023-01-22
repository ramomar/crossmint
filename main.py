import time

from megaverse import logic
from megaverse import io
from megaverse import entities


def solve_phase_1():
    goal_map_response = io.get_goal_map()
    goal_map = goal_map_response['goal']
    coordinates = logic.make_coordinates(goal_map, lambda e: e == entities.POLYANET)

    for (row, column) in coordinates:
        request_data = {
            'row': row,
            'column': column,
        }
        response = io.post_entity('POLYANET', request_data)
        print(response.json())

    print(f'View map: {io.MAP_URL}')


def solve_phase_2():
    goal_map_response = io.get_goal_map()
    goal_map = goal_map_response['goal']
    coordinates = logic.make_coordinates(goal_map, lambda e: e not in entities.SPACE)
    entites_to_create = [((row, col), logic.make_entity(goal_map[row][col])) for (row, col) in coordinates]

    for entity_to_create in entites_to_create:
        coordinates, entity = entity_to_create
        entity_type = entity['type']
        details = entity['details'] if 'details' in entity else {}

        print(io.post_entity(entity_type, coordinates, details))

        # Don't flood the API
        time.sleep(1)

    print(f'View map: {io.MAP_URL}')


if __name__ == '__main__':
    solve_phase_2()
