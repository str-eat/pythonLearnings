import random
import numpy as np

alphabet = '#_23456789abcdefghijklmnopqrstuvwxyz'
# key = 'giv_mosn76239qjw4chzrlbexu#t58apkfdy'
key = 's2ferw_nx346ty5odiupq#lmz8ajhgcvk79b'
index = dict((i, a) for a, i in enumerate(alphabet))
# vectors = {i:[n%6, n//6] for n, i in enumerate(alphabet)}
# print(vectors)

def elsie_four(key, text):

    def encrypt(key, text):
        state_grid = np.array([index[i] for i in key]).reshape(6, 6)
        index_grid = np.array([a for a, i in enumerate(alphabet)]).reshape(6, 6)
        i, j = 0, 0
        marker = state_grid[i][j]
        response = ''
        
        print(marker)
        print("Index:", index)
        print("Index Grid:", index_grid)
        print("Before", state_grid)

        for letter in text:
            r, c = np.ravel(np.where(state_grid == index[letter]))

            x = (r + (marker // 6)) % 6
            y = (c + (marker % 6 )) % 6
            ciphertext = state_grid[x][y]
            response += alphabet[ciphertext]
        
            state_grid[r] = np.roll(state_grid[r], 1)
            if x == r:
                y = (y + 1) % 6
            if i == r:
                j = (j + 1) % 6

            state_grid[:,y] = np.roll(state_grid[:,y], 1)
            if c == y:
                r = (r + 1) % 6
            if j == y:
                i = (i + 1) % 6

            i = (i + (ciphertext // 6)) % 6
            j = (j + (ciphertext % 6)) % 6

            marker = state_grid[i][j]

        print(response, "\n")

    def decrypt(key, text):
        state_grid = np.array([index[i] for i in key]).reshape(6, 6)    
        i, j = 0, 0
        marker = state_grid[i][j]
        
        response_array = []
        for letter in text:
            response_array.append(index[letter])

        unencrypted = ''

        for letter in response_array:
            x, y = np.ravel(np.where(state_grid == letter))
            r = (x - (marker // 6)) % 6
            c = (y - (marker % 6)) % 6
            plaintext = state_grid[r][c]
            unencrypted += alphabet[plaintext]

            state_grid[r] = np.roll(state_grid[r], 1)
            if x == r:
                y = (y + 1) % 6
            if i == r:
                j = (j + 1) % 6

            state_grid[:,y] = np.roll(state_grid[:,y], 1)
            if c == y:
                r = (r + 1) % 6
            if j == y:
                i = (i + 1) % 6

            i = (i + (letter // 6)) % 6
            j = (j + (letter % 6)) % 6

            marker = state_grid[i][j]

        print(unencrypted)

    decrypt(key, text)

if __name__ == '__main__':
    elsie_four('9mlpg_to2yxuzh4387dsajknf56bi#ecwrqv', 'grrhkajlmd3c6xkw65m3dnwl65n9op6k_o59qeq')