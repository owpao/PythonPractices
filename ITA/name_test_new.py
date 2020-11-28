''' this is the doc string of name_test_new '''

def funct():
    """define the behavior of the method

    Args:
        None

    Returns:
        None
    """
    print("nametest_new:"+__name__)
    print(__doc__)

if __name__ == "__main__":
    setA = {1, 2, 3, 4, 5}
    setB = { 6, 7, 8}

    print(setA.issubset(setB))
    print(setB.issuperset(setA))
    print(setB.isdisjoint(setA))
