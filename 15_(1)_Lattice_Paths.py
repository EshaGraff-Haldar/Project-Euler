# number of paths is (total moves) Choose (number_of_horizontal_moves)
#just need to pick when to do the horizontal paths, given you have a certain number of moves

import math
lattice_paths = int(math.factorial(20+20) / ( math.factorial(20) * math.factorial(20)))
print(lattice_paths)