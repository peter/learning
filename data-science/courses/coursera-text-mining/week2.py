import nltk
nltk.download()
from nltk.book import *

# *** Introductory Examples for the NLTK Book ***
# Loading text1, ..., text9 and sent1, ..., sent9
# Type the name of the text or sentence to view it.
# Type: 'texts()' or 'sents()' to list the materials.
# text1: Moby Dick by Herman Melville 1851
# text2: Sense and Sensibility by Jane Austen 1811
# text3: The Book of Genesis
# text4: Inaugural Address Corpus
# text5: Chat Corpus
# text6: Monty Python and the Holy Grail
# text7: Wall Street Journal
# text8: Personals Corpus
# text9: The Man Who Was Thursday by G . K . Chesterton 1908

### Counting vocabulary of words

len(sent7)

len(text7)

len(set(text7))

list(set(text7))[:10]

dist = FreqDist(text7)
len(dist)

vocab1 = dist.keys()
list(vocab1)[:10]

dist['four']

freqwords = [w for w in vocab1 if len(w) > 5 and dist[w] > 100]

### Normalization and stemming

input1 = "List listed lists listing listings"
words1 = input1.lower().split(' ')

porter = nltk.PorterStemmer()
[porter.stem(t) for t in words1]

### Lemmatization

udhr = nltk.corpus.udhr.words('English-Latin1')
udhr[:20]

[porter.stem(t) for t in udhr[:20]] # Still Lemmatization

WNlemma = nltk.WordNetLemmatizer()
[WNlemma.lemmatize(t) for t in udhr[:20]]

### Tokenization

text11 = "Children shouldn't drink a sugary drink before bed."
text11.split(' ')

nltk.word_tokenize(text11)

text12 = "This is the first sentence. A gallon of milk in the U.S. costs $2.99. Is this the third sentence? Yes, it is!"
sentences = nltk.sent_tokenize(text12)
len(sentences)

sentences

## Advanced NLP Tasks with NLTK

### POS tagging

nltk.help.upenn_tagset('MD')

text13 = nltk.word_tokenize(text11)
nltk.pos_tag(text13)

text14 = nltk.word_tokenize("Visiting aunts can be a nuisance")
nltk.pos_tag(text14)

# Parsing sentence structure
text15 = nltk.word_tokenize("Alice loves Bob")
grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP
NP -> 'Alice' | 'Bob'
V -> 'loves'
""")

parser = nltk.ChartParser(grammar)
trees = parser.parse_all(text15)
for tree in trees:
    print(tree)

text16 = nltk.word_tokenize("I saw the man with a telescope")
grammar1 = nltk.data.load('mygrammar.cfg')
grammar1

parser = nltk.ChartParser(grammar1)
trees = parser.parse_all(text16)
for tree in trees:
    print(tree)

from nltk.corpus import treebank
text17 = treebank.parsed_sents('wsj_0001.mrg')[0]
print(text17)

### POS tagging and parsing ambiguity

text18 = nltk.word_tokenize("The old man the boat")
nltk.pos_tag(text18)

text19 = nltk.word_tokenize("Colorless green ideas sleep furiously")
nltk.pos_tag(text19)
