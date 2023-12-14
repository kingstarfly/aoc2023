def main():
    spelled_out_numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    with open("1-2-data.txt", "r") as f:
        lines = f.readlines()

        total = 0

        for line in lines:
            value = 0

            # find word or number from start of line
            chars = ""

            for char in line:
                chars += char

                for spelled_out_number in spelled_out_numbers:
                    if chars.endswith(spelled_out_number):
                        value += 10 * spelled_out_numbers[spelled_out_number]
                        break

                if value > 0:
                    break

                if char.isnumeric():
                    value += 10 * int(char)
                    break

            # find word or number that occurs at end of the line
            chars = ""
            for i in range(len(line) - 1, -1, -1):
                char = line[i]
                chars = char + chars

                found_ending_number = False

                for spelled_out_number in spelled_out_numbers:
                    if chars.startswith(spelled_out_number):
                        value += spelled_out_numbers[spelled_out_number]
                        found_ending_number = True
                        break

                if found_ending_number:
                    break

                if char.isnumeric():
                    value += int(char)
                    break

            print(value)
            total += value

        return total


if __name__ == "__main__":
    print(main())
