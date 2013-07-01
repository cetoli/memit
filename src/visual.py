"""
############################################################
Memit - Visual
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2013/06/11  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.1 $
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2011, `GPL <http://is.gd/3Udt>`__.

Serious Game in cavalier projection for memetics.
"""
REPO = "/studio/%s"
Z_COUNT = 6
X_HAND0 = 10
X_HANDS = 600
Y_HAND0 = 590 - 6 * 70
Y_HAND1 = 210
Y_HANDS = 70

TRANS = "translate rotate scale skewX skewY matrix".split()

EVENT = ("onfocusin onfocusout onactivate onload onclick onkeydown onkeyup" + \
    " onmousedown onmouseup onmouseover onmousemove onmouseout").split()

class Visual:
    """ Builder creating SVG elements and placeholder groups. :ref:`visual`
    """
    def __init__(self,doc, gui, time):
        self.gui, self.time = gui, time
        self.doc = doc["panel"]
        self.phaser = lambda x = 0: None
        #self.build_hand(gui)
    def build_hand(self):
        def group(g, x, y, doc = self.doc):
            grp = self.gui.g(id = "h%d"%g, transform = "translate(%d %d)"%(x, y))
            doc <= grp
            return grp
        self.hands = [group(g, (g // Z_COUNT) * X_HANDS + X_HAND0,
            (g % Z_COUNT) * Y_HANDS + Y_HAND0 + Y_HAND1 * (g // Z_COUNT)) for g in range(9)]
        return self.hands
    def build_pieces(self):
        self.badges = [image(REPO%'memit/piece0%d_0%d.png'%(1, b),0, 0,
            70, 70, hand ) for b, hand in enumerate(self.hands)]
        return self.badges
    def build_cube(self,gui,bottom_image, rear_image, side_image):
        def image(href, x, y,width, height, doc = self.doc, style = {}, self= self):
            img = self.gui.image(href=href , x=x, y=y ,width=width,
                            height=height, style = style)
            doc <= img
            return img
        OFF =123
        SIDE = 300
        RDX = 30
        self.cube = self.gui.g(transform = "translate(550  150)")
        self.doc <= self.cube
        bottom = gui.image(href=REPO%bottom_image,
                    x=SIDE,y=-2*SIDE, width=SIDE,height=SIDE, rotate= 90)
        rear = gui.image(href=REPO%rear_image,
                    x=0,y=OFF, width=SIDE,height=SIDE, skewX=45, scale=(1,0.71))
        left = gui.image(href=REPO%side_image,
                    x=OFF,y=0, width=SIDE,height=SIDE, skewY=45, scale=(0.71,1))
        self.parts = [bottom, rear, left]
    def build_base(self):
        OFF =170
        SIDE = 99
        RDX = 30
        def image(href, x, y,width, height, doc = self.doc, style = {}, self= self):
            img = self.gui.image(href=href , x=x, y=y ,width=width,
                            height=height, style = style)
            doc <= img
            return img
        def text(txt, x, y, font_size=22,text_anchor="middle",style = {}):
            tex= self.gui.text(txt , x=x, y=y ,font_size=font_size,
                            text_anchor=text_anchor, style = style)
            self.doc <= tex
            return tex
        def voxel( i, j ,k , doc = self.doc, fill = "red"):
            x, y = OFF+k*100+71*i,  OFF+j*100+71*i
            rec = self.gui.rect(x =0, y = 0,
            width=SIDE-(2-i)*RDX, height=SIDE-(2-i)*RDX,
            style=dict(fill=fill, fillOpacity= 0.2))
            vox = self.gui.g( transform = "translate(%d %d)"%(x, y))
            doc <= vox
            vox <= rec
            return vox
        gui= self.gui
        KINDS = [0,1]#[0]*2+[1]*5
        self.back = self.gui.g()
        self.avatar = image(href=REPO%'memit/background_base.png', x= 0, y = 0,
            width=800, height=600, style=dict(opacity= 1))
        self.pump = image(href=REPO%'memit/bomba.png', x= 390, y = 5,
            width=400, height=112, style=dict(opacity= 1))
        self.drops = [image(REPO%'memit/gota.png',750, 50 + 100*i,
            40, 52) for i in range(6)]
        self.bpuzzle = self.gui.g(transform = "translate(550  150)")
        puzzle = image(href=REPO%'memit/puzzle00_00.png', x= 550, y = 150,
            width=200, height=100 )
        self.puzzle = self.gui.g(transform = "translate(550  150)")
        self.doc <= self.puzzle
        self.puzzles = [image(REPO%('memit/puzzle_0%d.png'%p),0, 0 , 200, 100,
            self.back) for p in range(9)]
        self.puzzle <= self.puzzles[0]
        self.digits = [
            text('0', 425 +50*i, 65, 48, 'middle', {'fill': 'white'})
            for i in range(4)]
        self.value =0
        self.inc =1
        #time.set_interval(self.tick,100)
        self.time.set_interval(self._tick,100)
        return self.bpuzzle, self.puzzles, self.puzzle
    def set_inc_value(self,value, inc=1):
        self.value, self.inc = value, inc
    def build_board(self):
        CLS='red green blue'.split()
        Z2TW, TW2Z = [0, 1, 2], [2, 1, 0]
        return [voxel(i, j, k, self.doc, CLS[i]) 
                       for i in TW2Z for j in Z2TW for k in Z2TW]
    def build_house(self):
        house = self.gui.g(transform = "translate(10  10)")
        self.doc <= house
        return house
        
    def _tick(self):
        """Time tick updates pump display value and makes the drops fall"""
        value = self.value //10
        for i, drop in enumerate(self.drops):
            y = 50 + (i * (-800 + 900* self.inc) + (10 * self.value) % 100) % 500
            drop.setAttribute('y' , y)
        #print ('tick', value, value %10, value //10)
        for i in range(4)[::-1]:
            self.digits[i].text = str(value % 10)
            value //= 10
        self.value += self.inc
        if self.value > 10:
            self.phaser(self.value)
