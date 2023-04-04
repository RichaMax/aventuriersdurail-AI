import gym
from gym import spaces
import json
import random


class gameEnv(gym.Env):
    def __init__(self, path_to_game_parameters):
        with open(path_to_game_parameters, 'r') as f:
            game_parameters = json.load(f)
        self.train_deck = random.shuffle(
            game_parameters['number_of_train_per_color'] * game_parameters['roads_color'] + 14 * ['Joker'])
        self.played_train_cards = [] # this one has to be reshuffle and add back to the train deck when empty
        self.destination_deck = random.shuffle(game_parameters['destination_cards'])
        self.played_destination_cards = [] # this one should not be added back to the destination deck
        self.wagons_per_player = game_parameters['number_of_wagons_per_player']
        self.bonus_points = game_parameters['longest_train_points']
        self.train_lenght_value = game_parameters['train_lenght_value']
        self.routes = self.create_routes_matrix(game_parameters['city_mapping'])

    def create_routes_matrix(self, mapping):



    def draw_train_card(self, number_of_cards):


    def compute_longest_train(self):
        #TODO: implement longest train computation (soit faire un truc gitan soit representer la carte sous forme de graph
        # et faire calcul du plus long chemin pour chaque couleur ? )
        pass
