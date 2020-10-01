#Diamond assignment -> make diamond with "*" and " ", changing the width, height = (2 * width - 1)
#Make inverse triangle from given height
TRIANGLE_HEIGHT = 5

for i in range(TRIANGLE_HEIGHT):
    print("*" * (i + 1))

for i in range(TRIANGLE_HEIGHT):
    print(" " * (TRIANGLE_HEIGHT - 1 - i) + "*" * (i + 1))

#height di sini maksudnya cmn 1/2 tinggi fullnya sampe ke tengah
def diamonding(height):
    middle = (2 * height - 1)
    for i in len(range(height)):
        print(" " * (height - 1 - i) + "*" * () + " " * (height - 1 - i))