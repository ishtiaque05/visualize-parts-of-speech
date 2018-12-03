import nltk
import json
import tkinter as tk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize
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


def create_json(word_freq):
	pos = ["CC","CD","DT","EX","FW", "IN", 
			"JJ", "JJR","JJS","LS", "MD",
			"NN", "NNS", "NNP", "NNPS", "PDT",
			"POS","PRP","PRP$", "RB","RBR",
			"RBS","RP","TO","UH", "VB"
			"VBD", "VBG", "VBN", "VBP", "VBZ",
			"WDT", "WP", "WP$", "WRD"
		]
	data = {}
	nodes = []
	links = []			
	
	for word, freq in word_freq.items():
		nodes.append({"id": word, "group": "words"})
		links.append( {"source": word, "target": nltk.tag.pos_tag([word])[0][1], "value": freq})

	for tag in pos:
		nodes.append({"id": tag, "group": "pos"})

	data['nodes'] = nodes
	data['links'] = links

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)
		
tokenized = word_tokenize(sample_text)
word_frequency_dist = nltk.FreqDist(tokenized)


word_freq = dict((tokenized, freq) for tokenized, freq in word_frequency_dist.items())
create_json(word_freq)
