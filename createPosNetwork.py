import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import tkinter as tk
from tkinter import filedialog


inputStr = input("[y]Open custom file or [n]use sample text for visualization? [y/n]")
inputStr = inputStr.lower()

if(inputStr == 'y' or inputStr == 'yes'):
	root = tk.Tk()
	root.withdraw()
	file_path = filedialog.askopenfilename()
	sample_text = open(file_path, "r").read() 
else:
	sample_text = state_union.raw("2006-GWBush.txt")

print(sample_text)

def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


#process_content()
