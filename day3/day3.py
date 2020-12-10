#%% part 1
import functools
import operator

prod = functools.partial(functools.reduce, operator.mul)
line_count = 0
with open('input.txt') as input_file:
    map = input_file.read().splitlines()

def get_tree_count(map, velocity):
    """
    
    """

    map_height = len(map)
    map_width = len(map[0])
    tree_count = 0
    col, row = velocity
    while row < map_height:
        cell = map[row][col]
        if cell == "#":
            # Tree hit!
            tree_count += 1
        col = (col + velocity[0]) % map_width # account for horizontal wraparound
        row += velocity[1]
    return tree_count

def is_tree(character):
    return character == "#"

velocities = ((1,1),(3,1),(5,1),(7,1),(1,2))

trees = []
for velocity in velocities:
    tree_count = get_tree_count(map,velocity)
    trees.append(tree_count)
    print(f"Tree count for velocity {velocity} is {tree_count}")
print(f"Tree list: {trees}")
print(f"Product of all tree counts is {prod(trees)}")
# %%
