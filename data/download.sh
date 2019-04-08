#!/bin/sh

echo "Downloading corpus"
# wget http://www.cl.ecei.tohoku.ac.jp/~shimaoka/corpus.zip
# unzip corpus.zip
# rm corpus.zip

#OntoNotes
python converter.py corpus/OntoNotes/all.txt corpus/OntoNotes/all.json
python converter.py corpus/OntoNotes/train.txt corpus/OntoNotes/train.json
python converter.py corpus/OntoNotes/test.txt corpus/OntoNotes/test.json
python converter.py corpus/OntoNotes/dev.txt corpus/OntoNotes/dev.json

#Wiki
python converter.py corpus/Wiki/all.txt corpus/Wiki/all.json
python converter.py corpus/Wiki/train.txt corpus/Wiki/train.json
python converter.py corpus/Wiki/test.txt corpus/Wiki/test.json
python converter.py corpus/Wiki/dev.txt corpus/Wiki/dev.json


echo "Downloading word embeddings..."
wget http://nlp.stanford.edu/data/glove.840B.300d.zip
unzip glove.840B.300d.zip
# rm glove.840B.300d.zip
