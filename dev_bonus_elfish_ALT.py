#!usr/bin/env/python
import sys
def elfish(x , elf = ['e','f','l']):
    x=x.lower()
    try:
        if x[0] in elf:
            elf.remove(x[0])
        return elfish(x[1:len(x)])
    except:
        if len(elf) > 0:
            return "it is not elfish"
        else:
            return "it is elfish"

a = sys.argv[1]
print(elfish(a))
