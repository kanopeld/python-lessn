def main():
    file = open("files/file.txt")
    lines = []
    while True:
        line = file.readline()
        if not line:
            break
        lines.append(line)

    print(file)
    file.close()
    # print(lines[0])
    # print(lines[-1])
    # print(lines[:2])
    # print(lines[:])

    file = open("files/file.txt")
    # print(file.readlines())
    file.close()

    with open('files/file.txt') as my_file:
        for line in my_file.readlines():
            print(line)

    with open('files/file.txt', 'a') as my_file:
        my_file.writelines(['line1', 'line2'])

if __name__ == '__main__':
    main()
