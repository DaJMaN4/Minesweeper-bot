from PIL import ImageGrab
import time
import mouse
import keyboard
import random

path = "C:\\Users\\damwid001\\PycharmProjects\\pythonMine\\venv\\Photos\\image.jpg"
grid = {}
numbers = {}
realNumbers = {}
numbersAndBlock = {}
allBlocksAround = {}
z = []
bombs = []
unknows = []
clicked = []
maybeBomb = []
listOfBlocks = []
blocksAround = []
numbersOfBlocksAround = []
x_start = 5922
y_start = 4634 
facePixelxlose = 105
facePixelylose = 3288 
facePixelxwin = 10958
facePixelywin = 3577
number = 0
bombsAround = 0
x = x_start
y = y_start
clickMore = False
blockFound = False
clickRight = False
clickedOnBomb = False
endFunctionBool = False
print("Running...")


def click(dy , dx, clickRight):
    mouse.move(392 + ((dx - 1) * 24), 311 + ((dy - 1) * 24)) # originaly 392 and 311
    if clickRight:
        mouse.click('right')
        time.sleep(0.1)
    mouse.click('left')


def clicking():
    xc = x_start
    yc = y_start
    def click():
        mouse.move(xc - 200, yc - 150)
        mouse.click('right')
    for v in range(16):
        for i in range(30):
            click()
            xc += 24
        xc = x_start
        yc += 24


def mapping():
    global x, y, grid
    number = 0
    for v in range(16):
        for i in range(30):
            number += 1
            pixels = screenshot.getpixel((x, y))

            if pixels[0] == 198 and pixels[0] == 198 and pixels[0] == 198: # none number/block
                grid[number] = [v + 1, i + 1, 10]

            if pixels[0] == 0 and pixels[0] == 0 and pixels[0] == 0: # a block
                grid[number] = [v + 1, i + 1, 20]

            if pixels[2] == 255:  # number 1
                grid[number] = [v + 1, i + 1, 1]

            if pixels[1] == 128: # number 2
                grid[number] = [v + 1, i + 1, 2]

            if pixels[0] == 255: # number 3
                grid[number] = [v + 1, i + 1, 3]

            if pixels[2] == 128: # number 4
                grid[number] = [v + 1, i + 1, 4]

            if pixels[0] == 128: # number 5
                grid[number] = [v + 1, i + 1, 5]

            if pixels[1] == 128 and pixels[2] == 128: # number 6
                grid[number] = [v + 1, i + 1, 6]

             #seven is black

            try:
                if grid[number] != numbersAndBlock[number]:
                    numbersAndBlock.pop(number)
            except:
                pass


            x += 36
        x = x_start
        y += 36
    x = x_start
    y = y_start


def loss():
    facePixels = screenshot.getpixel((facePixelxlose, facePixelylose))
    if facePixels[0] == 0:
        return True


def win():
    facePixels = screenshot.getpixel((facePixelxwin, facePixelywin))
    if facePixels[0] == 0:
        return True


def reset():
    mouse.move(392 + (15 * 23), 311 + (-2 * 23))
    mouse.click('left')
    time.sleep(0.1)
    clicking()
    time.sleep(0.5)
    grid.clear()
    numbers.clear()
    realNumbers.clear()
    z.clear()
    bombs.clear()
    maybeBomb.clear()
    clicked.clear()
    listOfBlocks.clear()
    numbersOfBlocksAround.clear()
    blockFound = False
    clickRight = False
    runClicks = False
    clickMore = False
    clickedOnBomb = False


def mapGrid(grid):
    for key in grid:
        numbers[key] = grid.get(key)[2]


def makeLists(key):
    global grid
    if key > 450:
        numbersOfBlocksAround = [key - 29, key - 30, key - 31,
                                 key - 1,            key + 1]

        listOfBlocks = [numbers.get(key - 29), numbers.get(key - 30), numbers.get(key - 31),
                        numbers.get(key - 1),                         numbers.get(key + 1)]
    elif key <= 30:
        numbersOfBlocksAround = [
                                 key - 1,            key + 1,
                                 key + 29, key + 30, key + 31]
        listOfBlocks = [
                        numbers.get(key - 1),                         numbers.get(key + 1),
                        numbers.get(key + 29), numbers.get(key + 30), numbers.get(key + 31)]
    elif grid.get(key)[1] == 1:
        numbersOfBlocksAround = [key - 30, key - 29,
                                           key + 1,
                                 key + 30, key + 31]

        listOfBlocks = [numbers.get(key - 30), numbers.get(key - 29),
                                               numbers.get(key + 1),
                        numbers.get(key + 30), numbers.get(key + 31)]
    elif grid.get(key)[1] == 30:
        numbersOfBlocksAround = [key - 31, key - 30,
                                 key - 1,
                                 key + 29, key + 30]

        listOfBlocks = [numbers.get(key - 31), numbers.get(key - 30),
                        numbers.get(key - 1),
                        numbers.get(key + 29), numbers.get(key + 30)]
    else:
        numbersOfBlocksAround = [key - 29, key - 30, key - 31,
                                 key - 1,            key + 1,
                                 key + 29, key + 30, key + 31]

        listOfBlocks = [numbers.get(key - 29), numbers.get(key - 30), numbers.get(key - 31),
                        numbers.get(key - 1),                         numbers.get(key + 1),
                        numbers.get(key + 29), numbers.get(key + 30), numbers.get(key + 31)]

    return listOfBlocks, numbersOfBlocksAround


def findBombsAround():
    for key in numbers:
        if numbers.get(key) != 10 and numbers.get(key) != 20:

            listOfBlocks, numbersOfBlocksAround = makeLists(key)

            realNumbers[key] = numbers.get(key)
            if numbers.get(key) == listOfBlocks.count(20):
                listnumbers = 0
                while listnumbers != len(listOfBlocks):

                    if listOfBlocks[listnumbers] == 20:
                        if not bombs.__contains__(numbersOfBlocksAround[listnumbers]):
                            bombs.append(numbersOfBlocksAround[listnumbers])
                            #print(bombs, "bob", listOfBlocks, numbersOfBlocksAround)

                    listnumbers += 1
                        #print("done", grid.get(key)[0], grid.get(key)[1], key, listOfBlocks, realNumbers)


def clickOnBlocks():
    clickMore = True
    for key in realNumbers:

        listOfBlocks, numbersOfBlocksAround = makeLists(key)
        bombsAround = 0

        for m in numbersOfBlocksAround:
            if m in bombs:
                bombsAround += 1
                if m in blocksAround:
                    blocksAround.remove(m)


        if bombsAround == realNumbers.get(key) and listOfBlocks.__contains__(20):
            for h in numbersOfBlocksAround:
                if h not in bombs and numbers.get(h) == 20:
                    if (keyboard.is_pressed('q')):
                        break
                    if h not in clicked:
                        click(grid.get(h)[0] , grid.get(h)[1] , True)
                        clicked.append(h)
                        clickMore = False
                        #print(grid.get(h)[0] , grid.get(h)[1], numbersOfBlocksAround, key)


    if clickMore:
        if endFunction():
            while clickMore:
                r = random.randint(1, 480)
                if r not in bombs and numbers.get(r) == 20:
                    click(grid.get(r)[0], grid.get(r)[1], True)
                    time.sleep(0.1)
                    clickMore = False
                    time.sleep(0.5)



time.sleep(5)
clicking()

while True:
    print("new line")
    if (keyboard.is_pressed('q')):
        print("quit has been pressed")
        break
    if (keyboard.is_pressed('e')):
        clicking()
    screenshot = ImageGrab.grab()
    if loss():
        reset()
        screenshot = ImageGrab.grab()
        print("I lost D:")
    elif win():
        print("I won :D")
        break
    mapping()
    mapGrid(grid)
    endFunction()
    findBombsAround()
    clickOnBlocks()

