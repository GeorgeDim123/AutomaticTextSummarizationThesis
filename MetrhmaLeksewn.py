from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import filedialog

from tkinter import filedialog

filename = filedialog.askopenfile()
fileReadyToRead = open(filename.name, 'r')
file_contents = fileReadyToRead.read()
print("")
print("Αυτό είναι το κείμενο που ανέβασε ο χρήστης :")
print("")

data = file_contents

data = file_contents
protasi=word_tokenize(data)


arithmos = len(protasi)

for x in range(0,arithmos):
    map(str.lower,protasi[x])


for x in set(protasi):
    print( "{0} = {1}".format(x,protasi.count(x)))

# PREPEI NA KANW TIS LEKSEIS LOWERCASE