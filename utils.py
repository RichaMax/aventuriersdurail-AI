from gymnasium.spaces import Graph
import numpy as np


# TODO: move them
COLOR_ID_DIC = {"red": 0,
                "orange": 1,
                "green": 2,
                "black": 3,
                "yellow": 4,
                "blue": 5,
                "white": 6,
                "pink": 7,
                "joker": 8
                }


def create_adjacency_matricies(mapping, nb_of_colors=8):
    all_cities = mapping.keys()
    encoded_cities = {k: i for i, k in enumerate(all_cities)}
    main_roads_matrix = np.zeros((len(all_cities), len(all_cities), nb_of_colors+1))
    double_roads_matrix = np.zeros((len(all_cities), len(all_cities), nb_of_colors+1))

    for current_city, linked in mapping.items():
        city_enc = encoded_cities[current_city]
        for linked_city, roads in linked.items():
            linked_city_enc = encoded_cities[linked_city]
            for i, road in enumerate(roads):
                road_length = road[0]
                color = road[1]
                if color == "neutral":
                    road_vector = np.array([0] + [road_length for _ in range(nb_of_colors)])
                else:
                    road_vector = [0 for _ in range(nb_of_colors)]
                    road_vector[COLOR_ID_DIC[color]] = road_length
                    road_vector = np.array([0] + road_vector)
                if i == 0:
                    main_roads_matrix[city_enc][linked_city_enc] = road_vector
                else:
                    double_roads_matrix[city_enc][linked_city_enc] = road_vector
    return main_roads_matrix, double_roads_matrix
