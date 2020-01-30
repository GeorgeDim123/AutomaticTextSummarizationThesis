import spacy
from spacy.lang.el.examples import sentences
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import filedialog
from spacy.lemmatizer import Lemmatizer


filename = filedialog.askopenfile()
fileReadyToRead = open(filename.name, 'r')
file_contents = fileReadyToRead.read()
print("")
print("Αυτό είναι το κείμενο που ανέβασε ο χρήστης :")
print("")

data = file_contents

nlp = spacy.load("el_core_news_sm")


sentence = nlp(data)
# for word in sentence:
# print(word.text + '  ===>', word.lemma_) ##


newsentence = ' '.join([word.lemma_ for word in nlp(data)])
print(newsentence)


sentence2 = nlp(newsentence)
sentenceAfter2lemms = ' '.join([word.lemma_ for word in nlp(data)])
print(sentenceAfter2lemms)
