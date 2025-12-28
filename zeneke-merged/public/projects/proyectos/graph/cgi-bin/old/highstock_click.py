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
regla = form.getvalue("regla", "")
fecha_selec = float(form.getvalue("fecha", ""))
#fecha_selec = 1376791519000
#La fecha viene en formato string del tipo '29/02/2013' por lo que hay que transformarla
fecha_tmp_regla = fecha_selec / 1000
#con esta orden ponemos la fecha en formato 'Wed Oct 02 % 2013' que es lo que entiende la BBDD
fecha_regla = time.strftime("%a %b %d % %Y", time.localtime(fecha_tmp_regla))
#-------------------------------------------------------------


salto = " <br /> "

print('Content-type: text/html; charset="UTF-8"\n\n');
print("Incidentes\n\n " + salto)

print(regla)
print(fecha_regla)
try:

	conn = pymysql.connect(host='localhost',user='root',
						passwd='q1w2e3r4t5', db='dlp')

	cur=conn.cursor()

	dias = 2
	fechas = []
	fechas_epoc = []

	#Recorremos las reglas buscando la que envia el html, deben coincidir ya que beben del mismo fichero maestro de reglas
	#for x in range(0):
	for x in range(len(network_rules)):
		if network_rules[x][0] == regla:		
			print("Fecha: " + fecha_regla)
			print(salto)
			fecha = ("(Timestamp like '") + fecha_regla + ("')")			
			for y in range(1,len(network_rules[x])):
				buscar = ('SELECT * FROM ndlp where rule like "') + network_rules[x][y] +('" and ') + fecha + (' group by incidentid')
				cur.execute (buscar)				
				fe1 = cur.fetchone()
				while (fe1 != None):
					#imprimimos todos
					#print(fe1)
					#imprimimos los que queramos
					print(fe1[0]+ ' '+fe1[2]+' '+fe1[5]+' '+fe1[7])
					print("\n" + salto)
					fe1 = cur.fetchone()	

except pymysql.Error as e:

	print ("Error en connexión a BBDD")
	sys.exit(1)

finally:

	if conn:
		conn.close()


