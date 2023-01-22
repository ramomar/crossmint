import requests
import json

<<<<<<< Updated upstream
# It's better to have a .env file, but this is ok for the purpose of this code.
=======
from megaverse import entities

>>>>>>> Stashed changes
MAP_URL = 'https://challenge.crossmint.io/map'
API_HOST = 'https://challenge.crossmint.io/api'
CANDIDATE_ID = '8e0265e6-f525-4f4b-9ddd-d8b405fdbfeb'
ENTITY_TO_RESOURCE = {
    entities.POLYANET.lower(): 'polyanets',
    entities.SOLOON.lower(): 'soloons',
    entities.COMETH.lower(): 'comeths'
}


def get_goal_map():
    return requests.get(f'{API_HOST}/map/{CANDIDATE_ID}/goal').json()


def post_entity(entity_type, coordinates, details):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    row, column = coordinates
    data_with_candidate_id = {
        **details,
        'row': row,
        'column': column,
        'candidateId': CANDIDATE_ID,
    }
    response = requests.post(f'{API_HOST}/{ENTITY_TO_RESOURCE[entity_type]}',
                             headers=headers,
                             data=json.dumps(data_with_candidate_id))

    return response.json()
