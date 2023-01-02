import sys
from multiprocessing.context import Process
from Domain.Services.TravelService import CheckValues
from Domain.Services.DecolarService import SingleProcess

def _main(params):
    CheckValues(params)
    SingleProcess(params=params).Start()

def main():
    args = sys.argv[1]
    _main(args)

if __name__ == "__main__":
    main()
