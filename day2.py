def get_checksum(rows):
    checksum = 0
    for row in rows:
        checksum += max(row) - min(row)
    return checksum


def get_evenly_divisible(row):
    sorted_row = sorted(row, reverse=True)
    for index, number in enumerate(sorted_row):
        for other_number in sorted_row[index + 1:]:
            if number % other_number == 0:
                # Exit early once found for the row.
                return (number, other_number)


def get_div_checksum(rows):
    checksum = 0
    for row in rows:
        a, b = get_evenly_divisible(row)
        checksum += a / b
    return checksum

if __name__ == '__main__':
    with open('day2-input.txt') as input_file:
        # read spreadsheet from input, convert to number
        rows = [
            [int(num) for num in row.strip().split('\t')]
            for row in input_file.readlines()
        ]
    # pt 1
    print(get_checksum(rows))
    # pt 2
    print(get_div_checksum(rows))
