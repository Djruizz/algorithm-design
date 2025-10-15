def esSimetrica(a):
    for f in range(len(a)):
        for c in range(len(a)):
            if a[f][c] != a[c][f]:
                return False
    return True


A = [
    ["d", "s", "e"],
    ["s", "d", "a"],
    ["e", "a", "d"]
]
print(esSimetrica(A))