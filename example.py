import recoverable_pdb as pdb

def demo():
    # raise 'e'
    a = [1]
    b = [2]
    a.append(2)
    b.append(3)
    return a, b

pdb.set_trace()
demo()
