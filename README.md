# Auto-Complete
## Google Project

In this project there is an implementation for one feature of Google's search engines - AutoComplete.

Autocomplete, or word completion, is a feature in which an application predicts the rest of a word a user is typing.

The purpose of the completion action is to make it easier for the user to find the most appropriate sentence.

Once entering some text the user will get the five closest completions to the input.

If there are five sentences that the text is their sub-string, they will be returned. Otherwise will be returned sentences containing the sub-string with one of the changes - a missing letter, additional letter, or a replaced letter.

If the user insert `#`, start a new word to search.

The results will be from sentences within given input text files.

You can upload your own files. in `data_manager.py`, line `4`, change to your path to folder.

## Example:

![image](https://user-images.githubusercontent.com/86183775/128430542-4a77b638-1945-4eb1-ab8c-70b42d290760.png)

