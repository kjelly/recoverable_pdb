import recoverable_pdb as pdb

def demo():
    a = 1
    b = 2
    a += 1
    b += 2
    return a, b

pdb.set_trace()
demo()
