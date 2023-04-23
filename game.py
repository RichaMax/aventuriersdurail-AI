import gymnasium
from gymnasium.spaces import Dict, MultiDiscrete, Discrete, MultiBinary
import json
import random
import numpy as np

from utils import create_adjacency_matricies


class gameEnv(gymnasium.Env):
    def __init__(self, path_to_game_parameters, nb_of_players=3):
        with open(path_to_game_parameters, 'r') as f:
            game_parameters = json.load(f)
        # Game Variables
        self.train_deck = random.shuffle(
            game_parameters['number_of_train_per_color'] * game_parameters['roads_color'] + 14 * ['joker']
        )
        self.played_train_cards = [] # this one has to be reshuffle and add back to the train deck when empty
        self.destination_deck = random.shuffle(game_parameters['destination_cards'])
        self.played_destination_cards = [] # this one should not be added back to the destination deck
        self.wagons_per_player = game_parameters['number_of_wagons_per_player']
        self.bonus_points = game_parameters['longest_train_points']
        self.train_lenght_value = game_parameters['train_lenght_value']
        self.main_roads_matrix, self.double_roads_matrix = create_adjacency_matricies(game_parameters['city_mapping'])
        # observation space
        observation_space = Dict(
            {
                "player_id": Discrete(nb_of_players, start=1),
                "decks_status": Dict(
                    {
                        "deck_size": Discrete(110), # faut enlever nb_player *4 ?
                        "face_up_wagons": MultiDiscrete([5 for _ in range(len(game_parameters['roads_color']))]),
                        "discard_deck": Discrete(110),
                        "remaning_destinatons_cards": Discrete(30) # faut enlever nb_players*3 ?
                    }
                ),
                "main_roads": self.main_roads_matrix,
                "double_roads": self.double_roads_matrix,
                "current_player_status": Dict(
                    {
                        "wagon_cards": MultiDiscrete([game_parameters['number_of_train_per_color']
                                                      for _ in range(len(game_parameters['roads_color']))
                                                      ] + [14]
                                                     ),
                        "nb_wagons_left": Discrete(self.wagons_per_player),
                        "destinations_todo": MultiDiscrete(np.ones(self.main_roads_matrix.shape[:2]))
                    }
                ),
                "other_players_status": Dict({})
            }
        )

    def draw_train_card(self, number_of_cards):
        pass

    def compute_longest_train(self):
        #TODO: implement longest train computation (soit faire un truc gitan soit representer la carte sous forme de graph
        # et faire calcul du plus long chemin pour chaque couleur ? )
        pass
    
    def reset(self):
        pass

    def compute_reward(self):
        pass

    def step(self, action):
        new_state = None
        reward = None
        terminal = None
        return new_state, reward, terminal
