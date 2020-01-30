import tkinter as tk
from tkinter import *
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import filedialog
from tkinter.messagebox import *


def my_function():
    global telikoScore
    global out
    global protasi

    filename = filedialog.askopenfile()
    fileReadyToRead = open(filename.name, 'r')
    file_contents = fileReadyToRead.read()

    data = file_contents

    data = file_contents

    leksi = word_tokenize(data)
    # ΕΔΩ ΑΛΛΑΖΩ ΤΑ ΣΗΜΕΙΑ ΣΤΙΞΗΣ ΓΙΑ ΝΑ ΚΟΠΟΥΝ ΣΩΣΤΑ ΟΙ ΠΡΟΤΑΣΕΙΣ
    leksi = [w.replace(';', '.') for w in leksi]
    leksi = [w.replace('!', '.') for w in leksi]
    protasi = sent_tokenize(data)

    # Lowercase ta grammata gia na ypologisoyn kai afta me ta kefalea
    leksi = [w.replace('α', 'Α') for w in leksi]
    leksi = [w.replace('ά', 'Α') for w in leksi]
    leksi = [w.replace('β', 'Β') for w in leksi]
    leksi = [w.replace('γ', 'Γ') for w in leksi]
    leksi = [w.replace('δ', 'Δ') for w in leksi]
    leksi = [w.replace('ε', 'Ε') for w in leksi]
    leksi = [w.replace('έ', 'Ε') for w in leksi]
    leksi = [w.replace('ζ', 'Ζ') for w in leksi]
    leksi = [w.replace('η', 'Η') for w in leksi]
    leksi = [w.replace('ή', 'Η') for w in leksi]
    leksi = [w.replace('θ', 'Θ') for w in leksi]
    leksi = [w.replace('ι', 'Ι') for w in leksi]
    leksi = [w.replace('ί', 'Ι') for w in leksi]
    leksi = [w.replace('κ', 'Κ') for w in leksi]
    leksi = [w.replace('λ', 'Λ') for w in leksi]
    leksi = [w.replace('μ', 'Μ') for w in leksi]
    leksi = [w.replace('ν', 'Ν') for w in leksi]
    leksi = [w.replace('ξ', 'Ξ') for w in leksi]
    leksi = [w.replace('ο', 'Ο') for w in leksi]
    leksi = [w.replace('ό', 'Ο') for w in leksi]
    leksi = [w.replace('π', 'Π') for w in leksi]
    leksi = [w.replace('ρ', 'Ρ') for w in leksi]
    leksi = [w.replace('σ', 'Σ') for w in leksi]
    leksi = [w.replace('τ', 'Τ') for w in leksi]
    leksi = [w.replace('υ', 'Υ') for w in leksi]
    leksi = [w.replace('ύ', 'Υ') for w in leksi]
    leksi = [w.replace('φ', 'Φ') for w in leksi]
    leksi = [w.replace('χ', 'Χ') for w in leksi]
    leksi = [w.replace('ψ', 'Ψ') for w in leksi]
    leksi = [w.replace('ω', 'Ω') for w in leksi]
    leksi = [w.replace('ώ', 'Ω') for w in leksi]
    leksi = [w.replace('ς', 'Σ') for w in leksi]

    a = len(protasi)
    b = len(leksi)
    mo = b / a

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

    for word in list(leksi):
        if word in stopwords:
            leksi.remove(word)

    arithmos = len(leksi)

    for x in range(0, arithmos):
        map(str.lower, leksi[x])

    pinakas = [0] * b
    vathmosprotasis = [0] * a

    for x in set(leksi):
        for i in range(0, a):
            if x in protasi[i]:
                vathmosprotasis[i] += leksi.count(x) / mo

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

    # EDW VRISKW TIN PROTASI ME TO MEGALITERO VATHMO KAI TIN EKTYPONW

    for i in range(0, arithmos):
        telikoScore[i] = listaScore[i] + vathmosprotasis[i]

    out = [i for i in sorted(range(len(telikoScore)),
                             key=telikoScore.__getitem__, reverse=True)][:5]
    # ARITHMOS POSES PROTASEIS THELEI O XRISTIS
    print(out)


def show_answer():

    my_function()
    Ans = "Οι  σημαντοκότερες προτάσεις του κειμένου είναι : \n "
    Ans0 = out

    Ans1 = protasi[out[0]]
    Ans2 = protasi[out[1]]
    Ans3 = protasi[out[2]]
    Ans4 = protasi[out[3]]
    Ans5 = protasi[out[4]]

    text1.insert(tk.INSERT, Ans)
    text1.insert(tk.INSERT, '\n'.join([Ans1, Ans2, Ans3, Ans4, Ans5]))


root = tk.Tk()
root.title("Programm")
text1 = tk.Text(root, heigh=25, width=70)


text1.pack()

label1 = Label(text="Αν θέλεις να βρείς τις σημαντοκότερες προτάσεις ενός κειμένου πάτα στο κουμπί 'Περίληψη'")
label1.pack()

button1 = Button(root, text='Περίληψη', command=show_answer)
button1.pack()


blank = Entry(root)


def close_window():
    root.destroy()


def open_window():
    side = tk.Tk()
    side.title(" Κανόνες ")
    LabelRules = Label(side, text=" Το πρόγραμμα αυτο θα σε βοηθήσει να βρείς τις σημαντικότερες προτασεις ενός κειμένου\nΓια να ξεκινήσεις απλά πάτησε το κουμπί περίληψη στο αρχικό μενου\nΣτη συνέχεια επέλεξε το κείμενο απο το οποίο θέλεις τις σημαντικότερες προτάσεις και αποθήκευσε το σε ένα έγγραφο κειμένου (αρχείο .txt)\nΕπέλεξε το αρχείο αυτό και οι σημαντικότερες προτάσεις του κειμένου αυτου θα αναρτηθουν στο πρόγραμμα. ")
    LabelRules.pack()

    def close_sideWindow():
        side.destroy()
    buttonExitSide = Button(side, text="Κλείσιμο ταμπέλας", command=close_sideWindow)
    buttonExitSide.pack()


def clear_window():
    text1.delete('1.0', END)


frame = Frame(root)
frame.pack()

buttonClear = Button(frame, text=" Καθάρισε ", command=clear_window)
buttonClear.pack()

buttonRules = Button(frame, text=" Κανόνες ", command=open_window)
buttonRules.pack()


buttonExit = Button(frame, text=" Έξοδος ", command=close_window)
buttonExit.pack()


root.mainloop()
