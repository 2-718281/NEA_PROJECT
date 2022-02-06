import numpy as np
import os, sys


arr = [[1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1]]

arr = np.array(arr)

arr = np.zeros((20, 60), dtype=np.int32)
arr[0, :] = 1
arr[-1, :] = 1
arr[:, 0] = 1
arr[:, -1] = 1
h = arr.shape[0]
w = arr.shape[1]

player_position = [7, 15]
for t in range(100000000):
    if t % 100000 == 0:
        player_position[1] = (player_position[1] + 1) % w

        arr_render = arr.copy()
        arr_render[player_position[0] - 1:player_position[0] + 2, player_position[1] - 1:player_position[1] + 2] = 2
        # str_out = "\r"#  sys.stdout.write('\n')
        # sys.stdout.write(str_out)
        # sys.stdout.flush()
        # sys.stdout.write('\n')
        os.system('cls')  # os.system('cls')
        str_out = "\n"
        for i in range(h):
            str_out += ''.join([(str(arr_render[i, j]) if arr_render[i, j] > 0 else " ") for j in range(w)])
            str_out += '\n'
        sys.stdout.write(str_out)



