import random
import numpy as np


# Reddit code challenge:
# https://www.reddit.com/r/dailyprogrammer/comments/8jvbzg/20180516_challenge_361_intermediate_elsiefour/

# Primary source:
# https://eprint.iacr.org/2017/339.pdf


# ElsieFour alphabet
alphabet = '#_23456789abcdefghijklmnopqrstuvwxyz'

# Personal key
# key = 'giv_mosn76239qjw4chzrlbexu#t58apkfdy'

# Key for reddit code challenge
key = 's2ferw_nx346ty5odiupq#lmz8ajhgcvk79b'

# Lookup to the numeric integer values of the ElsieFour alphabet
index = dict((i, a) for a, i in enumerate(alphabet))



def elsie_four(key, text):

    # Encryption algorithm, see primary source material for more information
    def encrypt(key, text):
        # Convert the key into a state matrix
        state_grid = np.array([index[i] for i in key]).reshape(6, 6)

        # Convert the ElsieFour index into a state-like matrix
        index_grid = np.array([a for a, i in enumerate(alphabet)]).reshape(6, 6)

        # Initialize the marker
        i, j = 0, 0
        marker = state_grid[i][j]

        # Initialize the encrypted response
        response = ''
        
        # Determine the encrypted value of every letter in the input text
        for letter in text:

            # Find the row and column of the letter currently being encrypted in the state matrix
            r, c = np.ravel(np.where(state_grid == index[letter]))

            # Find the indicies of the ciphertext value of the letter currently being encrypted
            # by adding the marker indicies to the input text indicies (modulo 6)
            x = (r + (marker // 6)) % 6
            y = (c + (marker % 6 )) % 6
            # Find the ciphertext value and concatenate it to the encrypted response
            ciphertext = state_grid[x][y]
            response += alphabet[ciphertext]
        
            # Alter the state matrix by rotating the row that contains the plaintext
            # If the marker's index moves the marker moves too  
            state_grid[r] = np.roll(state_grid[r], 1)
            if x == r:
                y = (y + 1) % 6
            if i == r:
                j = (j + 1) % 6

            # Alter the state matrix by rotating the column that contains the ciphertext
            # If the marker's index moves the marker moves too
            state_grid[:,y] = np.roll(state_grid[:,y], 1)
            if c == y:
                r = (r + 1) % 6
            if j == y:
                i = (i + 1) % 6

            # Update the indices of the marker
            i = (i + (ciphertext // 6)) % 6
            j = (j + (ciphertext % 6)) % 6

            # Update the marker with the new indices
            marker = state_grid[i][j]

        print(response, "\n")

    # Decryption algorithm. See primary source material for more information
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

    encrypt_tf = False
    if '%' in text:
        encrypt_tf = True
    if encrypt_tf:
        encrypt(key, text[1:])
    else:
        decrypt(key, text)

if __name__ == '__main__':
    elsie_four('7dju4s_in6vkecxorlzftgq358mhy29pw#ba', '%the_swallow_flies_at_midnight')