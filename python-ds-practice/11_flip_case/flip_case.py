def flip_case(phrase, to_swap):
    results = ""

    for char in phrase:
        if char.lower() == to_swap.lower():
            char = char.swapcase()
        results += char
    return results
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
