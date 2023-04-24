import gymnasium
from gymnasium.spaces import Dict, MultiDiscrete, Discrete, MultiBinary
import json
import random
import numpy as np

from utils import create_adjacency_matricies, COLOR_ID_DIC


class gameEnv(gymnasium.Env):
    def __init__(self, path_to_game_parameters, nb_of_players=3):
        with open(path_to_game_parameters, 'r') as f:
            game_parameters = json.load(f)
        # Game Variables
        wagons_cards = game_parameters['number_of_train_per_color'] * game_parameters['roads_color'] + 14 * ['joker']
        random.shuffle(wagons_cards)
        destinations_cards = game_parameters['destination_deck']
        random.shuffle(destinations_cards)
        self.train_deck = [COLOR_ID_DIC[w] for w in wagons_cards]
        self.played_train_cards = []  # this one has to be reshuffle and add back to the train deck when empty
        self.destination_deck = destinations_cards
        self.seen_destination_cards = []  # this one should not be added back to the destination deck
        self.wagons_per_player = game_parameters['number_of_wagons_per_player']
        self.bonus_points = game_parameters['longest_train_points']
        self.train_length_value = game_parameters['train_length_values']
        self.main_roads_matrix, self.double_roads_matrix = create_adjacency_matricies(game_parameters['city_mapping'])
        # observation space
        self.observation_space = Dict(
            {
                "player_id": Discrete(nb_of_players, start=1),
                "decks_status": Dict(
                    {
                        "deck_size": Discrete(110),  # faut enlever nb_player *4 ?
                        "face_up_wagons": MultiDiscrete([6 for _ in range(len(game_parameters['roads_color']))] + [3]),  # toutes les couleurs + joker
                        "discard_deck": Discrete(110),
                        "remaining_destinations_cards": Discrete(30)  # faut enlever nb_players*3 ?
                    }
                ),
                "main_roads": MultiDiscrete(7 * np.ones(self.main_roads_matrix.shape)),  # les chemins les plus long font 6, et faudrait que la premiere dim soit de taille nb joueur max +1
                "double_roads": MultiDiscrete(7 * np.ones(self.double_roads_matrix.shape)),
                "current_player_status": Dict(
                    {
                        "wagon_cards": MultiDiscrete([game_parameters['number_of_train_per_color'] + 1
                                                      for _ in range(len(game_parameters['roads_color']))
                                                      ] + [15]
                                                     ),
                        "nb_wagons_left": Discrete(self.wagons_per_player+1),
                        "destinations_todo": MultiBinary(self.main_roads_matrix.shape[:2]),
                        "nb_of_points": Discrete(400)  # random number
                    }
                ),
                "pickable_dest_cards": MultiBinary((3, self.main_roads_matrix.shape[0], self.main_roads_matrix.shape[1]))
            }
        )

    def draw_train_card(self, number_of_cards):
        pass

    def compute_longest_train(self):
        # TODO: implement longest train computation (soit faire un truc gitan soit representer la carte sous forme de graph
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
