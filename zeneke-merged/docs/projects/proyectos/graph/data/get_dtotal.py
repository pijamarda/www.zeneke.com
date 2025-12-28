#!/usr/bin/python3
# -*- coding:utf-8 -*-

#   Al ejecutable se puede lanzar de dos formas:
#
#   1. Lanzando el ejecutable sin argumentos
#   	   ./NombreDelEjecutable
#      El programa coge la ultima semana comple de domingo a sabado
#
#   2. Lanzando el ejecutable con un argumento de fecha.
#      El argumento tiene que tener el formato YYYY/MM/DD
#   	   ./NombreDelEjecutable 2013/04/16
#      El programa coge la ultima semana comple de domingo a sabado, anterior a la fecha introducida.

import pymysql
import sys
import datetime
import csv
import json
import calendar
from collections import Counter

def imprimirFecha(fe):
	if 'Mon' in fe:
		return 'Lunes'
	if 'Tue' in fe:
		return 'Martes'
	if 'Wed' in fe:
		return 'Miercoles'
	if 'Thu' in fe:
		return 'Jueves'
	if 'Fri' in fe:
		return 'Viernes'
	if 'Sat' in fe:
		return 'Sabado'
	if 'Sun' in fe:
		return 'Domingo'
	else:
		return 'Mal Dia'

fichero = 'rules.csv'
network_rules = []
host_rules = []
contador_network = 0
contador_host = 0

conn = None

nombres = []
elementos = []
primera_linea = []
#primera_linea.append('Categories')
next_linea = []

f = csv.reader(open(fichero, newline = "",encoding="utf-8"))
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
	

#for i in range(len(network_rules)):
#	for j in range(len(network_rules[i])):
#			if j == 0:
				#primera_linea.append(network_rules[i][j])
				#print(network_rules[i][j])

#elementos.append(primera_linea)


try:

	conn = pymysql.connect(host='localhost',user='root',
						passwd='q1w2e3r4t5', db='dlp')


	cur=conn.cursor()

	now = datetime.datetime.now()
	dias = 180
	fechas = []
	fechas_epoc = []
	Total = 0

	for i in range(dias,0,-1):
		fechas.append((now + datetime.timedelta(days=-i)).strftime("%a %b %d % %Y"))
		fechas_epoc.append(calendar.timegm((now + datetime.timedelta(days=-i)).timetuple())*1000)

	#for i in range(len(fechas_epoc)):
	#	print(fechas_epoc[i])

	for x in range(len(network_rules)):
		print("Regla: " + network_rules[x][0])
		for i in range(len(fechas)): 
			print("Fecha: " + fechas[i])
			next_linea = []
			fecha = ("(Timestamp like '") + fechas[i] + ("')")			
			next_linea.append(fechas_epoc[i])
			
			for y in range(1,len(network_rules[x])):
				buscar = ('SELECT DISTINCT incidentid, count(Rule) FROM ndlp where rule like "') + network_rules[x][y] +('" and ') + fecha
				cur.execute (buscar)
				fe1 = cur.fetchone()
				Total = Total + fe1[1]
			print (Total)
			next_linea.append(Total)
			Total = 0
			elementos.append(next_linea)			
			
		#for x in range(len(elementos)):
		#	print(elementos[x])
			
		filename = 'dtotal_' + network_rules[x][0][:3]  +'.json'
		
		print("Imprimimos el json: ")
		print(json.dumps(elementos))

		with open(filename, 'wt', encoding='utf8') as f:
			print("Guardando en: " + filename)
			f.write(json.dumps(elementos))	
		elementos = []
except pymysql.Error as e:

	print ("Error en connexión a BBDD")
	sys.exit(1)

finally:

	if conn:
		conn.close()


