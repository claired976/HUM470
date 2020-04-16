# This is just preliminary experimentation w/ WordNet


import csv # the .txt files are csv format
import random
from random import randint

NUM_SYNSETS = 82191 # total number of synsets
synset = [] # store each row of synsets
hypernym = []

# parse the synset file 
with open('synsets.txt') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    for row in csvreader: 
        synset.append(row) 

# parse the hypernym file
with open('hypernyms.txt') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    for row in csvreader: 
        hypernym.append(row) 


# choose a random word out of a synset
def word_from_synset(synset_id):
    words = synset[synset_id][1].split() # split apart all the words in this synset
    j = randint(0, len(words) - 1) # choose a random index of one of the words in this synset
    return(words[j])



# generates a random synset, and a random word in that synset
i = randint(0, NUM_SYNSETS) # select random id of synset  # i is the current random number...
print(word_from_synset(i), "is", end = " ")



# moving "upwards" randomly
k = randint(1, len(hypernym[i]) - 1) # random hypernym index
rand_hypernym_id = int(hypernym[i][k]) # random hypernym
print(word_from_synset(rand_hypernym_id), "is")



matched_indexes = []

# moving "downwards" randomly
# need to find all instances of this ID in the hypernym file


# generates a random synset, and a random word in that synset
i = randint(0, NUM_SYNSETS) # select random id of synset  # i is the current random number...
print(word_from_synset(i), "is", end = " ")

for row in hypernym:
    for word in row:
        if int(word) == i:
            matched_indexes.append(int(row[0])) # gives you all of the indices that contain it

matched_indexes.remove(i) # remove itself from potential children
if (len(matched_indexes) == 0):
    print("this is the last child.")
else:
    print(word_from_synset(random.choice(matched_indexes)), "is")

