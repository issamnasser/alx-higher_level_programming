def multiple_returns(sentence):
    returns = ()
    if len(sentence) == 0:
        returns = 0, "None"
    else:
        returns = len(sentence), sentence[0]
    return returns
