import nltk
from nltk.corpus import gutenberg

nltk.download('gutenberg')
text_ids = gutenberg.fileids()

corpus_data = []
for text_id in text_ids:
    text = nltk.corpus.gutenberg.raw(text_id)
    corpus_data.append(text)


