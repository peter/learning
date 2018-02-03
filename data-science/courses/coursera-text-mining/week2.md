# Week 2

What is NLP? Any computation or manipulation of natural language.

Natural languages evolve - words are added or removed or change meaning, rules
may change. Examples of tasks:

* Counting words
* Finding sentences
* Part of speech tagging
* Semantic roles
* Identifying entities in a sentence

Tokenization (normalization), lemmatization and stemming are quite
important pre-processing tasks in NLP and they are non-trivial.

Normalization: `.lower().split(' ')`

Stemming:

```python
porter = nltk.PorterStemmer()
# List, listed, lists, listing, listings -> list
[porter.stem(t) for t in words]
```

Lemmatization: the resulting words should actually be meaningful/valid dictionary words.

```python
nltk.word_tokenize(text)
nltk.sent_tokenize(text)
```

[POS tagging](https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/):

```python
nltk.pos_tag(nltk.word_tokenize(text))
```

Ambiguity:

"Visiting aunts can be a nuisance"
"I saw the man with the telescope"

Treebank parse tree

Parsing grammatical structure helps provide meaning. Better models could be learned
with supervised learning.

What is the lexical diversity of the given text input? (i.e. ratio of unique tokens to the total number of tokens)

```python
tokens = nltk.word_tokenize(moby_raw)
total_count = len(tokens)
unique_count = len(set(tokens))
lexical_diversity = unique_count/total_count # => 0.081
```

```python
from nltk.probability import FreqDist
tokens = nltk.word_tokenize(moby_raw)
dist = FreqDist(word.lower() for word in tokens)
word_count = dist['whale'] # => 1086
total_count = len(tokens)
word_count / total_count
```

[20 most common words](http://www.ling.helsinki.fi/kit/2009s/clt231/NLTK/book/ch01-LanguageProcessingAndPython.html#frequency-distributions):

```python
from nltk.probability import FreqDist
tokens = nltk.word_tokenize(moby_raw)
dist = FreqDist(word.lower() for word in tokens)
# words = list(dist.keys())[:20]
[(w, f) for w, f in dist.most_common(20)]
```

* [Counting word frequency using NLTK FreqDist()](https://www.strehle.de/tim/weblog/archives/2015/09/03/1569)

```
[stemmer.stem(w.lower()) for w in nltk.word_tokenize(text) if len(w) > 0 and not w.isnumeric() and not w in stopwords]
```

```python
def answer_three():
    from nltk.probability import FreqDist
    dist = FreqDist(moby_tokens)
    # words = list(dist.keys())[:20]
    return dist.most_common(20)
#     sortedToken = sorted(list(set(moby_tokens)), key=lambda token: dist[token], reverse=True)
#     return [(token, dist[token]) for token in sortedToken[:20]]
```


What tokens have a length of greater than 5 and frequency of more than 150?

```python
def answer_four():
    from nltk.probability import FreqDist
    dist = FreqDist(moby_tokens)
    tokens = set([t for t in set(moby_tokens) if len(t) > 5 and dist[t] > 150])
    return sorted(tokens)
#     frequentTokens = [token for token in set(moby_tokens) if len(token)>5 and dist[token]>150]
#     frequentTokens.sort()
#     return frequentTokens
```

Longest word:

```python
from nltk.probability import FreqDist
tokens = nltk.word_tokenize(moby_raw)
longest_len = 0
longest_word = None
for word in tokens:
    if len(word) > longest_len:
        longest_len = len(word)
        longest_word = word
(longest_word, longest_len) # => ("twelve-o'clock-at-night", 23)

# Shorter:
lengths = [(len(w), w) for w in tokens]
(longest_len, longest_word) = sorted(lengths, reverse=True)[0]
(longest_word, longest_len)
```

What unique words have a frequency of more than 2000? What is their frequency?
"Hint:  you may want to use `isalpha()` to check if the token is a word and not punctuation."
*This function should return a list of tuples of the form `(frequency, word)` sorted in descending order of frequency.*

```python
def answer_six():
    from nltk.probability import FreqDist
    dist = FreqDist(moby_tokens)
    words = set([(dist[w], w) for w in moby_tokens if w.isalpha() and dist[w] > 2000])
    return sorted(words, reverse=True)
#     words = [w for w in set(text1) if w.isalpha() and dist[w]>2000]
#     words.sort(key=lambda word:dist[word], reverse=True)
#     return [(dist[word], word) for word in words]
```

What is the average number of tokens per sentence?

```python
def answer_seven():
    sentences = nltk.sent_tokenize(moby_raw)
    tokens_per_sentence = [len(nltk.word_tokenize(s)) for s in sentences]
    return sum(tokens_per_sentence)/len(sentences)
```

What are the 5 most frequent parts of speech in this text? What is their frequency?

This function should return a list of tuples of the form (part_of_speech, frequency) sorted in descending order of frequency.

```python
def answer_eight():
    from collections import Counter
    sentences = nltk.sent_tokenize(moby_raw)
    pos = [nltk.pos_tag(s) for s in sentences]
    tags = [t for p in pos for (w, t) in p]
    print(f'pm debug pos[0]={pos[0]} tags[0]={tags[0]}')
    counts = Counter(tags)
    return counts.most_common(5)
```

## Part 2 - Spelling Recommender

For this part of the assignment you will create three different spelling recommenders, that each take a list of misspelled words and recommends a correctly spelled word for every word in the list.

For every misspelled word, the recommender should find find the word in `correct_spellings` that has the shortest distance*, and starts with the same letter as the misspelled word, and return that word as a recommendation.

```python
def jaccard_distance(label1, label2):
    """Distance metric comparing set-similarity.
    """
    return (len(label1.union(label2)) - len(label1.intersection(label2)))/len(label1.union(label2))


def answer_nine(entries=['cormulent', 'incendenece', 'validrate']):
    results = []
    for entry in entries:
        candidates = [w for w in correct_spellings if w[0] == entry[0]]
        results.append(min(candidates, key=
                           lambda candidate:nltk.jaccard_distance(set(nltk.ngrams(entry, n=3)), set(nltk.ngrams(candidate, n=3)))))
    return results

def answer_ten(entries=['cormulent', 'incendenece', 'validrate']):
    results = []
    for entry in entries:
        candidates = [w for w in correct_spellings if w[0] == entry[0]]
        results.append(min(candidates, key=
                           lambda candidate:nltk.jaccard_distance(set(nltk.ngrams(entry, n=4)), set(nltk.ngrams(candidate, n=4)))))
    return results    


def answer_eleven(entries=['cormulent', 'incendenece', 'validrate']):
    results = []
    for entry in entries:
        candidates = [w for w in correct_spellings if w[0] == entry[0]]
        results.append(min(candidates, key=
                           lambda candidate:nltk.edit_distance(entry, candidate)))
    return results
```

* [distance functions in NLTK](http://www.nltk.org/_modules/nltk/metrics/distance.html)
