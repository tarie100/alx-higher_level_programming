#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        result = None
    else:
        result = sentence[0]
        print("Length: {:d} - First character: {:s}".format(len(sentence), result))
