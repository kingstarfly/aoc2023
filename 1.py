def main():
    with open("1-data.txt", "r") as f:
        lines = f.readlines()

        total = 0

        for line in lines:
            value = 0
            for char in line:
                if char.isnumeric():
                    value += 10 * int(char)
                    break
            for i in range(len(line) - 1, -1, -1):
                char = line[i]
                if char.isnumeric():
                    value += int(char)
                    break
            total += value

        return total


if __name__ == "__main__":
    print(main())
