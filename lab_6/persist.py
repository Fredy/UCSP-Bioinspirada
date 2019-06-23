import picke


def save_weights(weights, file):
    with open(file, 'wb') as save:
        picke.dump(weights, save)


def load_weights(file):
    with open(file, 'rb') as load:
        weights = picke.load(load)
    return weights
