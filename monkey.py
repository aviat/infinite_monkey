import random
import string
import time
import argparse
from threading import Thread

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
        new = self.generate()
        while new != self.word and not stop:
            new = self.generate()
        if new == word:
            print "%s has found: %s" % (self.name, new)
            stop = True

    def generate(self):
        return ''.join([random.choice(self.letters) for x in self.range_word])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--word', type=str, required=True)
    parser.add_argument('-t', '--threads', type=int, default=1)
    args = parser.parse_args()

    word = args.word
    range_word = range(len(word))
    threads_count = args.threads

    threads = [Monkey(x+1, word, string.lowercase) for x in range(threads_count)]
    begin = time.time()
    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join(1000)

    print "Finished in: %s" % (time.time() - begin,)
