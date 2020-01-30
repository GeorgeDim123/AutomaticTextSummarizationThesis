from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import filedialog

from tkinter import filedialog

filename = filedialog.askopenfile()
fileReadyToRead = open(filename.name, 'r')
file_contents = fileReadyToRead.read()

data = file_contents
pinakas = (word_tokenize(data))

stopwords = ['ΑΛΛΟΣ', 'άλλος', 'εγώ', 'ΕΓΩ', 'ΕΜΕΝΑ', 'ΕΜΕΙΣ', 'ΕΜΑΣ', 'ΜΟΥ', 'ΜΕ', 'ΜΑΣ', 'ΕΣΥ', 'ΕΣΕΝΑ', 'ΕΣΑΣ', 'ΣΟΥ', 'ΣΕ', 'ΣΑΣ', 'ΑΥΤΟΣ', 'ΑΥΤΟΥ', 'ΑΥΤΟΙ', 'ΑΥΤΩΝ', 'ΑΥΤΟΥΣ',
             'ΤΟΣ', 'ΤΟΥ', 'ΤΟΝ', 'ΤΟΙ', 'ΤΟΥΣ', 'ΑΥΤΗ', 'ΑΥΤΗΣ', 'ΑΥΤΗΝ', 'ΑΥΤΕΣ', 'ΤΗ', 'ΤΗΣ', 'ΤΗΝ', 'ΤΕΣ', 'ΤΟΥΣ', 'ΤΙΣ', 'ΑΥΤΟ', 'ΑΥΤΟΥ', 'ΑΥΤΑ', 'ΤΟ', 'ΤΟΥ', 'ΤΑ', 'ΤΟΥΣ', 'ΕΣΕΙΣ', 'ΑΥΤΑ', 'ΣΤΗΝ', 'ΣΤΗ', 'ΣΤΑ',
             'ΣΤΟ', 'ΣΤΟΝ', 'ΣΤΟΥΣ', 'ΣΤΩΝ', 'ΣΤΙΣ', 'Ο', 'Η', 'ΤΟ', 'ΟΙ', 'ΤΩΝ', 'ΤΟΥΣ',
             'Η', 'ΤΗΣ', 'ΤΗ', 'ΤΙΣ', 'ΤΟΥ', 'ΤΑ', 'ΤΟΝ', 'ΤΗΝ', 'ΑΝΑ', 'ΠΑΡΑ', 'ΚΑΤΑ', 'ΔΙΑ', 'ΜΕΤΑ', 'ΑΝΤΙ',
             'ΑΜΦΙ', 'ΠΕΡΙ', 'ΕΠΙ', 'ΑΠΟ', 'ΥΠΟ', 'ΥΠΕΡ', 'ΕΙΣ', 'ΕΝ', 'ΕΚ', 'ΕΞ',
             'ΠΡΟ', 'ΠΡΟΣ', 'ΣΥΝ', 'ΑΧΡΙ', 'ΜΕΧΡΙ', 'ΑΝΕΥ', 'ΧΩΡΙΣ', 'ΠΛΗΝ', 'ΕΝΕΚΑ', 'ΕΝΕΚΕΝ', 'ΜΑ', 'ΝΗ',
             'ΕΝΑΝΤΙΟΝ', 'ΕΝΑΝΤΙ', 'ΕΝΑΝΤΙΑ', 'ΩΣ', 'ΣΑΝ', 'ΓΙΑ', 'ΕΩΣ', 'ΠΡΟΤΟΥ', 'ΝΑ', 'ΑΝ', 'ΘΑ', 'ΕΙΝΑΙ',

             'άλλος', 'εγώ', 'εμένα', 'εμείς', 'εμάς', 'μου', 'με', 'μας', 'εσύ',
             'εσένα', 'εσάς', 'σου', 'σε', 'σας', 'αυτός', 'αυτού', 'αυτοί', 'αυτών', 'αυτούς',
             'τος', 'του', 'τον', 'τοι', 'τους', 'αυτή', 'αυτής', 'αυτήν', 'αυτές', 'τη', 'της', 'την', 'τες', 'τους', 'τις', 'αυτό', 'αυτά', 'το', 'του', 'τα', 'τους', 'εσείς', 'στην', 'στη', 'στα',
             'στο', 'στον', 'στους', 'στων', 'στις', 'ο', 'η', 'το', 'οι', 'των', 'τους',
             'ή', 'της', 'τις', 'τα', 'ανα', 'ανά', 'παρά', 'κατά', 'διά', 'μετά', 'αντί',
             'αμφί', 'περί', 'επί', 'επι', 'απο', 'υπο', 'υπέρ', 'εις', 'εν', 'εκ', 'εξ', 'προ', 'προς', 'συν', 'αρχι', 'μέχρι', 'άνευ', 'χωρίς', 'πλην', 'ένεκα', 'μα', 'νη',
             'εναντίον', 'έναντι', 'ενάντια', 'ως', 'σαν', 'για', 'έως', 'προτού', 'να', 'αν', 'θα', 'είναι']


# Εδω κάνω τις λέξεις lowercase πριν αφαιρέσω τα stopwords.
pinakas = [w.replace('Α', 'α') for w in pinakas]
pinakas = [w.replace('Ά', 'ά') for w in pinakas]
pinakas = [w.replace('Β', 'β') for w in pinakas]
pinakas = [w.replace('Γ', 'γ') for w in pinakas]
pinakas = [w.replace('Δ', 'δ') for w in pinakas]
pinakas = [w.replace('Ε', 'ε') for w in pinakas]
pinakas = [w.replace('Έ', 'ε') for w in pinakas]
pinakas = [w.replace('Ζ', 'ζ') for w in pinakas]
pinakas = [w.replace('Η', 'η') for w in pinakas]
pinakas = [w.replace('Ή', 'ή') for w in pinakas]
pinakas = [w.replace('Θ', 'θ') for w in pinakas]
pinakas = [w.replace('Ι', 'ι') for w in pinakas]
pinakas = [w.replace('Ί', 'ι') for w in pinakas]
pinakas = [w.replace('Κ', 'κ') for w in pinakas]
pinakas = [w.replace('Λ', 'λ') for w in pinakas]
pinakas = [w.replace('Μ', 'μ') for w in pinakas]
pinakas = [w.replace('Ν', 'ν') for w in pinakas]
pinakas = [w.replace('Ξ', 'ξ') for w in pinakas]
pinakas = [w.replace('Ο', 'ο') for w in pinakas]
pinakas = [w.replace('Ό', 'ό') for w in pinakas]
pinakas = [w.replace('Π', 'π') for w in pinakas]
pinakas = [w.replace('Ρ', 'ρ') for w in pinakas]
pinakas = [w.replace('Σ', 'σ') for w in pinakas]
pinakas = [w.replace('Τ', 'τ') for w in pinakas]
pinakas = [w.replace('Υ', 'υ') for w in pinakas]
pinakas = [w.replace('Ύ', 'ύ') for w in pinakas]
pinakas = [w.replace('Φ', 'φ') for w in pinakas]
pinakas = [w.replace('Χ', 'χ') for w in pinakas]
pinakas = [w.replace('Ψ', 'ψ') for w in pinakas]
pinakas = [w.replace('Ω', 'ω') for w in pinakas]
pinakas = [w.replace('Ώ', 'ώ') for w in pinakas]


for word in list(pinakas):  # iterating on a copy since removing will mess things up
    if word in stopwords:
        pinakas.remove(word)
print("")
print("εδώ κάνω τις λέξεις όλες lowercase για να μπορουν να συνυπολογιστούν και αυτες :")
print("")
# print(pinakas)


print(pinakas)
