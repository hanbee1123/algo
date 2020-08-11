#find all permutations
# Permutation is the number of all possible outocomes of a sequence of numbers when order does matter
# eg. 123 can have permutations of [123,132,213,231,312,321] = 3!
# time complexity = O(n!)

def permutation(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        for cc in permutation(s[:i] + s[i+1:]):
            res.append(c+cc)
    return res

def combination(s):
    if len(s)<2:
        return s
    res = []
    for i, c in enumerate(s):
        res.append(c)
        for cc in combination(s[:i]+s[i+1:]):
            res.append(c+cc)
    return res

if __name__ == "__main__":
    # print(permutation('abcd'))
    print(combination('abcd'))