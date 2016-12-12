#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pymysql
import sys
import datetime
import csv
import json
import calendar
from collections import Counter


fichero = 'rules.csv'
network_rules = []
host_rules = []
contador_network = 0
contador_host = 0




dACD = 0
dClientesEmpleados = 0
dPCI = 0
dMedios = 0
dAdjuntos = 0

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
conn = None



nombres = []
elementos = []
primera_linea = []
primera_linea.append('Categories')
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
	

for i in range(len(network_rules)):
	for j in range(len(network_rules[i])):
			if j == 0:
				primera_linea.append(network_rules[i][j])
			print(network_rules[i][j])

elementos.append(primera_linea)

try:

	conn = pymysql.connect(host='localhost',user='root',
						passwd='q1w2e3r4t5', db='dlp')


	cur=conn.cursor()
	now = datetime.datetime.now()
	dias = 7
	fechas = []
	fechas_semanal = []
	Total = 0

	for i in range(dias,0,-1):
		fechas.append((now + datetime.timedelta(days=-i)).strftime("%a %b %d % %Y"))
		fechas_semanal.append((now + datetime.timedelta(days=-i)).strftime("%d/%m/%Y"))

	for i in range(len(fechas)):
		next_linea = []
		fecha = ("(Timestamp like '") + fechas[i] + ("')")
		print(imprimirFecha(fechas[i]))
		print(fechas[i])
		next_linea.append(fechas_semanal[i])
		for x in range(len(network_rules)):
			for y in range(1,len(network_rules[x])):
				buscar = ('SELECT DISTINCT incidentid, count(Rule) FROM ndlp where rule like "') + network_rules[x][y] +('" and ') + fecha
				cur.execute (buscar)
				fe1 = cur.fetchone()
				Total = Total + fe1[1]
			print (network_rules[x][0], Total)
			next_linea.append(Total)
			Total = 0
		elementos.append(next_linea)
			
		
		#if (i == 0): elementos.append(['State',sGenerales,sClientesEmpleados,sDocInterna,sPCI,sMedios,sAdjuntos])
		#if (i == 0): elementos.append(['Categories',sACD,sClientesEmpleados,sDocInterna,sPCI,sMedios])
		#elementos.append([imprimirFecha(fechas[i]),dGenerales,dClientesEmpleados,dDocInterna,dPCI,dMedios,dAdjuntos])
		#elementos.append([fechas_semanal[i],dACD,dClientesEmpleados,dDocInterna,dPCI,dMedios])
		#print(nombres)
	for x in range(len(elementos)):
		print(elementos[x])
	

except pymysql.Error as e:

	print ("Error en connexión a BBDD")
	sys.exit(1)

finally:

	if conn:
		conn.close()

filename = 'dsemanal.csv'



with open(filename, 'wt', encoding='utf8') as f:
	writer = csv.writer(f)
	writer.writerows(elementos)