import pickle
from neat import *

with open('model/best_of_generation_40', 'rb') as g:
    genome = pickle.load(g)

config = Config('config')

genome.draw(config)
