# Created by: Jason MacLafferty
# Created on: 18 November 2012
# Finished on: 25 November 2012
# Project Name: Evaluate Math Expression

# version 0 -- get the basics up and running
# version 1 -- add fancier, nicer answer output, like pretty print output of the original inputed polynomial etc.
# version 2 -- fine-tune and tweak version 1, revise and rewrite function to pretty-print the inputed polynomial and the string parsing capabilities of the function
# can_be_number
# version 3 -- split source code between multiple files

# ===========================
# pull in needed helper functions
import exp_math_v3b
# ===========================
# Begin Function Definitions

# the following function may not be acceptable in its design or use.
# However, it represents a C style language "main" like method to start the application.
# It is invoked at the bottom of the program script--not automatically like a "main" application
# entry-point method in a C style language.
def main():
    '''None -> None
    Grabs a strings of input from the user, calls data validation functions on the input,
    and if the input is valid it calls a function to begin processing the data.'''
    
    inputstr = raw_input('Please enter a valid expression representing a mathematical polynomial.\n' +
                         'If you want help to know the proper format for this expression,\n' +
                         'please type, "h" or "help." ')
    
    if inputstr == 'h' or inputstr == 'help':
        print 'The format for an input expression representing a mathematical polynomial is as follows:\n' + \
        '"a:b,c:d,e:f" ... etc. the first character of each comma-separated pair of sub-expressions represents\n' + \
        'the coefficient of a monomial and the second number after the colon represents the power of the monomial.\n' + \
        'Two examples are: "3:2,5:4,1:3" which stands for: "3x^2 + 5x^4 + x^3", the second example is: "4.7:2,3.27:5,2.1:7",\n' + \
        'which represents: "4.7x^2 + 3.27x^5 + 2.1x^7". Please note that the "x" character in all of the examples stands for:\n' + \
        'the independent variable of the polynomial expression or equation.'
    else:
        is_valid_input = exp_math_v3b.is_data_valid(inputstr)
        if is_valid_input:
            result = start_processing(inputstr)
        else:
            while is_valid_input == False:
                inputstr = raw_input('Please input a valid expression representing a mathematical polynomial. ')
                is_valid_input = exp_math_v3b.is_data_valid(inputstr)
            
            result = start_processing(inputstr)
            
        if '.0' == str(result['answer'])[:-2]:
            result['answer'] = int(result['answer'])
        
        pretty_print_polynomial = exp_math_v3b.pretty_polynomial(inputstr)
        
        print 'the value of the specified polynomial:', pretty_print_polynomial
        print 'where x =', result['x']
        print 'is:', result['answer']
        
def start_processing(valid_expression):
    '''str -> float
    Accepts a valid expression representing a mathematical polynomial and starts the the processing of it.
    Furthermore, it returns the result.'''
    
    x_val_str = grab_number_str()
    terms = exp_math_v3b.list_of_terms(valid_expression)
    result = exp_math_v3b.exp_evaluate(terms, x_val_str)
    
    return result

def grab_number_str():
    '''None -> str
    Grabs a numerical value string from the user, validates it and returns the validated string value.'''
    
    is_valid_number = False
    
    while is_valid_number == False:
        input_num_str = raw_input('Please enter a valid numerical value to evaluate the inputed polynomial for. ')
        is_valid_number = exp_math_v3b.can_be_number(input_num_str)
    
    return input_num_str
            
# End Function Definitions
# ===========================

# ===========================
# Begin Function Invokation(s)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    main()

# End Function Invokation(s)
# ===========================
