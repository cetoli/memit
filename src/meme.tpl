<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><!--

############################################################
Memit - Serious Game in cavalier projection for memetics
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/03/29
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
__author__ = "Carlo E. T. Oliveira (carlo@nce.ufrj.br)"
__version__ = "0.1"
__date__ = "2013/03/29"
-->
<html>
<head>
<meta charset="iso-8859-1">
<title>ActivUFRJ: Car Badges</title>
<meta http-equiv="content-type" content="application/xml;charset=utf-8" />
<link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon" />
<script type="text/javascript" src="/file/memit/brython.js"></script>
<script type="text/python" src="/file/memit/memit.py">
</script>
<script type="text/python">
class Gui(object):
    def __init__(self, doc):
        self.doc = doc
        self.id = doc["doc_id"]

    def __getitem__(self, obid):
        return self.doc[obid]

    def __le__(self, element):
        self.doc <= element

    def setAttribute(self, elem, atrribute, value):
        self[elem].setAttribute(atrribute, value)
    
    def cling(self, to, from):
        doc[to] <= doc[from]

    def send(self,operation **step):
        def on_complete(req):
            if req.status==200 or req.status==0:
                doc["result"].html = req.text
            else:
                doc["result"].html = "error "+req.text

        req = ajax()
        req.on_complete = on_complete
        url = "/record/"+ operation
        req.open('POST',url,True)
        req.set_header("Content-Type","application/json; charset=utf-8")
        data = str(dict(self.id= step)).replace("'",'"')
        req.send(data)

main(GUI(doc))
</script>
</head>
<body onLoad="brython(1)">
<div id="data">
<div id="doc_id">{{ doc_id }}</div>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
    width="800" height="600" style="border-style:solid;border-width:1;border-color:#000;">
  <g id="panel">
  </g>
</div>
</body>
</html>
