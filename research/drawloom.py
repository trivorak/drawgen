import binascii
from PIL import Image, ImageDraw

scaleSize = 10

# Open Binary Files
with open("../Halliburton - Plant 2054-Pro-CNCR.pdf", mode="rb") as f:
    a = f.read()
    ab = binascii.hexlify(a)
    abc = str(ab, 'utf-8')

# Create blank List
aList = []
aListInt = []
aWorkingList = []

# Split by every 2 characters and append to "blank list"
for i in range(0, len(abc), 2):
    aList.append(abc[i:i + 2])

# Convert elements to int from Hex
for element in aList:
    aListInt.append(int(element, 16))

# Make the list an even amount of elements
for i in range(0, 2 - len(aListInt) % 2):
    aListInt.append(0)

# Multiply values by Scale size and round
for element in aListInt:
    aWorkingList.append(round(element * scaleSize, 0))

# Not sure what the hell I was doing here
aListInt = aWorkingList

im = Image.new("RGB", (255 * scaleSize, 255 * scaleSize), (255, 255, 255))

draw = ImageDraw.Draw(im)

draw.polygon(xy=aListInt, outline=(0, 0, 0))

im.show()
