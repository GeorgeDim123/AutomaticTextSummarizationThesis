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
leksi=word_tokenize(data)
protasi=sent_tokenize(data)

a = len(protasi)
print("")
print("Το κείμενο εχει τόσες προτάσεις :")
print(a)

print("")
print("Αυτός είανι ο αριθμός λέξεων σε κάθε πρόταση :")
b = len(leksi)
print(a)

mo=b/a
print(mo)



arithmos = len(leksi)

for x in range(0,arithmos):
    map(str.lower,leksi[x])

pinakas=[0]*b
vathmosprotasis=[0]*a

for x in set(leksi):
    print( "{0} = {1} = {2}".format(x,leksi.count(x),leksi.count(x)/mo))
    for i in range(0,a):
        if x in protasi[i]:
            vathmosprotasis[i]+=leksi.count(x)/mo
print("")
print(" Ο βαθμός της κάθε πρότασης αντίστοιχα είναι : ")
print(vathmosprotasis)


# PREPEI NA KANW TIS LEKSEIS LOWERCASE