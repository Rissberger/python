def titleize(phrase):
    words = [word.capitalize() for word in phrase.split()]

    return ' '.join(words)
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
