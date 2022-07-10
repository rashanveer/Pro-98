def counter():
    fileName = "Saying.txt"
    num = 0
    file = open(fileName)
    f = file.readlines()
    for line in f:
        num = num+len(line)
    print(num)  

counter()      