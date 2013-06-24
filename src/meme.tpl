<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><!--

############################################################
Memit - Serious Game in cavalier projection for memetics
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/06/23
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
-->
<html>
    <head>
        <meta charset="iso-8859-1">
        <title>ActivUFRJ: Car Badges</title>
        <meta http-equiv="content-type" content="application/xml;charset=utf-8" />
        <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon" />
        <script type="text/javascript" src="/file/activlets/brython.js"></script>
        <script type="text/python" src="/file/memit/meme.py">
        </script>
        <script type="text/python">
            import svg
            main(GUI(doc, svg))
        </script>
    </head>
    <body onLoad="brython(1)">
        <div id="data">
            <div id="doc_id">{{ doc_id }}</div>
            <svg xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink" 
                width="800" height="600"
                style="border-style:solid;border-width:1;border-color:#000;">
              <g id="panel">
              </g>
            </svg>
        </div>
    </body>
</html>
