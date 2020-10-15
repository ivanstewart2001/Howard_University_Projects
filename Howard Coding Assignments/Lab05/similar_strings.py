def evaluate_first_word (s):
    x = list(s)
    index = 0
    new = []
    while index < 1:
        for i in x:
            y = ord(i)
            new.append(y)
        index += 1
    return new

def evaluate_second_word (s):
    x = list(s)
    index = 0
    new = []
    while index < 1:
        for i in x:
            y = ord(i)
            new.append(y)
        index += 1
    return new

def different_character_evaluator(s1, s2):
    x = set(evaluate_first_word(s1))
    y = set(evaluate_second_word(s2))
    a = x.difference(y)

    if x == y:
        return True
    elif len(a) <= 1:
        return True
    else:
        return False

def missing_character_evaluator(s1, s2):
    x = set(evaluate_first_word(s1))
    y = set(evaluate_second_word(s2))
    a = x.difference(y)

    if x == y:
        return True
    elif len(a) <= 1:
        return True
    else:
        return False

def extra_character_evaluator(s1, s2):
    x = set(evaluate_first_word(s1))
    y = set(evaluate_second_word(s2))
    a = y.difference(x)

    if x == y:
        return True
    elif len(a) <= 1:
        return True
    else:
        return False

def are_strings_similar(s1, s2):
    x = set(evaluate_first_word(s1))
    y = set(evaluate_second_word(s2))
    a = y.difference(x)
    b = x.difference(y)
    if x == y:
        return True
    elif len(a) <= 1:
        evaluate = different_character_evaluator(s1, s2)
        return evaluate
    elif len(a) <= 1:
        evaluate = missing_character_evaluator(s1, s2)
        return evaluate
    elif len(b) <= 1:
        evaluate = extra_character_evaluator(s1, s2)
        return evaluate
    else:
        return False

print(are_strings_similar('spot', 'SPOT'))