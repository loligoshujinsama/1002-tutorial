#!usr/bin/env/python
import sys

def elfish(x, chars=['e','f','l']):
    x = x.lower()
    

    if len(chars)<1: #If list is fully removed, it IS elfish
        return "is one elfish word!"
    elif len(x)<1 and len(chars)>1:     #If there still exists the list, and input is exhausted - it IS NOT elfish
        return "is not an elfish word!"

    
    if x[0] in chars: #Check first char if it matches any in list chars
        chars.remove(x[0]) #Remove either E or L or F if matches first char (E/L/F)

    return elfish(x[1:len(x)], chars)
    

if __name__ == "__main__":
    try:
        x = sys.argv[1]
        print(f"{x} {elfish(x)}")

    except Exception as e:
        print(e.args)
