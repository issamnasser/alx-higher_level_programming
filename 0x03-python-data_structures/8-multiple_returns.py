#!/usr/bin/python3
def multiple_returns(sentence):
    returns=()
    if len(sentence)==0:
        returns=(len(sentence),"None")
    else:
        returns(len(sentence),sentence[0])
    return returns
