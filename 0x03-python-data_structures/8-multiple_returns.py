def multiple_returns(sentence):
    returns=()
    if not sentence:
        returns=(0, "None")
    else:
        returns=(len(sentence), sentence[0])
    return returns
