X = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
Y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

yx = zip(Y, X)
yx.sort()
print(yx)  # ["a", "d", "h", "b", "c", "e", "i", "f", "g"]