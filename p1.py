from PIL import Image



try:
    img = Image.open('input00.jpg')

except:
    print("file not found!")
    exit()

try:
    fhandle = open('2A2X.txt','w')

except:
    print("not able to open the file to store RGB values")
    exit()

rgb_pixels = list(img.getdata())



width,height = img.size
print("Image Properties -")
print("Height = ",height," Width = ",width)
print("Image Format = ",img.format)


fhandle.write(str(height)+' '+str(width)+"\n")

# print(rgb_pixels)
print("\n\nRGB Array - \n")
c = 0
readstring = ''

for tupl in rgb_pixels:
    for i in [ele for ele in tupl] :
        readstring += str(i)+','

        c = c + 1

        if(c %3 == 0):
            readstring = readstring[:-1]+" "

    if(c % 180 == 0 ):
        print(readstring[:])
        fhandle.write(readstring+"\n")
        readstring=''

# c denotes 1800 * 3 ,i.e, 1800 RGB Elements
#print(c)
fhandle.close()

