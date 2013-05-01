import recoverable_pdb as pdb
import example_lib

def demo():
    # raise 'e'
    a = [1]
    b = [2]
    a.append(2)
    b.append(3)
    example_lib.test()
    return a, b

pdb.set_trace()
demo()
print 'end'