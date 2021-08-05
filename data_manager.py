import os
from operator import itemgetter
from sentences_trie import SentencesTrie
DATA_PATH = "./2021-archive\\python-3.8.4-docs-text\\using/"


class DataManager:

    def __init__(self):
        self.sentences_array = []
        self.sentences_trie = None

    def reboot_array(self):
        """Read the files and insert sentences with data to the array of sentences"""
        dir_path = os.path.dirname(DATA_PATH)
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                with open(root[2:] + '\\' + file, encoding='utf8') as text_file:
                    line_number = 0
                    for line in text_file.readlines():
                        line_number += 1
                        self.sentences_array.append(
                            {"txt": line.strip(), "file": file.replace(".txt", ""), "line": line_number})
        self.sentences_array = sorted(self.sentences_array, key=itemgetter('txt'))

    def reboot_trie(self):
        """Insert each sentence with all its suffixes to the trie of suffixes"""
        self.sentences_trie = SentencesTrie()
        for i in range(len(self.sentences_array)):
            for j in range(len(self.sentences_array[i]['txt'])):
                self.sentences_trie.insert_sentence(self.sentences_array[i]['txt'][j:], (i, j))

    def reboot(self):
        """Reboot the system with all the needed data"""
        print("Loading the files and preparing the system...")
        self.reboot_array()
        self.reboot_trie()
        print("The system is ready :)")

    def get_sentence_data(self, sentence_index):
        """Get an index and return the data of the sentence in this index in the array"""
        return self.sentences_array[sentence_index]['txt'], f"{self.sentences_array[sentence_index]['file']}, {self.sentences_array[sentence_index]['line']}"

    def get_trie(self):
        """Return the trie pointer"""
        return self.sentences_trie

