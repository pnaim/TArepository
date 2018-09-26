stack = []
topStack = []
middleStack = []
bottomStack = []
item = input("Enter your items: ").split()

def put():
    x = 0
    y = 1
    while x <= len(item):
        if len(topStack) < 5:
            topStack.append(item[x:y])
            print(topStack)
        elif len(middleStack) < 5:
            middleStack.append(item[x:y])
            print(middleStack)
        elif len(bottomStack) < 5:
            bottomStack.append(item[x:y])
            print(bottomStack)
        x += 1
        y += 1
    return

def take():
    x = 0
    while x <= len(item):
        if len(bottomStack) > 0:
            bottomStack.pop()
            print(bottomStack)
        elif len(middleStack) > 0:
            middleStack.pop()
            print(middleStack)
        elif len(topStack) > 0:
            topStack.pop()
            print(topStack)
        else:
            print("empty")
        x += 1
    return

put()
take()
