import requests
import json

MAP_URL = 'https://challenge.crossmint.io/map'
API_HOST = 'https://challenge.crossmint.io/api'
CANDIDATE_ID = '8e0265e6-f525-4f4b-9ddd-d8b405fdbfeb'


def make_coordinates(goal_map, predicate):
    rows = len(goal_map)
    cols = len(goal_map[0])
    result = []

    for x in range(rows):
        for y in range(cols):
            if predicate(goal_map[x][y]):
                result.append((x, y))

    return result


def phase_1():
    response = requests.get(f'{API_HOST}/map/{CANDIDATE_ID}/goal').json()
    goal_map = response['goal']
    coordinates = make_coordinates(goal_map, lambda p: p == 'POLYANET')

    for (row, column) in coordinates:
        request_data = {
            'row': row,
            'column': column,
            'candidateId': CANDIDATE_ID
        }
        response = requests.post(f'{API_HOST}/polyanets',
                                 headers={'Content-Type': 'application/json; charset=utf-8'},
                                 data=json.dumps(request_data))
        print(response.json())

    print(f'View map: {MAP_URL}')


if __name__ == '__main__':
    pass