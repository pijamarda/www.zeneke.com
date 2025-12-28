#!/usr/bin/python3
# -*- coding:utf-8 -*-
import cgi
import webbrowser

def header(title):
    print ("""Content-type: text/html; charset="UTF-8"\n\n""")
    print ("""<!DOCTYPE html>
<head>
    
    <link rel="stylesheet" href="../css/default2.css" />
    <title>Login para Graficas</title>
</head>
<BODY>""")

def footer():
    print ("</BODY></HTML>")

form = cgi.FieldStorage()
password = "dgarcia"

if not form:
    header("Login Response")
elif "login" in form and form["login"].value != "" and "password" in form and form["password"].value == password:
    
    header("Connected ...")
    print("""
        <div id="logo">
            <table height="100%">
            <tr>
            <td><img src="../img/logo2.png" style='border-radius:0px; border:0px; padding:0px; margin:0px; align:bottom'/></td>    
            <td width="100%" align="right"> <font size="6" color="white">Telefonica Soluciones &nbsp&nbsp&nbsp</font></td>
            </tr>
            </table>
        </div>

        """)
    print ("<center><hr><H3>Bienvenido," , form["login"].value, ". <a href=../index2.html>Pinchar aqui para continuar</a></H3><hr></center>")
    print (r"""<form><input type="hidden" name="session" value="%s"></form>""" % (form["login"].value))
    #print ("<H3><a href=../index2.html>Pinchar aqui para continuar</a></H3>")
    print("""
        <div id="footer">
         Telefonica Soluciones Todos los derechos reservados
        </div>

        """)
    

else:
    header("No success!")
    print ("<H3>Contraseña incorrecta</H3>")

footer()
