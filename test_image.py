import Image
import os

def test1():
    size=(1024,1024)

    f=Image.new("RGB",size,(100,200,210))

    color=(0,0,0)

    for x in xrange(0,size[0]):
        for y in xrange(0,size[1]):
            color=(int((255.0/size[0])*x),int((255.0/size[1])*y),int((255.0/size[1])*y))
            #print color
            f.putpixel((x,y),color)


    f.save("fengxs.bmp","BMP")
    print (f.mode)
    print size[0]*size[1]

def test2():
    for s in os.walk("."):
        for ss in s[2]:
            p = s[0]+"/"+ss
            print os.path.isfile(p)
            

test2()
