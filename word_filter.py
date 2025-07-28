def word_filter():
    print("This is the word filter tool.")
    while True:
        print("1-To Exit")
        sentence = input("Enter a sentence: ").lower().strip()
        if sentence == "1":
            break
        banned_words = input(
            "Which words are to be blocked(Write them comma-seperated): ").lower().strip()
        if banned_words == "1":
            break
        banned_words = banned_words.replace(" ", "").split(",")
        words = sentence.split()
        new_sentence = []
        for word in words:
            new_word = word
            for banned_word in banned_words:
                banned_word_length = len(banned_word)
                banned_word_replace = []
                for i in range(banned_word_length):
                    banned_word_replace.append("*")
                new_word = new_word.replace(
                    banned_word, "".join(banned_word_replace))
            new_sentence.append(new_word)
        print("Cleaned sentence:", " ".join(new_sentence))
    print("You exited the word filter.")


word_filter()
