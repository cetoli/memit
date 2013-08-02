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
        <style>
        .hidden_display { display :none;}
        </style>
        <!--script type="text/javascript" src="../libs/lib/brython.js"></script-->
        <script type="text/javascript" src="brython.js"></script>
        <script type="text/python" src="meme.py">
        </script>
        <script type="text/python">
            import svg
            #import time
            main(doc, svg, ajax)
        </script>
    </head>
    <body onLoad="brython(1)">
        <div id="data">
            <div id="doc_id" class="hidden_display">{{ doc_id }}</div>
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
