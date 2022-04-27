# -*- coding: utf-8 -*-

"""Main module."""

"""
count words script
"""

from bs4 import BeautifulSoup


class Counter:
    """
    class for counting words given a string
    """

    def __init__(self, sentence):
        """
        class constructor
        :param sentence: str [text whose words are to be counted]
        """
        assert isinstance(sentence, str)
        self.sentence = sentence

    def __repr__(self):
        """
        class representation
        :return: str
        """
        return f"<{self.sentence}>"

    def count_words(self):
        """
        Method that counts words
        :return: integer
        """
        self.extract_text_from_possible_html_string
        words_list = self.sentence.split()
        return len(words_list)

    @property
    def extract_text_from_possible_html_string(self):
        """
        Run through the text through beautiful soup
        and extract text
        """
        soup = BeautifulSoup(self.sentence, 'html.parser')
        all_elements = soup.find_all()
        if len(all_elements) != 0:
            self.sentence = all_elements[0].text


if __name__ == "__main__":
    text = "<h1> I am trying hard </h1>"
    obj = Counter(text)
    print(obj.extract_text_from_possible_html_string())
