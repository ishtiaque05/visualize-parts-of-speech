# Parts of Speech Visualization

This repo demonstrate how we can tag parts of speech using python NLTK package.

To run this repo:

1. clone the repo
2. create a virtualenv and pip3 install -r requirements.txt
3. run: python3 createPosNetwork.py which will generate the data.json files
4. setup an http server to serve the index.html page
5. view the in web browser

Demo:
![Parts Of Speech Visualization](https://github.com/ishtiaque05/visualize-parts-of-speech/blob/master/pos.png)


## POS tag list:

1. CC	coordinating conjunction
2. CD	cardinal digit
3. DT	determiner
4. EX	existential there (like: "there is" ... think of it like "there exists")
5. FW	foreign word
6. IN	preposition/subordinating conjunction
7. JJ	adjective	'big'
8. JJR	adjective, comparative	'bigger'
9. JJS	adjective, superlative	'biggest'
10. LS	list marker	1)
11. MD	modal	could, will
12. NN	noun, singular 'desk'
13. NNS	noun plural	'desks'
14. NNP	proper noun, singular	'Harrison'
15. NNPS	proper noun, plural	'Americans'
16. PDT	predeterminer	'all the kids'
17. POS	possessive ending	parent's
18. PRP	personal pronoun	I, he, she
19. PRP$	possessive pronoun	my, his, hers
20. RB	adverb	very, silently,
21. RBR	adverb, comparative	better
22. RBS	adverb, superlative	best
23. RP	particle	give up
24. TO	to	go 'to' the store.
25. UH	interjection	errrrrrrrm
26. VB	verb, base form	take
27. VBD	verb, past tense	took
28. VBG	verb, gerund/present participle	taking
29. VBN	verb, past participle	taken
30. VBP	verb, sing. present, non-3d	take
31. VBZ	verb, 3rd person sing. present	takes
32. WDT	wh-determiner	which
33. WP	wh-pronoun	who, what
34. WP$	possessive wh-pronoun	whose
35. WRB	wh-abverb	where, when
