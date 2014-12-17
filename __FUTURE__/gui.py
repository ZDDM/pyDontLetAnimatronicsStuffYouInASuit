import pyglet, os, sys, time
from pyglet.gl import *
from pyglet.image.codecs.png import PNGImageDecoder

def init():
    global images, window
    platform = pyglet.window.get_platform()
    display = platform.get_default_display()
    screen = display.get_default_screen()
    template = pyglet.gl.Config(alpha_size=8)
    config = screen.get_best_config(template)
    context = config.create_context(None)
    
    window = pyglet.window.Window(caption="-pyDLASYIAS-", width=1600, height=720, context=context)
    window.push_handlers(pyglet.window.event.WindowEventLogger())

    pyglet.resource.path = ['images', 'sounds']
    pyglet.resource.reindex()
    
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    window.set_visible()

    #images
    securityofficenimg = pyglet.image.load(os.path.join("images", "sec.png"), decoder=PNGImageDecoder())

    leftbuttonimg = pyglet.image.load(os.path.join("images", "lb.png"), decoder=PNGImageDecoder())
    leftbuttonimgdoorclosed = pyglet.image.load(os.path.join("images", "lbdc.png"), decoder=PNGImageDecoder())
    leftbuttonimgbothclosed = pyglet.image.load(os.path.join("images", "lbb.png"), decoder=PNGImageDecoder())
    leftbuttonimglight = pyglet.image.load(os.path.join("images", "lbl.png"), decoder=PNGImageDecoder())

    rightbuttonimg = pyglet.image.load(os.path.join("images", "rb.png"), decoder=PNGImageDecoder())
    rightbuttonimgdoorclosed = pyglet.image.load(os.path.join("images", "rbdc.png"), decoder=PNGImageDecoder())
    rightbuttonimgbothclosed = pyglet.image.load(os.path.join("images", "rbb.png"), decoder=PNGImageDecoder())
    rightbuttonimglight = pyglet.image.load(os.path.join("images", "rbl.png"), decoder=PNGImageDecoder())

    cambuttonimg = pyglet.image.load(os.path.join("images", "cambutton.png"), decoder=PNGImageDecoder())
    honk = pyglet.resource.media(os.path.join("sounds", "freddyhonk.wav"), streaming=False)
    
    background = pyglet.sprite.Sprite(securityofficenimg, 0, 0)
    leftbutton = pyglet.sprite.Sprite(leftbuttonimg, 1, 180)
    rightbutton = pyglet.sprite.Sprite(rightbuttonimg, 1475, 180)
    cambutton = pyglet.sprite.Sprite(cambuttonimg, 500, 40)
    


    
    
    
    imagelist = [background, leftbutton, cambutton, rightbutton]

    @window.event
    def on_draw():
        window.clear()
        for image in imagelist:
            image.draw()

    @window.event
    def on_mouse_press(x=range(0, 1600), y=range(0, 720), button='LEFT', modifiers=None):
        global leftdoor
        if x in range(32, 70) and y in range(332, 374):
            print "TBC WITH PYDLASYIAS' LEFT DOOR FUNCT. (%s, %s)" %(x,y)

        if x in range(31, 69) and y in range(246, 294):
            print "TBC WITH PYDLASYIAS' LEFT LIGHT FUNCT. (%s, %s)" %(x,y)

        if x in range(504, 1100) and y in range(50, 90):
            print "TBC WITH CAMERA!!! (%s, %s)" %(x,y)

        if x in range(1498, 1534) and y in range(324, 374):
            print "TBC WITH PYDLASYIAS' RIGHT DOOR FUNCT. (%s, %s)" %(x,y)

        if x in range(1499, 1536) and y in range(243, 295):
            print "TBC WITH PYDLASYIAS' RIGHT LIGHT FUNCT. (%s, %s)" %(x,y)

        if x in range(675, 682) and y in range(480, 485):
            print "Honk! (%s, %s)" % (x,y)
            honk.play()
            

        
                

    @window.event
    def on_close():
        sys.exit(0)
        os._exit(0)
        pyglet.exit(0)

    pyglet.app.run()

init()   
