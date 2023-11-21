def number_compare(a, b):
    if a == b:
        print('Numbers are equal')
    elif a > b:
        print('First number is greater than second one')
    else: 
        print('Second number is greater than first one')
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """