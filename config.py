import os
from mazelib.algorithms import *

SPECIAL_TOKENS = [
    "<start>",
    "<end>",
    "[PAD]",
    "[MASK]"
]

ALLOWED_ALGORITHMS = [
    Prims,
    AldousBroder,
    BacktrackingGenerator,
    BinaryTree,
]

NUMBER_OF_MAZES = 1000
TRAINING_PERCENT = 0.9

MIN_HEIGHT = 3
MAX_HEIGHT = 3
MIN_WIDTH = 3
MAX_WIDTH = 3

OUTPUT_DIRECTORY = "out"
DATA_FILENAME = "dataset.txt"
TOKENIZER_FILENAME = "tokenizer.json"

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), OUTPUT_DIRECTORY)
MODEL_DIRECTORY = os.path.join(OUTPUT_PATH, "models")
DATA_DIRECTORY = os.path.join(OUTPUT_PATH, "data")
DATA_FILE_PATH = os.path.join(DATA_DIRECTORY, DATA_FILENAME)
TOKENIZER_FILE_PATH = os.path.join(OUTPUT_DIRECTORY, TOKENIZER_FILENAME)