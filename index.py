
POST_X = 0
POST_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]

print("+" + "-" * MAP_WIDTH * 3 +  "+")

for coordinate_y in range(MAP_HEIGHT):
    print("|", end="")
    for coordinate_x in range(MAP_WIDTH):
        if my_position[POST_X] == coordinate_x and my_position[POST_Y] == coordinate_y:
            print(" @ ", end="")
        else:
            print("   ", end="")
    print("|")

print("+" + "-" * MAP_WIDTH * 3 +  "+")



