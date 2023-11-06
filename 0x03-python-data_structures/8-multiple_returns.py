#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        firstchar = sentence[0]
        return (length, firstchar)
    else:
        return (0, None)
