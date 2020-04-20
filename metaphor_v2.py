#-----------------------------------------------------------------------
# metaphor_v2.py creates lists of linked metaphors, subject to different
# human and computer generated constraints
#-----------------------------------------------------------------------

import csv 
import random
from random import randint

NUM_SYNSETS = 82191 # total number of synsets
synset = [] # store synsets data
hypernym = [] # store hypernym data

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

# return a random word out of a synset, given its id
def word_from_synset(synsetId):
    words = synset[synsetId][1].split() # split apart all the words in this synset
    randIndex = randint(0, len(words) - 1) # choose a random index of one of the words in this synset
    return(words[randIndex]) # return the word at that index

# return the id of a random hypernym of a synset, given its id
def find_parent(synsetID):
    if (len(hypernym[synsetID]) <= 1):
        return -1 # this is the absolute parent
    randHypernymIndex = randint(1, len(hypernym[synsetID]) - 1) # random index of one of the hypernyms
    randHypernymId = int(hypernym[synsetID][randHypernymIndex]) # id of the random hypernym
    return(randHypernymId)

# return the id of a random hyponym of a synset, given its id
def find_child(synsetID):
    matched_ids = [] # store ids of children of this synset
    for row in hypernym: # go through all relationships
        for word in row:
            if int(word) == synsetID: # if this synset is a child, add the parent to matched_ids
                matched_ids.append(int(row[0]))
    matched_ids.remove(synsetID) # ignore original synset from children list
    if (len(matched_ids) == 0):
        return(-1) # this is a leaf node
    else:
        return(random.choice(matched_ids)) # a random child

# first word; PARAMETER
#firstID = 59450 # human selects first synset
firstID = randint(0, NUM_SYNSETS) # computer selects synset 
print(word_from_synset(firstID), "is", end = " ") # print first word

# number of words in metaphor; PARAMETER
numWords = 5 # human selects number of hops
# numWords = randint(1, 10) # computer selects number of hops, subject to human constraint


# probability of choosing to move upwards at each step; PARAMETER
probUpwards = 0.5 # human selected
# probUpwards = random.uniform(0, 1) # computer selected

prevID = firstID # synset ID of the previously generated word

# loop numWords times, selecting a new word each time
for i in range(numWords):

    # determine number of steps between current word and next word; PARAMETER
    numSteps = 5 # human selects number of steps
    # numSteps = randint(0, 10) # computer selects number of steps, subject to human constraint

    # probUpwards = random.uniform(0, 1) # computer re-selects prob. each word selection

    # repeat numSteps times
    for j in range(numSteps):

        # PARAMETER
        # probUpwards = random.uniform(0, 1) # computer re-selects prob. each step

        k = random.uniform(0, 1)
        if k <= probUpwards: # move upwards/find a parent
            newID = find_parent(prevID) 
            if (newID < 0): # check if parent exists
                # print("This is a parentless synset")
                newID = find_child(prevID)

        else: # move downwards/find a child
            newID = find_child(prevID)
            if (newID < 0): # check if child exists
                # print("This is a childless synset")
                newID = find_parent(prevID) 
        
        prevID = newID # update prevID

    # print the next word
    if (i < (numSteps - 1)):
        print(word_from_synset(prevID), "is", end = " ") # word in middle
    else:
        print(word_from_synset(prevID)) # last word