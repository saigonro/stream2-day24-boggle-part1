from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    grid = { (row,col) : choice(ascii_uppercase) 
                for row in range(height) 
                    for col in range(width) }
    return grid

def neighbours_of_position(coords):
    row = coords[0]
    col = coords[1]
    return [
        (row-1, col-1),
        (row-1, col),
        (row-1, col+1),
        (row, col-1),
        (row, col+1),
        (row+1, col-1),
        (row+1, col),
        (row+1, col+1)
        ]

def real_grid_neighbours(grid):
    real_neighbours = {}
    for square in grid:
        neighbours = neighbours_of_position(square)
        neighbours = [ n for n in neighbours if n in grid]
        real_neighbours[square] = neighbours
    return real_neighbours

def path_to_word(grid, path):
    word = ""
    for square in path:
        word += grid[square]
    return word

def load_wordlist(file):
    with open(file) as f:
        words = f.read().split('\n')
    words = [ w.upper() for w in words]
    return set(words)

def search(grid, wordlist):
    neighbours = real_grid_neighbours(grid)
    words = []

    def do_search(path):
        word = path_to_word(grid, path)
        if word in wordlist:
            words.append(word)
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
    for position in grid:
        do_search([position])
    return set(words)

def main():
    """
    This is the function that will run the whole project
    """
    grid = make_grid(3, 3)
    wordlist = load_wordlist("words.txt")
    words = search(grid, wordlist)
    for word in words:
        print(word)
    print("Found %s words" % len(words))

if __name__ == "__main__":
    # Code in here will only execution when the file is run directly    
    main()