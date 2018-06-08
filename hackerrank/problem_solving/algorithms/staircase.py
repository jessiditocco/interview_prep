def staircase(n):
    
    spaces = []

    for i in range(n - 1):
        spaces.append(" ")
    spaces.append("#")

    print "".join(spaces)

    x = -2

    for i in range(n - 1):
        spaces[x] = "#"
        print "".join(spaces)

        x = x - 1


staircase(6)
