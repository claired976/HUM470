# ----------------------------------------------------------------------------
# hparser.py takes the hypernym text file and returns a JavaScript file of
# JavaScript objects for the web. Namely, it stores the hypernyms as a
# symbol table objects.
# ----------------------------------------------------------------------------

import csv

if __name__ == '__main__':

    with open('hypernym.js', 'w') as js_file:
        js_file.write("let hypernym = { \n")

        with open('hypernyms.txt') as csv_file:
            csvreader = csv.reader(csv_file, delimiter=',')
            for row in csvreader:
                string = row[0] + ": "
                js_file.write(string)
                js_file.write('[')
                for element in row[1:]:
                    js_file.write("'")
                    js_file.write(element)
                    js_file.write("', ")
                js_file.write('],')
                js_file.write('\n')
        js_file.write("}")
