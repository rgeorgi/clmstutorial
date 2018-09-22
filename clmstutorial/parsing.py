"""
This module implements methods to load a parser
and return a parse
"""

from nltk.parse import EarleyChartParser, ParserI
from nltk.tokenize import word_tokenize
import nltk

def init_parser(grammar_path) -> EarleyChartParser:
    """
    Read a grammar file from disk and use it to create
    an EarleyChartParser

    :param grammar_path: Path to the CFG grammar file (*.cfg)
    :return: EarleyChartParser using that grammar.
    """
    grammar = nltk.load(grammar_path)
    parser = EarleyChartParser(grammar)
    return parser

def parse_sent(parser: ParserI, sentence: str):
    """
    Given a sentence string and a parser, tokenize that
    string and return a parse.

    :param parser: Any parser implementing NLTK's "parse()" method.
    :param sentence: An iterable of strings, pre-tokenized.
    :return: An NLTK tree() object.
    """
    word_tokens = word_tokenize(sentence)
    tree = parser.parse(word_tokens)
    return tree