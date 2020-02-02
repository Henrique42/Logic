from itertools import product

#Parse the formula to DNF
def parser(propositions, formula):
    h2 = []
    h3 = []

    for var in product([False, True], repeat=len(propositions)):
            aux_list = dict(zip(propositions, var))
            #Get the truth table
            result = eval(formula, aux_list)
            
            #append false values
            if result == False or result == 0:
                h2.append([str(v) for v in var])
    if h2 == []:
        return [[True]]
    else:
        for i in h2:
            aux = []
            
            for j in range(0, len(i)):
                if i[j] == 'True':
                    aux.append(propositions[j])
                else:
                    aux.append(propositions[j])

            h3.append(aux)

        return h3

#Main
def dnf():
    print('\nDNF PARSER')
    h = input('Tip the formula: ')
    h1 = h.strip().replace('>', '<=').replace('%', '==').replace('~', '1 - 1 * ').replace('&', 'and').replace('|', 'or')
    formula = compile(h1, '<string>', 'eval')
    #Get propositions
    propositions = formula.co_names

    #Catch invalid formulas
    if h not in propositions and'True' not in h and 'False' not in h and '>' not in h and '%' not in h and '~' not in h and '&' not in h and '|' not in h:
        print('Invalid formula!')
    else:
        print('List of clauses: ', parser(propositions, formula))