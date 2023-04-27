def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    # Convert numbers to strings
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Create dictionaries to count the frequencies of digits in each number
    freq1 = {}
    freq2 = {}
    for digit in str_num1:
        freq1[digit] = freq1.get(digit, 0) + 1
    for digit in str_num2:
        freq2[digit] = freq2.get(digit, 0) + 1
    
    # Check if the frequencies of digits in the two numbers are the same
    return freq1 == freq2