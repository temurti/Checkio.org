def longest_palindromic(text):
    text = text.lower()
    results = []

    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]

            if chunk == chunk[::-1]:
                results.append(chunk)

    if not results:
        return text[0]
    else:
        return max(results, key=len)


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
