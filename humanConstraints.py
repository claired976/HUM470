#-----------------------------------------------------------------------
# humanConstraints.py generates random constraints for the word count,
# line count, etc. for the human poet.
#-----------------------------------------------------------------------

import random
from random import randint

numWords = 3 # number of words in metaphor chain

print("You get this many words to explain each metaphor: ", randint(0, 50))

for i in range(numWords):
    print("You get this many words between word %i and word %i: " %(i+1, i+2),
          randint(0, 50))