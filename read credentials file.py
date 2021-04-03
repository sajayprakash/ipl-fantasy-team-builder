import pickle

with open('credentials.dat', 'rb+') as f:
    try:
        while True:
            list = pickle.load(f)
            for line in list:
                print(list)
    except EOFError:
        pass







