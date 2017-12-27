
def boolean(x, y, condition):
    if condition == 'conjunction':
        return x & y
    elif condition == 'disjunction':
        return x | y
    elif condition == 'implication':
        return (x and y) or not x
    elif condition == 'exclusive':
        return x ^ y
    elif condition == 'equivalence':
        return 1 if x == y else 0
        
        
if __name__ == '__main__':
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"

