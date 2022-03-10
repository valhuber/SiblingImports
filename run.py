from SiblingB.B import methodB

def main():
    # call method
    s = methodB()
    print(f'run calls methodB, gets {s}')

if __name__ == "__main__":
    print(f'\n run.py, starting')
    main()