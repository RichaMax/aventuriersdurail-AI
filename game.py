import json
import random


class gameEnv:
    def __init__(self, path_to_game_parameters):
        # Je pense que il faut reprendre le JSON parce que faut pouvoir keep track de quel jouer occupe quel chemin, comment ?
        with open(path_to_game_parameters, 'r') as f:
            game_parameters = json.load(f)
        for key, value in game_parameters.items():
            setattr(self, key, value)
        self.train_deck = random.shuffle(self.number_of_train_per_color * self.roads_color + 14 *['Joker'])

    def compute_longest_train(self):
        #TODO: implement longest train computation (soit faire un truc gitan soit representer la carte sous forme de graph
        # et faire calcul du plus long chemin pour chaque couleur ? )
        pass