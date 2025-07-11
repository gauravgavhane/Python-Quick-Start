# Parallel programming

import os
import multiprocessing

def Square(No):
    return (No*No)

def main():
    Data = [1,2,3,4,5]
    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(Square, Data)

    print("Result after square operation is ",Result)

if __name__ == "__main__":
    main()