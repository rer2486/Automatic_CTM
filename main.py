import cv2 as cv


def draw_outline(name, corner1, corner2, corner3, corner4, side1, side2, side3, side4):
    image = texture.copy()
    if corner1:
        for width in range(OutlineLength):
            for length in range(OutlineLength):
                image[width][length] = outline[width][length]
    if corner2:
        for length in range(len(texture) - OutlineLength, len(texture)):
            for width in range(OutlineLength):
                image[width][length] = outline[width][length]
    if corner3:
        for width in range(len(texture) - OutlineLength, len(texture)):
            for length in range(OutlineLength):
                image[width][length] = outline[width][length]
    if corner4:
        for width in range(len(texture) - OutlineLength, len(texture)):
            for length in range(len(texture) - OutlineLength, len(texture)):
                image[width][length] = outline[width][length]
    if side1:
        for length in range(OutlineLength, len(texture) - OutlineLength):
            for width in range(OutlineLength):
                image[width][length] = outline[width][length]
    if side2:
        for length in range(OutlineLength):
            for width in range(OutlineLength, len(texture) - OutlineLength):
                image[width][length] = outline[width][length]
    if side3:
        for width in range(OutlineLength - len(texture), len(texture)):
            for length in range(len(texture) - OutlineLength, len(texture)):
                image[width][length] = outline[width][length]
    if side4:
        for length in range(OutlineLength, len(texture) - OutlineLength):
            for width in range(len(texture) - OutlineLength, len(texture)):
                image[width][length] = outline[width][length]
    cv.imwrite(str(name) + ".png", image)


texture = cv.imread('texture.png')
outline = cv.imread('outline.png')
while True:
    try:
        OutlineLength = int(input('Outline length: '))
        break
    except ValueError:
        print("Please enter an integer!")
if len(texture) == len(texture[0]) and len(texture) == len(outline) and len(outline) == len(outline[0]):
    draw_outline(0, True, True, True, True, True, True, True, True)
    draw_outline(1, True, True, True, True, True, True, False, True)
    draw_outline(2, True, True, True, True, True, False, False, True)
    draw_outline(3, True, True, True, True, True, False, True, True)
    draw_outline(4, True, True, True, True, True, True, False, False)
    draw_outline(5, True, True, True, True, True, False, True, False)
    draw_outline(6, True, True, True, True, False, True, False, False)
    draw_outline(7, True, True, True, True, True, False, False, False)
    draw_outline(8, True, False, True, True, False, False, False, False)
    draw_outline(9, True, True, True, False, False, False, False, False)
    draw_outline(10, True, True, False, True, False, False, False, False)
    draw_outline(11, False, False, True, True, False, False, False, False)
    draw_outline(12, True, True, True, True, True, True, True, False)
    draw_outline(13, True, True, True, False, True, True, False, False)
    draw_outline(14, True, True, False, False, True, False, False, False)
    draw_outline(15, True, True, False, True, True, False, True, False)
    draw_outline(16, True, True, True, True, False, True, False, True)
    draw_outline(17, True, True, True, True, False, False, True, True)
    draw_outline(18, True, True, True, True, False, False, False, True)
    draw_outline(19, True, True, True, True, False, False, True, False)
    draw_outline(20, False, True, True, True, False, False, False, False)
    draw_outline(21, True, True, False, True, False, False, False, False)
    draw_outline(22, True, True, False, False, False, False, False, False)
    draw_outline(23, True, False, True, False, False, False, False, False)
    draw_outline(24, True, True, True, True, False, True, True, False)
    draw_outline(25, True, False, True, False, False, True, False, False)
    draw_outline(26, False, False, False, False, False, False, False, False)
    draw_outline(27, False, True, False, True, False, False, True, False)
    draw_outline(28, True, True, True, False, False, True, False, False)
    draw_outline(29, True, True, False, True, True, False, False, False)
    draw_outline(30, True, False, True, True, False, True, False, False)
    draw_outline(31, True, True, True, False, True, False, False, False)
    draw_outline(32, False, False, False, True, False, False, False, False)
    draw_outline(33, False, False, True, False, False, False, False, False)
    draw_outline(34, True, False, False, True, False, False, False, False)
    draw_outline(35, False, True, True, False, False, False, False, False)
    draw_outline(36, True, True, True, True, False, True, True, True)
    draw_outline(37, True, False, True, True, False, True, False, True)
    draw_outline(38, False, False, True, True, False, False, False, True)
    draw_outline(39, False, True, True, True, False, False, True, True)
    draw_outline(40, True, False, True, True, False, False, False, True)
    draw_outline(41, False, True, True, True, False, False, True, False)
    draw_outline(42, False, True, True, True, False, False, False, True)
    draw_outline(43, True, True, False, True, False, False, True, False)
    draw_outline(44, False, True, False, False, False, False, False, False)
    draw_outline(45, True, False, False, False, False, False, False, False)
    draw_outline(46, True, True, True, True, False, False, False, False)
    input("Textures succesefully created, Press ENTER to leave.")
else:
    print('Texture/Outline Is not a square or outline image size is not equal to texture image size.\nPress ENTER to '
          'leave')
    input()
