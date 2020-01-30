from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import filedialog

filename = filedialog.askopenfile()
fileReadyToRead = open(filename.name, 'r')
file_contents = fileReadyToRead.read()
print("")
print("Αυτό είναι το κείμενο που ανέβασε ο χρήστης :")
print("")

data = file_contents
print(sent_tokenize(data))
protasi=sent_tokenize(data)


a = len(protasi)
print("")
print("Το κείμενο εχει τόσες προτάσεις :")
print(a)

print("")
print("Αυτός είανι ο αριθμός λέξεων σε κάθε πρόταση :")
for item in protasi:
   print(len(item.split()))