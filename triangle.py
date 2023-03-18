FACTOR = 20
HEIGHT = FACTOR
WIDTH =  FACTOR * 2

PIXELS = []


def init():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            PIXELS.append(".")

def barycentric(x1, y1, x2, y2, x3, y3, xc, yc):
    det = ((x1 - x3)*(y2 - y3)) - (x2 - x3)*(y1 -y3)
    u1 = ((y2 - y3)*(xc - x3) + (x3 - x2)*(yc - y3))
    u2 = ((y3 - y1)*(xc - x3) + (x1 - x3)*(yc - y3))
    u3 = det - u1 - u2

    return det, u1, u2, u3

def dispaly():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(PIXELS[y*WIDTH + x], end="")
        print()

def main():
    init()

    x1, y1 = WIDTH//2, 0
    x2, y2 = 0, HEIGHT - 1
    x3, y3 = WIDTH - 1, HEIGHT - 1

#    PIXELS[y1*WIDTH + x1] = "$"
#    PIXELS[y2*WIDTH + x2] = "$"
#    PIXELS[y3*WIDTH + x3] = "$"

    for y in range(HEIGHT):
        for x in range(WIDTH):
            det, u1, u2, u3 = barycentric(x1, y1, x2, y2, x3, y3, x, y)
            if (u1/det >= 0 and u2/det >= 0 and u3/det >= 0):
                PIXELS[y*WIDTH + x] = "$"

    dispaly()


if __name__ == "__main__":
    main()
