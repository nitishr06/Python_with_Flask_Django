import sys

def main(opener):
    f = opener(sys.argv[1], mode='wt') #data is 2nd command line argument so 1 is used. 
    f.write(''.join(sys.argv[2:])) #0th element of sys.arg contains the script name
    f.close()
