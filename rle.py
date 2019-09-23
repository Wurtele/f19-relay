#!/usr/bin/env python3

import sys

#read textfile
#take repeating characters and turn them into num then letter ex aaa -> 3a
def main(args):

    if (argv[1]=='x'):
        with open(argv[2],'r') as f:
            for line in f:
                c=0                          #count number of characters until new character then save num + char
                current=''
                previous=''
                for char in line:
                    current=char
                    if current==previous:
                        c+=1
                    else:
                        print(c,previous)
                    previous=char
    elif (argv[1]=='c'):
        pass

    return 0

if __name__ == "__main__":
    main(sys.argv)
