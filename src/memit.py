"""
############################################################
Memit - All
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2013/03/17  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.1 $
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2011, `GPL <http://is.gd/3Udt>`__.

Serious Game in cavalier projection for memetics.

"""
__author__  = "Carlo E. T. Oliveira (carlo@nce.ufrj.br) $Author: carlo $"
__version__ = "0.2 $Revision$"[10:-1]
__date__    = "2013/03/17 $Date$"

REPO = '/studio/memit/%s'

def _logger(*a):
    print(a)
        

if not '__package__' in dir():
    import svg
    from html import TEXTAREA
    logger = log
    pass
else:
    logger = _logger
    pass

def noop(nop=''):
    pass
HANDLER = {"_NOOP_":'noop()'}
VKHANDLER = dict([(k,noop) for k in range(32,40)])

def uuid():
    r = jsptrand()
    return '%i'%(JSObject(jsptdate).getTime()*1000+r)

def jshandler(event):
    code = event.keyCode
    if code in VKHANDLER:
        VKHANDLER[code]()
    #alert(event.keyCode)
if not '__package__' in dir():
    doc.onkeypress=jshandler

def eventify(owner):
    #alert('owner :'+owner)
    HANDLER[owner]()
    
TRANS = "translate rotate scale skewX skewY matrix".split()

EVENT = ("onfocusin onfocusout onactivate onload onclick onkeydown onkeyup" + \
    " onmousedown onmouseup onmouseover onmousemove onmouseout").split()


class Dialog:
    """ Floating panel holding an editable text area. :ref:`dialog`
    """
    def __init__(self, gui, img = REPO%'paje.png',  text = '', act = lambda x:None):
        self._rect=gui.rect(0,100, 800, 440, style= {
            'fillOpacity':'0.7', 'fill':'black'})
        self._area=gui.textarea(text,80,130, 700, 400)
        self._imag=gui.image(img,2,80, 32, 32)
        self._imag.addEventListener('click', self.action)
        self.act= act
    def hide(self):
        self._rect.style.visibility = 'hidden'
        self._area.style.visibility = 'hidden'
        self._imag.style.visibility = 'hidden'
        #self._area.setVisible(self._area,False)
    def show(self):
        self._rect.style.visibility = 'visible'
        self._area.style.visibility = 'visible'
        self._imag.style.visibility = 'visible'
        #self._area.setVisible(self._area,True)
    def get_text(self):
        return self._area.value
    def set_text(self, text):
        self._area.value = text
    def action(self, event):
        self.hide()
        self.act(self)

 
class GUI:
    """ Factory creating SVG elements, unpacking extra arguments. :ref:`gui`
    """
    def __init__(self,panel,data):
        self.args = {}
        self.panel = self._panel = panel
        self.data = data
        for child in panel: # iteration on child nodes
                panel.remove(child)
        
    def get_args(self):
        args = self.args
        for key, value in self.args.items():
            args[key]= 'eventify(\\"%s\\")'%value
        self.args = {}
        p='"'
        if len(args) != 0:
            args = ', '+','.join(['%s = %s%s%s'%(k,p,v,p)
                                     for k, v in args.items()])
        else:
            args = ''
        return args
    def _get_kwargs(self,kw):
        trans =' '.join(
            [key + ['(%s)','%s'][isinstance(value, tuple)]%str(value)
             for key, value in kw.items() if key in TRANS])
        return trans and ', transform="%s"'%trans or ''
            
    def request(self, url = '/rest/studio/jeppeto?type=2', action = None, data=''):
        req = ajax()
        req.on_complete = action
        req.set_timeout(8,self._err_msg)
        req.open('GET',url,True)
        req.set_header("Content-Type","text/plain; charset=utf-8")
        req.send()
        pass

    def _err_msg(self, url = None, data = '', action = None, error = None):
        pass

    def textarea(self,text,x,y,w,h,style= {}):
        def dpx(d):
            return '%spx'%d
        attrs = dict (position = 'absolute', top=dpx(y), left=dpx(x) ,
            width=dpx(w) , height=dpx(h), color = 'navajowhite', border= 1,
            resize = 'none', background = 'transparent')
        attrs['top']= y
        attrs = {'position' : 'absolute', 'top':dpx(y), 'left':dpx(x),
            'width':dpx(w) , 'height':dpx(h), 'resize' : 'none','borderColor': 'darkslategrey',
            'color': 'navajowhite', 'border': 1, 'background' : 'transparent' }
        #t = TEXTAREA(text, style = {'position' : 'absolute', 'top':'100px', 'left':'40px'})#attrs)
        t = TEXTAREA(text, style = attrs)
        #d_rect=gui.rect(10,100, 540, 240, style= {'fill-opacity':'0.2', 'fill':'black'})
        self.data <= t
        return t
    
    def dialog(self, text, img = REPO%'paje.png', act = lambda x:None):
        t = Dialog(self,text=text, img=img, act=act)
        #t.setStyleAttribute('border',0)
        return t
    def set(self, element):
        self.panel = element
    def clear(self):
        self.panel = self._panel
    def remove(self, element):
        self.panel.removeChild(element)

    def text(self, text,x=150,y=25, font_size=22,text_anchor="middle",
      style= {}):
      element = svg.text(text,x=x,y=y,
      font_size=font_size,text_anchor=text_anchor,
      style=style)
      self.panel <= element
      return element
  
    def group(self, group= None, layer=0):
        element = group or svg.g()
        self.panel <= element
        layer and self.set(element) or self.clear()
        return element

    def path(self, d,style={}, onMouseOver="noop",  onMouseOut="noop"):
        exec('element = svg.path(d=%s,style=%s%s)'%(
            str(d),str(style),self.get_args()))
        self.panel <= element
        return element
  
    def image(self,  href, x=0, y=0, width=100, height=50, **kw):
        exec('element = svg.image(href="%s", x=%i, y=%i, width=%i, height=%i%s)'%(
            href, x, y, width, height,self._get_kwargs(kw)))
        self.panel <= element
        return element
  
    def ellipse(self,  href, cx=0, cy=0, rx=100, ry=50, style= {}, **kw):
        exec('element = svg.ellipse(cx=%i, cy=%i, rx=%i, ry=%i,style=%s%s)'%(
            cx, cy, rx, ry,str(style),self.get_args()))
        self.panel <= element
        return element
  
    def rect(self, x=0, y=0, width=100, height=50,style={}):
        exec('element = svg.rect(x=%i, y=%i, width=%i, height=%i,style=%s%s)'%(
            x, y, width, height,str(style),self.get_args()))
        self.panel <= element
        return element
    
    def handler(self, key, handle):
        VKHANDLER[key] = handle
    def avatar(self):
        return Avatar(self)
    
    def _decorate(self, handler, **kw):
      self.args = {} #kw #dict(kw)
      #alert(' '.join([k for k,v in kw.items()]))
      for key, value in kw.items():
          handler_id = uuid()
          HANDLER[handler_id] = handler
          self.args[key] = handler_id
          #alert(key+':'+ self.args[key])
          x =self.args
      #alert(' ,'.join([k+':'+v for k,v in x.items()]))
      return self
    def click(self,handler):
      self._decorate(handler, onClick=handler)
      return self
    def over(self,handler):
      self._decorate(handler, onMouseOver=handler)
      return
    
class Marker:
    """ Colored shadow on the walls helping the user to deploy a piece in 3D.  :ref:`marker`
    """
    def __init__(self,gui, x, y, fill, face):
        cls='red green blue'.split()
        self.face = face
        k, j, i = face
        OA, OB, OC = 345, 172, 125
        #skew
        self.avatar = gui.ellipse(cx= x+35, cy = y+35, rx=35, ry=35,
                 style=dict(fill=fill, fillOpacity= 0.5))
        self._off = (k * j * OA + k * i * OB + j * i * OC ,
                     k * j * OA+ k * i * OC  + j * i * OB)
        self.hide()
    def show(self, x, y):
        self.avatar.setAttribute("visibility",'hidden')
        self.avatar.setAttribute('cx', x) 
        self.avatar.setAttribute('cy', y)
        self.avatar.setAttribute("visibility",'visible')
    def hide(self):
        self.avatar.setAttribute("visibility",'hidden')
    def on_over(self, ev, i, j, k):
        OFFX, OFFY = self._off
        #x, y, z = [c*f for c,f in zip(self.face,[i,j,k])]
        f= self.face
        x, y, z = k * f[0], j * f[1], i * f[2]
        ax = OFFX+x*100+71*z
        ay = OFFY+y*100+71*z
        #logger('face %s ijk %s xyz %s ax %d ay %d'%(self.face,(i,j,k),(x,y,z),ax,ay))
        self.show(ax, ay)
class Piece(Marker):
    """ Represents the user choice when deployed insde the 3D open cube. :ref:`piece`
    """
    def __init__(self,gui, x, y, fill, r, g, b, board, pid):
        SIDE = 70
        self.board, self.fill, self.pid = board, fill, pid
        self.red, self.green, self.blue = r,g,b
        #self.avatar = gui.ellipse(cx= x+35, cy = y+35, rx=20, ry=20,
        #         style=dict(fill=fill, fillOpacity= 0.5))
        #self.avatex = gui.text(pid, x= x+35, y = y+35+10,
        #         style=dict(fill='navajowhite', fillOpacity= 0.7))
        self.avatar = gui.image(href=REPO%fill,
                    x=x ,y=y, width=SIDE,height=SIDE)
        self.ascore= gui.text(pid, x= 45, y = 300+ pid*30,
                 style=dict(fill='black', fillOpacity= 0.7))
        self.avatar.addEventListener('mouseover', self.on_over)
        #self.avatex.addEventListener('mouseover', self.on_over)
        self.avatar.addEventListener('mouseout', self.on_out)
        self.avatar.addEventListener('click', self.on_click)
        #self.avatex.addEventListener('click', self.on_click)
        self.house = board
        #self.hide()
    def show(self, x, y):
        self.avatar.setAttribute("visibility",'hidden')
        self.avatar.setAttribute('x', x) 
        self.avatar.setAttribute('y', y)
        self.avatar.setAttribute("visibility",'visible')
    def do_markers(self, *a):
        pass
    def _idle(self, *a):
        pass
    def on_over(self, ev):
        self.do_markers(ev)
    def _on_over(self, ev):
        i, j, k = self._ijk
        self.red.on_over(ev, i, j, k)
        self.green.on_over(ev, i, j, k)
        self.blue.on_over(ev, i, j, k)
    def on_click(self, ev):
        self.board.drag(self)
    def place(self, z, y, x, house):
        self.house.remove(self)
        self.house = house
        self.avatar.setAttribute("style",
            "fill: %s; fill-opacity: %f"%(self.fill,  0.3+z*0.35))
        self._ijk = (z, y, x)
        OFFX, OFFY = 170, 170
        ax = OFFX+x*100+71*z
        ay = OFFY+y*100+71*z
        self.show(ax, ay)
        self.avatex.setAttribute("x",ax)
        self.avatex.setAttribute("y",ay+10)
        self.ascore.text = '%d=%d.%d.%d'%(self.pid,z, y, x)
        self.do_markers = self._on_over
    def on_out(self, ev):
        self.red.hide()
        self.green.hide()
        self.blue.hide()

class House:
    """ marks a 3D location inside the cube where a piece can be deployed. :ref:`house`
    """
    def __init__(self,gui, i, j, k, fill, r, g, b, board):
        OFF =170
        SIDE = 99
        RDX = 30
        self.board = board
        self.place = self._place
        self.avatar = gui.rect(x= OFF+k*100+71*i, y = OFF+j*100+71*i,
            width=SIDE-(2-i)*RDX, height=SIDE-(2-i)*RDX,
            style=dict(fill=fill, fillOpacity= 0.2))
        self.avatar.addEventListener('mouseover', self.on_over)
        self.avatar.addEventListener('mouseout', self.on_out)
        self.avatar.addEventListener('click', self.on_click)
        self.red, self.green, self.blue = r,g,b
        self._ijk = (i, j, k)

    def on_over(self, ev):
        i, j, k = self._ijk
        self.red.on_over(ev, i, j, k)
        self.green.on_over(ev, i, j, k)
        self.blue.on_over(ev, i, j, k)
    def _idle(self, *a):
        pass
    def _place(self, ev):
        "ask board to add a piece to itself and disable new deployments here"
        self.board.place(self._ijk, self)
        self.place = self._idle
    def remove(self,piece):
        "set state to receive a piece"
        self.place = self._place
    def on_click(self, ev):
        self.place(ev)
    def on_out(self, ev):
        self.red.hide()
        self.green.hide()
        self.blue.hide()
   
class Cube:
    """ A 3D game board represented in a cavalier projection. :ref:`cube`
    """
    def __init__(self,gui,bottom_image, rear_image, side_image):
        cls='red green blue'.split()
        OFF =123
        SIDE = 300
        RDX = 30
        bottom = gui.image(href=REPO%bottom_image,
                    x=SIDE,y=-2*SIDE, width=SIDE,height=SIDE, rotate= 90)
        rear = gui.image(href=REPO%rear_image,
                    x=0,y=OFF, width=SIDE,height=SIDE, skewX=45, scale=(1,0.71))
        left = gui.image(href=REPO%side_image,
                    x=OFF,y=0, width=SIDE,height=SIDE, skewY=45, scale=(0.71,1))
        self.parts = [bottom, rear, left]
    def hide(self):
        for part in self.parts:
            part.hide()
    def show(self):
        for part in self.parts:
            part.show()

class Form:
    """ Collects demographic info and send results to the server. :ref:`form`
    """
    def __init__(self,gui=None):
        self._build_form(gui)
    def _build_form(self, gui):
        self.form = gui.rect(x=100,y=100, width=600,height=400,
                 style=dict(fill='navajowhite', fillOpacity= 0.8))
        logger('b form a')
        self.form.addEventListener('click', self._submmit)

    def _request_form(self, gui):
        logger('b form a')
        req = ajax()
        logger('b form')
        req.on_complete = self._on_complete
        req.set_timeout(8,self._err_msg)
        req.open('GET','/api/',True)
        #req.set_header('content-type', 'application/x-www-form-urlencoded')
        req.set_header("Content-Type","text/plain; charset=utf-8")
        req.send()
    def _on_complete(self,req):

        if req.status==200 or req.status==0:
            logger('req %s req text %s'%(dir(req),req.header))
            return
            ids = req.text.split('name="_xsrf"')[1][:200].split('"')
            logger('xsrf %s'%(ids))#,ids[7]))
        else:
            logger('error %s'%req.text)
    def _err_msg(self):
        logger('timeout after 8s')
    def _submmit(self,ev):
        self.form.setAttribute("visibility",'hidden')
        logger('submmit')
   
class Phase:
    """ A game stage with a particular scenario and pieces. :ref:`phase`
    """
    def __init__(self, gui, back_layer, component):
        print(component)
        back, puzzle, jigs, faces, pieces = component
        gui.set(back_layer)
        self.group = gui.group(layer=1)
        self.back = [gui.image (href= bk) for bk in back+puzzle]
        self.jigs = [gui.image (href= bk) for bk in jigs]
        print(faces)
        #: The 3D cube for this phase.
        self.cube = Cube(gui, *faces)
        gui.clear()
        Z2TW, TW2Z = [0, 1, 2], [2, 1, 0]
        P_PLC = [[i*j, 350 + 50 * i,610 + 50*j] for j in Z2TW for i in TW2Z]
        #: Original placement of pieces at phase startup.
        self.piece_places = P_PLC
        #: Set of pieces to play in this phase.
        self.pieces = pieces
            

    def reset(self):
        """Rearrange all pieces into original placement. """
        [self.show(x, y) for fid, x, y in self.piece_places]
        pass
    def hide(self):
        self.group.setAttribute('visibility','hidden')
        [piece.hide() for piece in self.pieces]
    def show(self):
        self.group.setAttribute('visibility','visible')
        [self.pieces[fid].show(x, y) for fid, x, y in self.piece_places]
        
class Board:
    """ A meme game board with a 3D cube, some pieces, score and puzzle. :ref:`board`
    """
    def remove(self,piece):
        "acts as a default null house"
        pass
    def _parse_response(self, response, prefices):
        def _figures(response = response):
            #workaround for brython bug
            resp = eval(response.text)
            return resp['result']
        #figures = resp['result']
        return [
            [[img for img in _figures()
                if ('%s0%d'%(prefix, infix)) in img] for infix in range(7)
            ]
            for prefix in prefices.split()]
    def _load_scenes(self, response):
        self.face_imgs, self.back_imgs =self._parse_response(response, 'face backs')
        self._build_phases()
    def _load_figures(self, response):
        self.piece_imgs, self.jig_imgs, self.puzzle_imgs = self._parse_response(
            response, 'piece jigs puzzle')
        self.gui.request('/rest/studio/memit?type=2', self._load_scenes)
    def _load_inventory_from_server(self):
        self.gui.request('/rest/studio/memit?type=1', self._load_figures)
    def _build_markers(self, gui):
        self.red = Marker(gui, 300,300,'red',(0,1,1))
        self.green = Marker(gui, 300,300,'green',(1,0,1))
        self.blue = Marker(gui, 300,300,'blue',(1,1,0))
        
    def place(self, *a):
        """Placement state method. Assumes _place (active) or _idle states"""
        pass
    def _place(self, position = None, house = None):
        self.piece.place(*position, house = house)
        self.place = self._idle
        return self.piece
    def _idle(self, *a):
        pass
    def _drag(self, p =None):
        i, j, k = self._ijk
    def drag(self, p =None):
        """Enable placement of pieces. Arg p is the piece being dragged """
        self.piece = p
        self.place = self._place
    def __init__(self,gui):
        self.gui = gui
        self.houses = []
        self.phases = []
        self.piece  = None
        self.phase = 0
        self._load_inventory_from_server()
    def _build_layers(self,gui):
        self.back_layer = gui.group(layer=0)
        self.marker_layer = gui.group()
        self._build_markers(gui)
        gui.clear()
        self.pieces_layer = gui.group(layer=0)
    def _build_inventory_locally(self):
        # not being used currently, should be a fallback for server failure
        PHASES = 7
        PIECES = 9
        #self.faces = ['valor.png','beleza.png','conforto.png'] * PHASES
        self.back_imgs = ['back%02d.jpg'%(phase)
            for phase in range(PHASES)]
        self.puzzle_img = ['puzzle%02d.jpg'%(phase)
            for phase in range(PHASES)]
        self.jig_imgs = [
            ['jigs%02d_%02d.jpg'%(phase,face) for face in range(PIECES)]
            for phase in range(PHASES)]
        self.face_imgs = [['face%02d_%02d.jpg'%(phase,face) for face in [0,1,2]]
            for phase in range(PHASES)]
        self.piece_imgs = ['piece%02d_%02d.png'%(kind,piece)
            for piece in range(PIECES) for kind in [0,1]]
    def _build_phases(self):
        gui= self.gui
        CLS='red green blue'.split()
        Z2TW, TW2Z = [0, 1, 2], [2, 1, 0]
        KINDS = [0,1]#[0]*2+[1]*5
        self._build_layers(gui)
        RGB = [self.red, self.green, self.blue]
        #piece_places = [[[350 + 50 * i,610 + 50*j]
        #    for j in Z2TW] for i in TW2Z]
        piece_places = [[i*j, 350 + 50 * i,610 + 50*j]
            for j in Z2TW for i in TW2Z]
        print (piece_places)
        gui.set(self.pieces_layer)
        pc = self.pieces = [
            [Piece(gui, x, y, self.piece_imgs[kind][fid], *RGB, board = self, pid = fid)
            for fid, x, y in piece_places] for kind in KINDS]
        logger('to b form')
        gui.clear()
        piece_imgs = [pc[i] for i in [0,0,1,1,1,1,1]]
        self.phases = [Phase(gui, self.back_layer, components)
            for components in zip(self.back_imgs,
                self.puzzle_imgs, self.jig_imgs, self.face_imgs, piece_imgs)]
        gui.set(self.back_layer)
        self.houses = [House(gui, i, j, k, CLS[i], *RGB, board = self)
                       for k in Z2TW for j in Z2TW for i in TW2Z]
        gui.clear()
        self.phases[0].show()
         
def main(dc,pn, gui, repo):
    """ Starting point """
    global REPO
    REPO = repo
    return Board(gui)
    """
    #for phase in phases:
    #    Phase(gui, self.back_layer)
        #self.phases= [
        #    [Cube(gui, *faces),None] for faces in self.face_imgs[phase]]
        #self._build_markers(gui)
        #for i in [2,1,0]:
        #    for j in [0,1,2]:
        #        for k in [0,1,2]:
        #            self.houses.append( House(gui, i, j, k, cls[i],
        #                         self.red, self.green, self.blue, self))
        #for i in [2,1,0]:
        #    for j in [0,1,2]:
        #        Piece(gui,610 + 50*j, 350 + 50 * i, 'black',
        #            self.red, self.green, self.blue, self,3*i+j+1)
    #self._build_form(gui)
    """
