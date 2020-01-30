from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import filedialog

filename = filedialog.askopenfile()
fileReadyToRead = open(filename.name, 'r')
file_contents = fileReadyToRead.read()




data = file_contents
protasi=sent_tokenize(data)


arithmos = len(protasi)

listaProtasewn = [0] * arithmos
listaScore=[0] * arithmos



for x in range(arithmos):
    listaProtasewn[x]=x+1


# EDW VAZW TIS VATHMOLOGIES ANALOGA ME TIN THESI TIS PROTASIS
listaScore[0] = listaScore[0] + 0.5
listaScore[arithmos-1] = listaScore[arithmos-1] + 0.5

#EDW VAZW TIS VATHMOLOGIES ANALOGA ME TON ARITHMO TON LEKSEWN
for x in range(0,arithmos):
    if len(protasi[x].split()) < 8:
        listaScore[x] = listaScore[x]-0.25
    elif len(protasi[x].split()) > 7 and len(protasi[x].split()) < 13:
        listaScore[x] = listaScore[x] + 0.5
    elif len(protasi[x].split()) > 12:
        listaScore[x] = listaScore[x] - 0.25


print("")
print("Αυτες είναι οι προτάσεις σε αύξων αριθμό :")
print(listaProtasewn)
print("")
print("O βαθμός της κάθε πρότασης αντίστοιχα είναι :")
print(listaScore)

# EDW VRISKW TIN PROTASI ME TO MEGALITERO VATHMO KAI TIN EKTYPONW


out = [i for i in sorted(range(len(listaScore)), key=listaScore.__getitem__, reverse=True)][:3]


for x in out:
    print(protasi[x])