#!/usr/bin/python3
def multiple_returns(sentence):
    returns=()
    if not sentence:
        return returns(len(sentence),"None")
    else:
        return returns(len(sentence),sentence[0])
