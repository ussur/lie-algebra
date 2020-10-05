# 4
algebra = [
    [0, 3, 4, 5, 6, 0, 0],
    [-3, 0, 0, 0, 7, 0, 0],
    [-4, 0, 0, -7, 0, 0, 0],
    [-5, 0, 7, 0, 0, 0, 0],
    [-6, -7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

# 13
# algebra = [
#     [0, 3, 4, 5, 0, 7, 0],
#     [-3, 0, 6, 7, 7, 0, 0],
#     [-4, -6, 0, 7, 0, 0, 0],
#     [-5, -7, -7, 0, 0, 0, 0],
#     [0, -7, 0, 0, 0, 0, 0],
#     [-7, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0]
# ]

# 2
# algebra = [
#     [0, 4, 5, 6, 0, 0, 0],
#     [-4, 0, 0, 6, 7, 0, 0],
#     [-5, 0, 0, 7, 6, 0, 0],
#     [-6, -6, -7, 0, 0, 0, 0],
#     [0, -7, -6, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0]
# ]


def lie_bracket(a, b):
    if not a or not b:
        return 0
    sign = 1 if a * b > 0 else -1
    return sign * algebra[abs(a) - 1][abs(b) - 1]


def identity(x, y, z):
    return lie_bracket(lie_bracket(x, y), z) + \
        lie_bracket(lie_bracket(z, x), y) + \
        lie_bracket(lie_bracket(y, z), x)


if __name__ == "__main__":
    dim = 7
    
    # no output means Jacobi identity is satisfied
    for i in range(1, dim + 1):
        for j in range(1, dim + 1):
            for k in range(1, dim + 1):
                ji = identity(i, j, k)
                if ji:
                    print("(e{}, e{}, e{}): {}".format(i, j, k, ji))
                