# ----------------------------------------------------------------------------
# sparser.py takes the synset text file and returns a JavaScript file of
# JavaScript objects for the web. Namely, it stores the synsets as a
# 1 array of definitions and 1 symbol table of words to indexes (to find
# definitions).
# ----------------------------------------------------------------------------

import csv

if __name__ == '__main__':

    darray = []

    with open('synsets.js', 'w') as js_file:

        js_file.write("// THIS FILE NOT COMPLETE\n\n")

        js_file.write("// a symbol table of words to index where definition "
            "lies \n")
        js_file.write("dictionary = {")
        with open('synsets_50.txt') as csv_file:
            csvreader = csv.reader(csv_file, delimiter=',')
            for row in csvreader:
                # write to dictionary
                js_file.write(row[0])
                js_file.write(": '")
                js_file.write(row[1])
                js_file.write("', ")
                darray.append(row[2])

        js_file.write("\n\n\n")
        js_file.write("// an array of definitions\n")
        js_file.write("definitions = [")
        for entry in darray:
            js_file.write("'")
            js_file.write(entry)
            js_file.write("', ")
        js_file.write("]")