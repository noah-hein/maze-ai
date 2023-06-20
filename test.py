import os.path
import random
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

from transformers import PreTrainedTokenizerFast, pipeline, GPT2LMHeadModel, set_seed

import config
from mazelib import Maze, Prims

if __name__ == '__main__':
    tokenizer = PreTrainedTokenizerFast(tokenizer_file=config.TOKENIZER_FILE_PATH)

    model = GPT2LMHeadModel.from_pretrained(config.MODEL_PATH, local_files_only=True)

    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
    set_seed(random.randint(0, 100000))

    max_length = (config.MAX_WIDTH * 2 + 1) * (config.MAX_HEIGHT * 2 + 1)
    print(max_length)
    maze_string = generator(
        "3",
        max_length=max_length,
        # num_beams=5,
        # no_repeat_ngram_size=2,
        # num_return_sequences=5,
        # early_stopping=True
    )
    maze_string = maze_string[0]["generated_text"]
    maze_string = maze_string.replace(" ", "")

    print(maze_string)


    maze = Maze()
    maze.string_to_maze(maze_string)
    print(maze.grid)
    maze.display_maze()
