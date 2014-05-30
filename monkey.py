import sys
import random
import string
import threading
import time

lower_letters = string.letters[:26]

word = sys.argv[1].lower()
lword = len(word)
range_word = range(len(word))
threads = int(sys.argv[2])
stop = False

def generate(range_word):
    return ''.join([random.choice(lower_letters) for x in range_word])

def find(word, range_word):
    global stop
    new = generate(range_word)
    while new != word and not stop:
        new = generate(range_word)
    if new == word:
        print "Found: %s" % new
        stop = True

threads = [threading.Thread(target=find, args=(word,range_word)) for x in range(threads)]
begin = time.time()
for t in threads:
    t.setDaemon(True)
    t.start()

for t in threads:
    t.join(1000)

print "Finished in: %s" % (time.time() - begin,)
