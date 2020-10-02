#height di sini maksudnya cmn 1/2 tinggi fullnya sampe ke tengah
def diamond(height):
    for i in range(height):
        print(" " * (height - 1 - i) + "*" * (i * 2 + 1))   #Use + 1 because index only counts until height-1
    for i in range(height - 2, -1, -1):
        print(" " * (height - 1 - i) + "*" * (i * 2 + 1))

diamond(eval(input("Type the height you want: ")))