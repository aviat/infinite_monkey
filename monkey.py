import random
import string
import time
import argparse
from threading import Thread
import functools

stop = False

class Monkey(Thread):

    def __init__(self, name, word, letters, *args, **kwargs):
        super(Monkey, self).__init__(*args, **kwargs)
        self.name = 'Monkey-%s' % (name,)
        self.letters = letters
        self.word = word
        self.range_word = range(len(word))

    def run(self):
        global stop
        word = self.word
        range_word = self.range_word
        choice = functools.partial(random.choice, self.letters)
        join = ''.join

        new = None
        while new != word and not stop:
            new = join([choice() for x in range_word])

        if new == word:
            print "%s has found: %s" % (self.name, new)
            stop = True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--word', type=str, required=True)
    parser.add_argument('-t', '--threads', type=int, default=1)
    args = parser.parse_args()

    threads = [Monkey(x+1, args.word, string.lowercase) for x in range(args.threads)]
    begin = time.time()
    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join(1000)

    print "Finished in: %s" % (time.time() - begin,)
