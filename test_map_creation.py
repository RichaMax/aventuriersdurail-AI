from utils import create_adjacency_matricies
import json

path_to_game_parameters = r"C:\Users\richa\Documents\perso\projets\adr_ai\game_config.json"
with open(path_to_game_parameters, 'r') as f:
     game_parameters = json.load(f)

mr, dr = create_adjacency_matricies(game_parameters['city_mapping'])
print(mr)
print(dr)
