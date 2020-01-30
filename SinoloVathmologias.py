from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import filedialog

from tkinter import filedialog

filename = filedialog.askopenfile()
fileReadyToRead = open(filename.name, 'r')
file_contents = fileReadyToRead.read()


data = file_contents

data = file_contents
leksi = word_tokenize(data)
protasi = sent_tokenize(data)

a = len(protasi)
b = len(leksi)
mo = b / a


arithmos = len(leksi)

for x in range(0, arithmos):
    map(str.lower, leksi[x])

pinakas = [0] * b
vathmosprotasis = [0] * a

for x in set(leksi):
    for i in range(0, a):
        if x in protasi[i]:
            vathmosprotasis[i] += leksi.count(x) / mo
print("")
print(" Ο βαθμός της κάθε πρότασης αντίστοιχα είναι : ")
print(vathmosprotasis)


# PREPEI NA KANW TIS LEKSEIS LOWERCASE


arithmos = len(protasi)

listaProtasewn = [0] * arithmos
listaScore = [0] * arithmos
telikoScore = [0] * arithmos


for x in range(arithmos):
    listaProtasewn[x] = x + 1


# EDW VAZW TIS VATHMOLOGIES ANALOGA ME TIN THESI TIS PROTASIS
listaScore[0] = listaScore[0] + 0.5
listaScore[arithmos - 1] = listaScore[arithmos - 1] + 0.5

# EDW VAZW TIS VATHMOLOGIES ANALOGA ME TON ARITHMO TON LEKSEWN
for x in range(0, arithmos):
    if len(protasi[x].split()) < 8:
        listaScore[x] = listaScore[x] - 0.25
    elif len(protasi[x].split()) > 7 and len(protasi[x].split()) < 13:
        listaScore[x] = listaScore[x] + 0.5
    elif len(protasi[x].split()) > 12:
        listaScore[x] = listaScore[x] - 0.25


print("")
print("O βαθμός της κάθε πρότασης αντίστοιχα είναι :")
print(listaScore)

# EDW VRISKW TIN PROTASI ME TO MEGALITERO VATHMO KAI TIN EKTYPONW


for i in range(0, arithmos):
    telikoScore[i] = listaScore[i] + vathmosprotasis[i]

print("")
print("TO TELIKO SCORE :")
print(telikoScore)

# EDW RWTAW TON XRISTI POSES PROTASEIS THELEI NA EKTYPOSW
#arithmosProtasewnGiaEktypwsh = input("Πόσες προτάσεις θέλεις να εκτυπωθουν για την Περίληψη ;")

out = [i for i in sorted(range(len(telikoScore)), key=telikoScore.__getitem__, reverse=True)][:5]


for x in out:
    print(x)
