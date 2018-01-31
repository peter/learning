# Week 1

## Learning Objectives

Interpret text in terms of its basic building blocks: sentences and words.
Identify common problems with raw text and perform text cleaning tasks in Python.
Write regular expressions to find textual patterns.

## Handling Text in Python

Documents / sentences / words (tokens) / characters

```python
text = 'Ethics are built right into the ideals and objectives of the United Nations '
len(text)

words = text.split(' ')
len(words)

[w for w in words if len(w) > 3]
[w for w in words if w.istitle()]
[w for w in words if w.endswith('s')]

text = 'To be or not to be'
words = text.split(' ')
len(words) # => 6
len(set(words)) # => 5
len(set([w.lower() for w in words])) # => 4
```

Useful string functions:

```
startswith, endswith
isupper, islower, istitle, isalpha, isdigit, isalnum
lower, upper, titlecase
split, splitlines, join
strip, rstrip
find, rfind
replace
```

Getting character list from a string:

```
text = 'This is my text'
list(text)
[c for c in text]
```

Reading files:

```
f = open('foobar.txt', 'r')
f.read()
f.readlines()

with open('workfile') as f:
  data = f.read()

[line for line in open('README.md')]
[l for l in open('README.md') if l.strip()]
```

## Regular Expressions

```python
import re

tweet = "@nltk Text analysis is awesome! #regex #pandas #python"
tweet_words = tweet.strip().split(' ')
[w for w in tweet_words if re.search('#[A-Za-z0-9_]+', w)]
[word for word in tweet.split() if word.startswith('#')]
```

"Python offers two different primitive operations based on regular expressions: re.match() checks for a match only at the beginning of the string, while re.search() checks for a match anywhere in the string (this is what Perl does by default)."

* [re module docs](https://docs.python.org/3/library/re.html)

```python
re.match("c", "abcdef")    # No match
re.search("c", "abcdef")   # Match

def repl(m):
     inner_word = list(m.group(2))
     random.shuffle(inner_word)
     return m.group(1) + "".join(inner_word) + m.group(3)
text = "Professor Abdolmalek, please report your absences promptly."
re.sub(r"(\w)(\w+)(\w)", repl, text) # => 'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'

re.findall()
```

"Raw string notation (r"text") keeps regular expressions sane. Without it, every backslash ('\') in a regular expression would have to be prefixed with another one to escape it."

Regex symbols:

```
. - any character
^ - start
$ - end
* - 0 or more
+ - 1 or more
? - 0 or 1
*?, +?, ?? - non greedy variants of above
{m} - match exactly m repetitions of preceding RE
{m, n} - match between m and n repetitions (greedy)
{m, n}? - match between m and n repetitions (non greedy)
[] - character set
| - or
() - capturing group
(?:) - non capturing group
(?i) - ignore case
(?m) - multiline
(?=...) - positive look ahead
(?<=...) - positive look behind
\b - beginning/end of word
\d - digit
\w - word character
\s - space
```

Verbose:

```python
re.compile(r"""\d +      # the integral part
                \.    # the decimal point
                \d *  # some fractional digits
            """, re.X)
```

## Text Data in Pandas


```python
import pandas as pd

time_sentences = ["Monday: The doctor's appointment is at 2:45pm.",
                  "Tuesday: The dentist's appointment is at 11:30 am.",
                  "Wednesday: At 7:00pm, there is a basketball game!",
                  "Thursday: Be back home by 11:15 pm at the latest.",
                  "Friday: Take the train at 08:10 am, arrive at 09:00am."]

df = pd.DataFrame(time_sentences, columns=['text'])
df

# find the number of characters for each string in df['text']
df['text'].str.len()

# find the number of tokens for each string in df['text']
df['text'].str.split().str.len()

# find which entries contain the word 'appointment'
df['text'].str.contains('appointment')

# find how many times a digit occurs in each string
df['text'].str.count(r'\d')

# find all occurances of the digits
df['text'].str.findall(r'\d')
```

## Internationalization (I18n)

UTF-8 is ubiquitous encoding now and it uses between one and four bytes.
It is backwards compatible with ASCII. Python 3 has UTF-8 support built in.

## Assignment

Date parsing.

* 04/20/2009; 04/20/09; 4/20/09; 4/3/09
* Mar-20-2009; Mar 20, 2009; March 20, 2009;  Mar. 20, 2009; Mar 20 2009;
* 20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009
* Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009
* Feb 2009; Sep 2009; Oct 2010
* 6/2008; 12/2009
* 2009; 2010

* Assume all dates in xx/xx/xx format are mm/dd/yy
* Assume all dates where year is encoded in only two digits are years from the 1900's (e.g. 1/5/89 is January 5th, 1989)
* If the day is missing (e.g. 9/2009), assume it is the first day of the month (e.g. September 1, 2009).
* If the month is missing (e.g. 2010), assume it is the first of January of that year (e.g. January 1, 2010).
* Watch out for potential typos as this is a raw, real-life derived dataset.

Find the correct date in each note and return a pandas Series in chronological order of the original Series' indices. This function should return a Series of length 500 and dtype int
