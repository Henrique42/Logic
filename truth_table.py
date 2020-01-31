from itertools import product

#TRUTH TABLE

#Replaces
def ttable_aux(text):
    return text.replace('True', 'T').replace('False', 'F').replace('0', 'F').replace('1', 'T')

#Main function
def ttable():
    print('\nTRUTH TABLE')
    h = input('Tip the formula: ')
    h1 = h.strip().replace('>', '<=').replace('%', '==').replace('~', '1 - 1 * ').replace('&', 'and').replace('|', 'or')
    formula = compile(h1, '<string>', 'eval')
    #Get the propositions from the formula
    propositions = formula.co_names

    #Catch invalid formulas
    if h not in propositions and 'True' not in h and 'False' not in h and '>' not in h and '%' not in h and '~' not in h and '&' not in h and '|' not in h:    
        print('Invalid formula!')
    else:
        print(' || '.join(propositions), '||', h)
        for var in product([False, True], repeat=len(propositions)):
            #Generate a list combining the propositions and true/false values 
            aux = dict(zip(propositions, var))
            #print the truth table
            print(ttable_aux(' || '.join(str(v) for v in var)), '||', ttable_aux(str(eval(formula, aux))))



