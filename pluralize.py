def pluralize(word):
    if word == 'mouse':
        word = 'mice'
    elif word == 'automaton':
        word = 'automata'
    elif word == 'moose':
        word = 'moose'
    else:
        word = word + 's'
    return word

print(pluralize(input('Word please: ')))