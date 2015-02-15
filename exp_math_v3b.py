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
# Begin Helper Function Definitions

def pretty_polynomial(inputstr):
    '''str -> str
    Returns a pretty print string of the polynomial specified by the, "inputstr," parameter.
    >>> pretty_polynomial('7:3,2:1,3:0')
    '7x^3 + 2x + 3'
    >>> pretty_polynomial('1:5,2:3,7:2')
    'x^5 + 2x^3 + 7x^2'
    >>> pretty_polynomial('1:1,1:7')
    'x + x^7'
    >>> pretty_polynomial('-1:7,2:3')
    '-x^7 + 2x^3'
    >>> pretty_polynomial('1:7')
    'x^7'
    >>> pretty_polynomial('1:5,-3:2,5:0')
    'x^5 - 3x^2 + 5'
    >>> pretty_polynomial('-1.0004:3,7:7')
    '-1.0004x^3 + 7x^7'
    >>> pretty_polynomial('1:0')
    '1'
    '''
    
    terms = list_of_terms(inputstr)
    pretty_poly = ''
    for coefficient, power in terms:
        sign, variable = '', ''
        
        if coefficient == '0':
            sign, coefficient, variable, power = '', '', '', ''
        elif coefficient == '1':
            if power == '0':
                sign, coefficient = ' + ', '1'
            else:
                sign, coefficient = ' + ', ''
        elif coefficient == '-1':
            sign, coefficient = ' - ', ''
        elif coefficient[0] == '-':
            sign, coefficient = ' - ', coefficient[1:]
        else:
            sign = ' + '
        
        if power == '0':
            variable, power = '', ''
        elif power == '1':
            variable, power = 'x', ''
        else:
             variable = 'x^'
        
        pretty_poly += sign + coefficient + variable + power
    
    if pretty_poly[:3] == ' - ':
        return '-' + pretty_poly[3:]
    else:
        return pretty_poly[3:] # strip off ' + ' character sequence from beginning of pretty-print polynomial string
                
def is_data_valid(inputstr):
    '''str -> bool
    Takes a string as an input and returns a bool indicating whether or not it
    properly identifies a valid mathematical expression.
    the form of the expression must be:
    "a:b,c:d,e:f"... where this representes a mathematical expression in the form of:
    ax^b + cx^d + ex^f and so on where "x" is the independent variable of the expression or function.
    a, c, and e represent the polynomial coefficients and b, d, and f represent the powers of each polynomial term.
    >>> is_data_valid('3:2,5:3')
    True
    >>> is_data_valid('3:1,2:x')
    False
    >>> is_data_valid('6L:2,3:7')
    False
    >>> is_data_valid('7 : 2,3.5:7')
    False
    >>> is_data_valid('7.875:3.59,3.14:2,3:5')
    True'''
    
    for char in inputstr:
        if not char in '0123456789.:,-':
            return False
    return True
    
def can_be_number(str_to_test):
    '''str - > bool
    Returns a value indicating whether or not the inputed string value is equivalent to a valid number.
    >>> can_be_number('9')
    True
    >>> can_be_number('3.376')
    True
    >>> can_be_number('7..2')
    False
    >>> can_be_number('3^2')
    False
    >>> can_be_number('$5')
    False
    >>> can_be_number('-3.75')
    True
    >>> can_be_number('--4')
    False
    >>> can_be_number('4.7-5')
    False
    '''
    
    valid_chars = '0123456789.-'
    
    for char in str_to_test:
        if not char in valid_chars:
            return False
            
    num_of_decimal_pts = 0
    num_of_negatives = 0
    for char in str_to_test:
        if char == '.':
            num_of_decimal_pts += 1
        if char == '-':
            num_of_negatives += 1
    
    if num_of_decimal_pts > 1 or num_of_negatives > 1:
        return False
        
    index_of_neg_char = []
    index_of_neg = str_to_test.find('-')
    while index_of_neg != -1:
        index_of_neg_char.append(index_of_neg)
        index_of_neg = str_to_test.find('-', index_of_neg + 1)
        
    valid_neg_index = 0
    for index in index_of_neg_char:
        if index != 0:
            return False
            
    return True
    
def list_of_terms(inputstr):
    '''str -> list
    Takes a valid mathematical expression string and returns a list of terms--really a list of lists
    where each sublist contains the coefficient and power of each term or monomial in the polynomial.
    >>> list_of_terms('2:3,4:5,7:2,8:0')
    [['2', '3'], ['4', '5'], ['7', '2'], ['8', '0']]
    >>> list_of_terms('3.1415:3,2.718:7')
    [['3.1415', '3'], ['2.718', '7']]'''
    
    list_of_terms = inputstr.split(',')
    terms_2 = []
    
    for term in list_of_terms:
        t = term.split(':')
        terms_2.append(t)
        
    return terms_2
    
def exp_evaluate(list_of_terms, x_val):
    '''list -> dictionary
    Takes a list of lists where each sub-list represents the coefficient and power of a monomial making up a polynomial.
    Secondly, it evaluates the polynomial for the value specified of the independent variable.
    >>> exp_evaluate([[1, 1], [1, 0]], 1) == {'answer' : 2, 'x' : 1}
    True
    >>> exp_evaluate([[1, 2], [1, 1], [5, 0]], 2) == {'answer' : 11, 'x' : 2}
    True
    >>> exp_evaluate([[2, 3], [1, 1], [1, 0]], 0.5) == {'answer' : 1.75, 'x' : 0.5}
    True'''
    
    for term_str in list_of_terms:
        term_str[0] = float(term_str[0])
        term_str[1] = float(term_str[1])
    
    x_val = float(x_val)
    
    exp_value = 0
    result = {'answer':None, 'x':None}
    
    for term in list_of_terms:
        exp_value += term[0] * (x_val ** term[1])
        
    result['answer'] = exp_value
    result['x'] = x_val
    
    return result
    
#if __name__ == '__main__': # these lines are to test the module
#    import doctest
#    doctest.testmod()