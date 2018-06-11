try:
    fhandle = open('input00.txt')

except:
    print("file cannot be opened")
    exit()


count = 0

for line in fhandle:
    line = line.strip()
    # print(len(line))

    words = line.split()
    count += len(words)

    # print(len(words))

# You will get 2 more than the length of the RGB Array here
# This is because the file has height and width as a list in the first line
# The second line is empty and the RGB values begin after that

print(count)
