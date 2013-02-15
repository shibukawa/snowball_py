import sys
import re

import snowballstemmer
from snowballstemmer.danish_stemmer import DanishStemmer
from snowballstemmer.dutch_stemmer import DutchStemmer
from snowballstemmer.english_stemmer import EnglishStemmer
from snowballstemmer.finnish_stemmer import FinnishStemmer
from snowballstemmer.french_stemmer import FrenchStemmer
from snowballstemmer.german_stemmer import GermanStemmer
from snowballstemmer.hungarian_stemmer import HungarianStemmer
from snowballstemmer.italian_stemmer import ItalianStemmer
from snowballstemmer.norwegian_stemmer import NorwegianStemmer
from snowballstemmer.porter_stemmer import PorterStemmer
from snowballstemmer.portuguese_stemmer import PortugueseStemmer
from snowballstemmer.romanian_stemmer import RomanianStemmer
from snowballstemmer.russian_stemmer import RussianStemmer
from snowballstemmer.spanish_stemmer import SpanishStemmer
from snowballstemmer.swedish_stemmer import SwedishStemmer
from snowballstemmer.turkish_stemmer import TurkishStemmer

stemmers = {
    'danish': DanishStemmer,
    'dutch': DutchStemmer,
    'english': EnglishStemmer,
    'finnish': FinnishStemmer,
    'french': FrenchStemmer,
    'german': GermanStemmer,
    'hungarian': HungarianStemmer,
    'italian': ItalianStemmer,
    'norwegian': NorwegianStemmer,
    'porter': PorterStemmer,
    'portuguese': PortugueseStemmer,
    'romanian': RomanianStemmer,
    'russian': RussianStemmer,
    'spanish': SpanishStemmer,
    'swedish': SwedishStemmer,
    'turkish': TurkishStemmer
}


def usage():
    print("testapp.py <algorithm> \"sentence\"...")

def main():
    argv = sys.argv
    if len(argv) < 1:
        usage()
        return
    algorithm = 'english'
    if len(argv) > 2:
        algorithm = argv[1]
        argv = argv[2:]
    else:
        argv = argv[1:]
    stemmerClass = stemmers.get(algorithm.lower(), EnglishStemmer)
    stemmer = stemmerClass()
    splitter = re.compile(r"[\s\.-]")
    for arg in argv:
        for word in splitter.split(arg):
            if word == '':
                continue
            original = word.lower()
            print(original + " -> " + stemmer.stem(original))
main()
