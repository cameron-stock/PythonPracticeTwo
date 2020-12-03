#function that can take an indefinite number  of numbers as arguments and returns their average

def foo(*args):
    return sum(args) / len(args)