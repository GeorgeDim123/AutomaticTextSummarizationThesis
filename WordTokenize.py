from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import filedialog

filename = filedialog.askopenfile()
fileReadyToRead = open(filename.name, 'r')
file_contents = fileReadyToRead.read()
print("")
print("Αυτό είναι το κείμενο που ανέβασε ο χρήστης :")
print("")

data = file_contents
print(word_tokenize(data))
