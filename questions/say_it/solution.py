def say_it(n: int) -> int:
    current_string = '1'
    for i in range (1, n):
        result_string = ''
        current_char = current_string[0]
        counter = 0

        for char in current_string:
            if char != current_char: 
                result_string += '{}{}'.format(counter, current_char)
                current_char = char
                counter = 1

            else:
                counter += 1

        current_string = result_string + '{}{}'.format(counter, current_char)

    return int(current_string)