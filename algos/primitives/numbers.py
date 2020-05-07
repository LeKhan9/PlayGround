def is_num_palindromic(num):
    '''
        Given a number, returns a bool representing if the number is "palindromic"
            - Pointedly —> the sequence of digits in the forward direction is the same as
                           the sequence of digits in the backwards direction
    '''
    
    BASE_SYSTEM = 10

    start_num = num
    reversed_num = 0

    while num > 0:

        # tease out last digit
        last_digit = num % BASE_SYSTEM

        # add it as least significant digit in running reversed number
        reversed_num = BASE_SYSTEM * reversed_num + last_digit

        # remove last digit from input number
        num //= BASE_SYSTEM

    return start_num == reversed_num
