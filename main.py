from auto_completion import AutoCompletion


def user_interface(auto_complete):
    """Get an input sentence from the user and print the completion suggestions"""
    while True:
        _input = input("Enter your text:\n")
        sentence = _input[:]
        node = auto_complete.data_manager.get_trie().root
        while _input != "#":
            completions, node = auto_complete.get_completions(sentence, node, len(sentence))
            if not len(completions):
                print("Sorry, There aren't any suggestion...")
            else:
                print(f"Here are {len(completions)} suggestions:")
                for i in range(len(completions)):
                    print(f"{i+1}. " + completions[i])
            print()
            _input = input(sentence)
            sentence += _input


if __name__ == '__main__':
    auto_complete = AutoCompletion()
    auto_complete.data_manager.reboot()
    user_interface(auto_complete)

