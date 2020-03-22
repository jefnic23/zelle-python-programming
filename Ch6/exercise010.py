phrase = input('Enter phrase: ')

def acronym(phrase):
    acro = [p[0] for p in phrase.split()]
    print('Acronym: {}'.format(''.join(acro).upper()))

acronym(phrase)
