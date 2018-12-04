import nltk
import json
import tkinter as tk
from nltk.tokenize import word_tokenize
from tkinter import filedialog

inputStr = input("[y]Open custom file or [n]use sample text for visualization? [y/n]")
inputStr = inputStr.lower()

if(inputStr == 'y' or inputStr == 'yes'):
	root = tk.Tk()
	root.withdraw()
	file_path = filedialog.askopenfilename()
	sample_text = open(file_path, "r").read() 
else:
	sample_text = open("temp.txt").read()


def create_json(word_freq):
	pos_dict = {
			"CC":1,"CD": 2,"DT": 3,"EX": 4,"FW": 5, "IN": 6, 
			"JJ": 7, "JJR": 8,"JJS": 9,"LS": 10, "MD": 11,
			"NN": 12, "NNS": 13, "NNP": 14, "NNPS": 15, "PDT": 16,
			"POS": 17,"PRP": 18,"PRP$": 19, "RB": 20,"RBR": 21,
			"RBS": 22,"RP": 23,"TO": 24,"UH": 25, "VB": 26,
			"VBD": 27, "VBG": 28, "VBN": 29, "VBP": 30, "VBZ": 31,
			"WDT": 32, "WP": 33, "WP$": 34, "WRD": 35
		}
	data = {}
	nodes = []
	links = []			
	
	for word, freq in word_freq.items():
		if nltk.tag.pos_tag([word])[0][1] in pos_dict:
			group = pos_dict[nltk.tag.pos_tag([word])[0][1]]
		else:
			group = 99

		nodes.append({"id": word, "group": group, "label": word, "level": 2})
		links.append( {"source": word, "target": nltk.tag.pos_tag([word])[0][1], "strength": freq})

	nodes.append({"id": "partsOfSpeech", "group": 100, "label": "Parts Of Speech", "level": 3})	
	for tag,val in pos_dict.items():
		nodes.append({"id": tag, "group": val, "label": tag, "level": 1})
		links.append({"source": tag, "target": "partsOfSpeech", "strength": 1})

	data['nodes'] = nodes
	data['links'] = links

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)
		
tokenized = word_tokenize(sample_text)
word_frequency_dist = nltk.FreqDist(tokenized)


word_freq = dict((tokenized, freq) for tokenized, freq in word_frequency_dist.items())
create_json(word_freq)
