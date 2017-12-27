"""
Stephan has a friend who happens to be a little mechbird. Recently, he was trying to teach it how to speak basic language. Today the bird spoke its first word: "hieeelalaooo". This sounds a lot like "hello", but with too many vowels. Stephan asked Nikola for help and he helped to examine how the bird changes words. With the information they discovered, we should help them to make a translation module.

The bird converts words by two rules:
- after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
Vowels letters == "aeiouy".

You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one whitespace). The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given in lowercase. You should translate this phrase from the bird language to something more understandable.

Input: A bird phrase as a string.

Output: The translation as a string.

Precondition: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
A phrase always has the translation.
"""

VOWELS = "aeiouy"


def translate(value):
    words = value.split(' ')
    new_words = []

    for word in words:
        new_word = ''
        letters = list(word)

        for letter in letters:
            new_word += letter
            if letter in VOWELS:
                try:
                    letters.pop(letters.index(letter) + 1)
                    letters.pop(letters.index(letter) + 1)
                except IndexError:
                    continue
            else:
                try:
                    letters.pop(letters.index(letter) + 1)
                except IndexError:
                    continue

        new_words.append(new_word)

    return " ".join(word for word in new_words)

if __name__ == '__main__':
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
