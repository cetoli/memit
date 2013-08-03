<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><!--

############################################################
Memit - Serious Game in cavalier projection for memetics
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/08/03
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
        <script type="text/python">
            def on_click(ev):
                pass
        </script>
    </head>
    <body onLoad="brython(1)">
        <div id="data">
            <div id="doc_id" class="hidden_display">{{ doc_id }}</div>
            <form action="register/head" id="head" method="post" name="Head">
                <table border="0" cellpadding="1" cellspacing="1" style="width:500px">
                    <tbody>
                        <tr>
                            <td>&nbsp;</td>
                            <td><input name="male" type="radio" /><img alt="" src="/userfiles/images/Golf%20Ball.jpg" style="height:50px; width:50px" /></td>
                            <td><input name="female" type="radio" /><img alt="" src="/userfiles/images/Mouse.jpg" style="height:39px; width:50px" /></td>
                            <td>&nbsp;</td>
                        </tr>
                        <tr>
                            <td><input name="male" type="radio" /><img alt="" src="/userfiles/images/Golf%20Ball.jpg" style="height:50px; width:50px" /></td>
                            <td><input name="male" type="radio" /><img alt="" src="/userfiles/images/Golf%20Ball.jpg" style="height:50px; width:50px" /></td>
                            <td><input name="male" type="radio" /><img alt="" src="/userfiles/images/Golf%20Ball.jpg" style="height:50px; width:50px" /></td>
                            <td><input name="male" type="radio" /><img alt="" src="/userfiles/images/Golf%20Ball.jpg" style="height:50px; width:50px" /></td>
                        </tr>
                        <tr>
                            <td><input name="female" type="radio" /><img alt="" src="/userfiles/images/Mouse.jpg" style="height:39px; width:50px" /></td>
                            <td><input name="female" type="radio" /><img alt="" src="/userfiles/images/Mouse.jpg" style="height:39px; width:50px" /></td>
                            <td><input name="female" type="radio" /><img alt="" src="/userfiles/images/Mouse.jpg" style="height:39px; width:50px" /></td>
                            <td><input name="female" type="radio" /><img alt="" src="/userfiles/images/Mouse.jpg" style="height:39px; width:50px" /></td>
                        </tr>
                        <tr>
                            <td>&nbsp;</td>
                            <td>&nbsp;</td>
                            <td>&nbsp;</td>
                            <td><input alt="" src="/userfiles/images/Public%20Folder/advancedsettings.png" style="width: 50px; height: 50px;" type="image" /></td>
                        </tr>
                    </tbody>
                </table>
                </form>

        </div>
    </body>
</html>
