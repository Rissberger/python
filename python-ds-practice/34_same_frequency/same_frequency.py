def same_frequency(num1, num2):
    def count_digits(num):
        counts = {}
        for digit in str(num):
            counts[digit] = counts.get(digit, 0) + 1
        return counts
    
    return count_digits(num1) == count_digits(num2)
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """