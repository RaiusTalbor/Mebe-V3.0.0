from tkinter import filedialog
import pickle
import os

try:
    pfad = filedialog.askopenfilename(title="Pickle-Datei auswählen", initialdir=os.path.dirname(os.path.abspath(__file__)), filetypes=[("Mebe-Dateien", "*.dat"), ("Alle Dateien", "*.*")])
except:
    pfad = filedialog.askopenfilename(title="Pickle-Datei auswählen", initialdir=os.path.dirname(os.getcwd(), filetypes=[("Mebe-Dateien", "*.dat"), ("Alle Dateien", "*.*")]))

#f = open("temporäre Dateien/000 - Zwischendaten.dat", mode='rb')
f = open(pfad, mode='rb')

platzhalter=pickle.load(f)

print(platzhalter)