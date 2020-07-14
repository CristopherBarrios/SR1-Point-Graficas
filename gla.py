#Cristopher jose Rodolfo Barrios Solis
#lab1

import struct
def char(c):
    return struct.pack('=c', c.encode('ascii'))

def word(c):
    return struct.pack('=h', c)

def dword(c):
    return struct.pack('=l', c)

def color(r, g, b):
    return bytes([b, g, r])

class Render(object):
    def __init__(self):
        self.winWidth = 0
        self.winHeight = 0
        self.viWidth = 0
        self.viHeight = 0
        self.color = color(255, 255, 255)
        self.xP = 0
        self.yP = 0
        self.framebuffer = []

    def glInit(self):
        return "Generando...\n"

    def glClear(self):
        self.framebuffer = [
            [color(0, 0, 0) for x in range(self.winWidth)]
            for y in range(self.winHeight)
        ]

    def glCreateWindow(self, width, height):
        self.winWidth = width
        self.winHeight = height
        self.framebuffer = [
            [color(0, 0, 0) for x in range(self.winWidth)]
            for y in range(self.winHeight)
        ]

    def glClearColor(self, r=0, g=0, b=0):
        self.framebuffer = [
            [color(r,g,b) for x in range(self.winWidth)]
            for y in range(self.winHeight)
        ]

    def glColor(self, r=0, g=0, b=0):
        self.color = color(r,g,b)

    def glViewPort(self, x, y, width, height):
        self.xP = x
        self.yP = y
        self.viWidth = width
        self.viHeight = height
        

    def glFinish(self, filename):
        f = open(filename, 'bw')
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.winWidth * self.winHeight * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        f.write(dword(40))
        f.write(dword(self.winWidth))
        f.write(dword(self.winHeight))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.winWidth * self.winHeight * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))


        for x in range(self.winWidth):
            for y in range(self.winHeight):
                f.write(self.framebuffer[y][x])
        f.close()

    def glVertex(self, x, y):
        newX = round((x + 1)*(self.viWidth/2)) + self.xP
        newY = round((y + 1)*(self.viHeight/2)) + self.yP
        self.framebuffer[newY][newX] = self.color

        

        def point(self, x, y):
            self.framebuffer[y][x] = color(255,0,0)


bitmap = Render()
print(bitmap.glInit())
bitmap.glCreateWindow(200,100)
bitmap.glViewPort(20,40,34,20)
bitmap.glClear()
bitmap.glVertex(0,0)
bitmap.glVertex(1,1)
bitmap.glVertex(-1,-1)
bitmap.glFinish('out.bmp')
