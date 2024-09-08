#Figure 10.7
import random

class intDict(object):
    """A dictionary with integer keys"""

    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self, key, dictVal):
        """Assumes key an int. Adds an entry."""
        hashBucket = self.buckets[key % self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == key:
                hashBucket[i] = (key, dictVal)
                return
        hashBucket.append((key, dictVal))

    def getValue(self, key):
        """Assumes key an int.
           Returns value associated with key"""
        hashBucket = self.buckets[key % self.numBuckets]
        for e in hashBucket:
            if e[0] == key:
                return e[1]
        return None

    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}'  # result[:-1] omits the last comma

if __name__ == '__main__':
    D = intDict(17)
    for i in range(20):
        #choose a random int in the range 0 to 10**5 - 1
        key = random.choice(range(10**5))
        D.addEntry(key, i)
    # print('The value of the intDict is:')
    # print(D)
    print('\n', 'The buckets are:')
    for hashBucket in D.buckets:  # violates abstraction barrier
        print('  ', hashBucket)
