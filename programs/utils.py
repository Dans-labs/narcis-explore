import gzip
import pickle

GZIP_LEVEL = 2
PICKLE_PROTOCOL = 4


def writeData(fileName, data):
    with gzip.open(fileName, 'wb', compresslevel=GZIP_LEVEL) as f:
        pickle.dump(data, f, protocol=PICKLE_PROTOCOL)


def readData(fileName):
    with gzip.open(fileName, 'rb') as f:
        data = pickle.load(f)
    return data


def getTopKeys(keys):
    topKeys = {}
    for (i, key) in enumerate(keys):
        if '.' not in key:
            topKey = key
        else:
            topKey = key[0:key.find('.')]
        topKeys[i] = topKey
    return topKeys
