def solve(numheads, numlegs):
    
    if numlegs % 2 != 0 or numheads <= 0 or numlegs <= 0:
        print("No solution exists.")
        return None

    
    num_rabbits = (numlegs - 2 * numheads) / 2

    
    num_chickens = numheads - num_rabbits

    
    if num_rabbits < 0 or num_chickens < 0 or num_rabbits != int(num_rabbits) or num_chickens != int(num_chickens):
        print("No solution exists.")
        return None

    return int(num_chickens), int(num_rabbits)


numheads = 42
numlegs = 100

result = solve(numheads, numlegs)

if result:
    chickens, rabbits = result
    print("There are",chickens,"chickens and",rabbits,"rabbits on the farm.")