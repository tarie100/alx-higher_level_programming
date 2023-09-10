#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return "Length: 0 - First character: None"
    else:
        return "Length: {:d} - First character: {:s}".format(len(sentence), sentence[0])
