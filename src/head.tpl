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
            <form action="head" id="head" method="post" name="Head">
                <input name="doc_id" id="doc_id" value="{{ doc_id }}" type="hidden" />
                <table border="0" cellpadding="1" cellspacing="1" style="width:1000px">
                    <tbody>
                        <tr style="padding:50px; margin:50px">
                            <td>&nbsp;</td>
                            <td><input name="sex" id="male" value="male" type="radio" />
                                <label for="male"><img alt="MALE" title="MALE" src="studio/memit/Male.png" style="margin-top: 80px; height:50px; width:50px" /></label></td>
                            <td><input name="sex" id="female"  value="female" type="radio" />
                                <label for="female"><img alt="FEMALE" title="FEMALE" src="studio/memit/Female.png" style="margin-top: 80px; height:39px; width:50px" /></label></td>
                            <td>&nbsp;</td>
                        </tr>
                        <tr style="padding:50px; margin:50px">

                            <td><input name="age" id="age18" value="age18" type="radio" />
                                <label for="age18"><img alt="Age 18 to 24" title="Age 18 to 24" src="studio/memit/18_anos.jpg" style="margin-top:80px; height:100px;" /></label></td>
                            <td><input name="age" id="age25" value="age25" type="radio" />
                                <label for="age25"><img alt="Age 25 to 44" title="Age 25 to 44" src="studio/memit/25_anos.jpg" style="margin-top: 80px; height:100px;" /></label></td>
                            <td><input name="age" id="age45" value="age45" type="radio" />
                                <label for="age45"><img alt="Age 45 to 64" title="Age 45 to 64" src="studio/memit/45_anos.jpg" style="margin-top: 80px; height:100px;" /></label></td>
                            <td><input name="age" id="age65" value="age65" type="radio" />
                                <label for="age65"><img alt="Age 65 to 124" title="Age 65 to 124" src="studio/memit/65_anos.jpg" style="margin-top: 80px; height:100px;" /></label></td>
                        </tr>
                        <tr style="padding:50px; margin:50px">
                            <td><input name="budget" id="budget18" value="budget18" type="radio" />
                                <label for="budget18"><img alt="Budget 1800 to 2400" title="Budget 1800 to 2400" src="studio/memit/18_budget.jpg" style="margin-top: 80px; height:90px;" /></label></td>
                            <td><input name="budget" id="budget25" value="budget25" type="radio" />
                                <label for="budget25"><img alt="Budget 2500 to 4400" title="Budget 2500 to 4400" src="studio/memit/25_budget.jpg" style="margin-top: 80px; height:90px;" /></label></td>
                            <td><input name="budget" id="budget45" value="budget45" type="radio" />
                                <label for="budget45"><img alt="Budget 4500 to 6400" title="Budget 4500 to 6400" src="studio/memit/45_budget.jpg" style="margin-top: 80px; height:90px;" /></label></td>
                            <td><input name="budget" id="budget65" value="budget65" type="radio" />
                                <label for="budget65"><img alt="Budget 6500 and +" title="Budget 6500 and +" src="studio/memit/65_budget.png" style="margin-top: 80px; height:90px;" /></label></td>
                        </tr>
                        <tr style="padding:50px; margin:50px">
                            <td>&nbsp;</td>
                            <td>&nbsp;</td>
                            <td>&nbsp;</td>
                            <td><input alt="" src="studio/memit/continue_arrow.png" style="margin-top: 80px; height: 100px;" type="image" /></td>
                        </tr>
                    </tbody>
                </table>
                </form>

        </div>
    </body>
</html>
