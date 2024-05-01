def reversePrefix(word: str, ch: str) -> str:
    idx = word.find(ch)
    return word if idx == -1 else word[:idx + len(ch)][::-1] + word[idx + len(ch):]


if __name__ == '__main__':
    print("dcbaefd" == reversePrefix("abcdefd", "d"))