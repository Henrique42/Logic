import cnf_parser
import truth_table

#Init
def main():
    op = ''
    
    while(op != '0'):
        print('\n 1: TRUTH TABLE \n 2: CNF PARSER \n 0. Encerrar')
        print('_____________________')
        op = input('Choose one option: ')

        if(op == '1'):
            truth_table.ttable()
        elif (op == '2'):
            cnf_parser.cnf()
        elif (op == '0'):
            print('Execution ended!')
        else:
            print('Invalid option!')

main()