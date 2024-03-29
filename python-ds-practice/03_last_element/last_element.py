def last_element(lst):
    if lst:
        return lst[-1]
    else:
        raise ValueError("List is empty")
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """