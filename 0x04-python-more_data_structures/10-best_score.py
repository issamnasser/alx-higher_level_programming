#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        score_list = list(a_dictionary.values())
        max = 0
        for i in score_list:
            if i > max:
                max = i
        for name, score in a_dictionary.items():
            if score == max:
                return name
