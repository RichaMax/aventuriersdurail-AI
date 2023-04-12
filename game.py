import gymnasium
from gymnasium.spaces import Dict, MultiDiscrete, Discrete
import json
import random
import numpy as np


class gameEnv(gymnasium.Env):
    def __init__(self, path_to_game_parameters, nb_of_players=3):
        with open(path_to_game_parameters, 'r') as f:
            game_parameters = json.load(f)
        # Game Variables
        self.train_deck = random.shuffle(
            game_parameters['number_of_train_per_color'] * game_parameters['roads_color'] + 14 * ['Joker']
        )
        self.played_train_cards = [] # this one has to be reshuffle and add back to the train deck when empty
        self.destination_deck = random.shuffle(game_parameters['destination_cards'])
        self.played_destination_cards = [] # this one should not be added back to the destination deck
        self.wagons_per_player = game_parameters['number_of_wagons_per_player']
        self.bonus_points = game_parameters['longest_train_points']
        self.train_lenght_value = game_parameters['train_lenght_value']
        # observation space
        observation_space = Dict(
            {
                "player_id": Discrete(nb_of_players, start=1),
                "map": self.create_cities_routes_matrix(game_parameters['city_mapping']), # to
                "deck_status": Dict(
                    {
                        "deck_size": Discrete(106, start=2),
                        "deck_size": MultiDiscrete(np.array([MultiBinary(13) for _ in range(5)])),
                    }
                )
            }
        )

    def create_cities_routes_matrix(self, mapping):
        pass

    def draw_train_card(self, number_of_cards):
        pass

    def compute_longest_train(self):
        #TODO: implement longest train computation (soit faire un truc gitan soit representer la carte sous forme de graph
        # et faire calcul du plus long chemin pour chaque couleur ? )
        pass
