from data_manager import DataManager
import string

RESULT_LEN = 5


class AutoCompletion:

    def __init__(self):
        self.data_manager = DataManager()
        self.decrement_scores = {"search_replaced": [5, 4, 3, 2, 1],
                                 "search_added": [10, 8, 6, 4, 2],
                                 "search_removed": [10, 8, 6, 4, 2]}

    def search_replaced_sentence(self, sentence, node, idx, num_of_sentences):
        """Search the sentence with replaced letter"""
        completions = {}
        for letter in string.ascii_lowercase:
            if len(completions) >= num_of_sentences:
                return completions, node
            result, node = self.data_manager.sentences_trie.search_sentence(sentence[:idx]+letter+sentence[idx+1:], node)
            if result:
                completions.update(result)
        return completions, node

    def search_added_sentence(self, sentence, node, idx, num_of_sentences):
        """Search the sentence with added letter"""
        completions = {}
        for letter in string.ascii_lowercase:
            if len(completions) >= num_of_sentences:
                return completions, node
            result, node = self.data_manager.sentences_trie.search_sentence(sentence[:idx] + letter + sentence[idx:], node)
            if result:
                completions.update(result)
        return completions, node

    def search_removed_sentence(self, sentence, node, idx):
        """Search the sentence with removed letter"""
        result, node = self.data_manager.sentences_trie.search_sentence(sentence[:idx] + sentence[idx + 1:], node)
        return (result, node) if result else ({}, node)

    def get_completions(self, sentence, node, all_sentence_len):
        """Get the input sentence and search completion suggestions for it."""
        completions, completions_sentences = [], []
        sentence = sentence.lower().replace("  ", " ", len(sentence))
        base_scores = 2 * all_sentence_len

        # Search the original sentence
        result, current_node = self.data_manager.sentences_trie.search_sentence(sentence, node)
        if result:
            completions += self.manipulate_result(result, completions_sentences, base_scores)
        if len(completions) >= RESULT_LEN:
            return completions[:RESULT_LEN], current_node

        # Search sentences with replaced letter
        for idx in reversed(range(len(sentence)+1)):
            result, current_node = self.search_replaced_sentence(sentence, node, idx, RESULT_LEN-len(completions))
            completions += self.manipulate_result(result, completions_sentences, base_scores-self.decrement_scores["search_replaced"][min(4, idx)])
            if len(completions) >= RESULT_LEN:
                return completions[:RESULT_LEN], current_node

        # Search sentences with added letter
        for idx in reversed(range(len(sentence)+1)):
            result, current_node = self.search_added_sentence(sentence, node, idx, RESULT_LEN-len(completions))
            completions += self.manipulate_result(result, completions_sentences, base_scores-self.decrement_scores["search_added"][min(4, idx)])
            if len(completions) >= RESULT_LEN:
                return completions[:RESULT_LEN], current_node

        # Search sentences with removed letter
        for idx in reversed(range(len(sentence)+1)):
            result, current_node = self.search_removed_sentence(sentence, node, idx)
            completions += self.manipulate_result(result, completions_sentences, base_scores-self.decrement_scores["search_removed"][min(4, idx)])
            if len(completions) >= RESULT_LEN:
                return completions[:RESULT_LEN], current_node

        return completions[:RESULT_LEN], current_node

    def manipulate_result(self, result, completions_sentences, scores):
        """Prepare the result with all the data for printing"""
        indexes = list(result.items())
        result = []
        for i in range(min(len(indexes), RESULT_LEN-len(completions_sentences))):
            sentence, sentence_data = self.data_manager.get_sentence_data(indexes[i][0])
            if not any([sentence == com_sentence for com_sentence in completions_sentences]):
                result += [f"{sentence} " + "(" + sentence_data + f", {indexes[i][1]}) score: {scores}"]
                completions_sentences += [sentence]
        return result

