def task(captcha, next_digit):
    total = 0
    for index, number in enumerate(captcha):
        next_number = captcha[(index + next_digit) % len(captcha)]
        if number == next_number:
            total += int(number)
    return total

if __name__ == '__main__':
    with open('day1-input.txt') as input_file:
        captcha = input_file.readline().strip()

    # pt 1
    print(task(captcha, 1))

    # pt 2
    print(task(captcha, len(captcha) / 2))
