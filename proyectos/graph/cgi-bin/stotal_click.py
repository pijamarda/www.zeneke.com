#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pymysql
import sys
import datetime
import csv
import json
import calendar
import codecs, sys
import cgi
import time
from collections import Counter
from time import mktime
from datetime import datetime

#este es el fichero general maestro donde estan todas las reglas configuradas
fichero = '/home/administrator/Scripts/config/rules.csv'
network_rules = []
host_rules = []


conn = None

elementos = []

#-------------------------------------------------------------------
#SELECCIONAMOS QUE ELEMENTOS QUEREMOS MOSTRAR
#0='ID' 1='Politica' 2='Fecha' 3='Accion' 4='Remitente' 5='Regla' 6='Fichero' 7='Dominio' 8='Contenido' 9='Asunto']

columnas=[0,2,8,4]
cabecera=['ID','Politica','Fecha','Accion','Remitente','Regla','Fichero','Dominio','Contenido','Asunto']
#-------------------------------------------------------------------

#Aqui lo que hacemos es coger todas las reglas tanto de NDLP como de HDLP del fichero maestro
#y las metemos en network_rules o host_rules respectivamente
f = csv.reader(open(fichero, newline = "",encoding="utf-8"))
contador_network = 0
contador_host = 0
for row in f:	
	if row[0] == 'network':
		network_rules.append([])
		for i in range (1,len(row)):
			network_rules[contador_network].append(row[i])
		contador_network += 1
	elif row[0] == 'host':
		network_host.append([])
		for i in range (1,len(row)):
			host_rules[contador_host].append(row[i])
		contador_host += 1

#-------------------------------------------------------------
# Este apartado sirve para capturar los datos enviados desde el html con la fecha y la regla seleccionada
form = cgi.FieldStorage()
regla_temp = form.getvalue("regla", "")
regla = regla_temp.replace("\r\n","")
fecha_selec = form.getvalue("fecha", "")
tipo = form.getvalue("tipo", "")
#La fecha viene en formato string del tipo '29/02/2013' por lo que hay que transformarlaa
if (tipo == 'stock'):
	fecha_tmp_regla = float(fecha_selec) / 1000
	fecha_regla = time.strftime("%a %b %d % %Y", time.localtime(fecha_tmp_regla))
else :
	fecha_tmp_regla = time.strptime(fecha_selec, "%d/%m/%Y")
	#con esta orden ponemos la fecha en formato 'Wed Oct 02 % 2013' que es lo que entiende la BBDD
	fecha_regla = (datetime.fromtimestamp(mktime(fecha_tmp_regla))).strftime("%a %b %d % %Y")

#-------------------------------------------------------------

salto = " <br /> "

print('Content-type: text/html; charset="UTF-8"\n\n');
print("Incidentes\n\n " + salto)

try:

	conn = pymysql.connect(host='localhost',user='root',
						passwd='q1w2e3r4t5', db='dlp')

	cur=conn.cursor()

	dias = 2
	fechas = []
	fechas_epoc = []

	#Recorremos las reglas buscando la que envia el html, deben coincidir ya que beben del mismo fichero maestro de reglas
	print(regla)
	print(salto)
	#print(fecha_selec)
	for x in range(len(network_rules)):
		if network_rules[x][0] == regla:
			print(salto)
			fecha = ("(Timestamp like '") + fecha_regla + ("')")			
			print('<table width="100%">')
			print('<tr>')
			for i in range(len(columnas)):
				print('<td>'+ cabecera[columnas[i]]+ '</td>')
			print('</tr>')
			for y in range(1,len(network_rules[x])):
				buscar = ('SELECT * FROM ndlp where rule like "') + network_rules[x][y] +('" and ') + fecha + (' group by incidentid')
				cur.execute (buscar)				
				fe1 = cur.fetchone()
				while (fe1 != None):
					print('<tr>')
					#imprimimos todos
					#print(fe1)
					#imprimimos los que queramosa
					for z in range(len(columnas)):
						print('<td>' + fe1[columnas[z]]+ '</td>')
					fe1 = cur.fetchone()	
					print('</tr>')
			print('</table>')
except pymysql.Error as e:

	print ("Error en connexión a BBDD")
	sys.exit(1)

finally:

	if conn:
		conn.close()


