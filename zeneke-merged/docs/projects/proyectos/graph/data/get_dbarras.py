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

#	Para añadir nuevas reglas hay que poner:
#		- El nombre de la regla a buscar, que corresponde con "?Rules".
#		- El nombre que se mostrara en los informes, que corresponde con
#  		  "?Rules_nombre".
#	En el nombre "?Rules", la interrogación corresponde con los caracteres
#	incidiales, que son:
#	- PC -> Preven Correo -> PCRules y PCRules_nombre.
#	- M -> Monitor -> MRules y MRules_nombre.

#sGenerales = 'Datos generales'
#RulesG = [  \
#        "LA CAIXA contenido cifrado", \
#        "LA CAIXA actas comite direccion",  \
#        "R_MON_RedOcto"]
#RulesGNombre = [  \
#        "Contenido cifrado:", \
#        "Positivos actas comite direccion:",  \
#        "Positivos APT:"]
#dGenerales = 0

sACD = 'Información confidencial'
RulesACD = [  \
        " ACD"]
RulesACDNombre = [  \
        "ACD:"]
dACD = 0

sClientesEmpleados = 'Datos de clientes y empleados'
RulesCyE = [  \
        "LA CAIXA-Contenido con mas de 50 DNIs", \
        "LA CAIXA-extractos"]
RulesCyENombre = [  \
        "Mas de 50 DNIs:", \
        "Extractos:"]
dClientesEmpleados = 0

sDocInterna = 'Documentación Interna'
RulesDI = ["R_PC_B_UsoInterno"]
RulesDINombre = ["Uso Interno:"]
dDocInterna = 0

sPCI = 'Protección contra fraudes en tarjetas'
RulesPFT = [  \
        "LA CAIXA-Contenido con mas de 50 tarjetas de credito", \
        "R_PC_B_Pista2"]
RulesPFTNombre = [  \
        "Mas de 50 Tarjetas:", \
        "Pista2:"]
dPCI = 0

sMedios = 'Envíos a medios de comunicación'
RulesEMC = ["R_PC_B_EnvioAPrensa_%"]
RulesEMCNombre = ["Envío a dominios de prensa: "]
dMedios = 0

sAdjuntos = 'Envio de adjuntos a WebMail'
RulesAW = [  \
        "R_PC_S_WebmailAttach_Ofi", \
        "R_PC_S_WebmailAttach_SSCC"]
RulesAWNombre = [  \
        "Adjuntos a WebMail Oficinas:", \
        "Adjuntos a WebMail SSCC:"]
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

def imprimirFechaMes(fe):
	if 'Jan' in fe:
		return 'Enero'
	if 'Feb' in fe:
		return 'Febrero'
	if 'Mar' in fe:
		return 'Marzo'
	if 'Apr' in fe:
		return 'Abril'
	if 'May' in fe:
		return 'Mayo'
	if 'Jun' in fe:
		return 'Junio'
	if 'Jul' in fe:
		return 'Julio'
	if 'Aug' in fe:
		return 'Agosto'
	if 'Sep' in fe:
		return 'Septiembre'
	if 'Oct' in fe:
		return 'Octubre'
	if 'Nov' in fe:
		return 'Noviembre'
	if 'Dec' in fe:
		return 'Diciembre'
	else:
		return 'Mal Mes'
conn = None



nombres = []
elementos = []

try:

	conn = pymysql.connect(host='localhost',user='root',
						passwd='q1w2e3r4t5', db='dlp')

	lRule = []

	cur=conn.cursor()
	cur1=conn.cursor()
	cur2=conn.cursor()
	curBlock=conn.cursor()
	curAllow=conn.cursor()


	#Para mirar los 7 días anteriores al dia de hoy, descomentar la siguiente linea
	now = datetime.datetime.now()
	meses = 5
	fechas = []
	fechas_semanal = []

	for i in range(meses,0,-1):
		fechas.append((now + datetime.timedelta(days=(30*-i))).strftime("% %b % %Y"))
		fechas_semanal.append((now + datetime.timedelta(days=-i)).strftime("%d/%m/%Y"))
	for i in range(len(fechas)):
		print(fechas[i])

	for i in range(len(fechas)): 

		fecha = ("(Timestamp like '") + fechas[i] + ("')")
		print(imprimirFechaMes(fechas[i]))
		print(fechas[i])
		Total = 0
		#print ("Datos generales")
		#if (i == 0): nombres.append(sGenerales)
		#print ("===============")
		#for m in RulesG:
		#	buscar = ('SELECT DISTINCT incidentid, count(Rule) FROM ndlp where rule like "') + m +('" and ') + fecha
		#	cur1.execute (buscar)
		#	fe1 = cur1.fetchone()
		#	print (RulesGNombre[RulesG.index(m)], fe1[1])
		#	Total = Total + fe1[1]
		#print ("Total: " + str(Total))
		#print ("\n")
		#dGenerales = Total
		
		print ("Información confidencial")
		if (i == 0): nombres.append(sACD)
		print ("========================")
		for m in RulesACD:
			buscar = ('SELECT DISTINCT incidentid, count(Rule) FROM ndlp where rule like "') + m +('" and ') + fecha
			cur1.execute (buscar)
			fe1 = cur1.fetchone()
			print (RulesACDNombre[RulesACD.index(m)], fe1[1])
			Total = Total + fe1[1]
		print ("Total: " + str(Total))
		print ("\n")
		dACD = Total
		
		Total = 0
		print ("Datos de clientes y empleados")
		if (i == 0): nombres.append(sClientesEmpleados)
		print ("=============================")
		for m in RulesCyE:
			buscar = ('SELECT DISTINCT incidentid, count(Rule) FROM ndlp where rule like "') + m +('" and ') + fecha
			cur1.execute (buscar)
			fe1 = cur1.fetchone()
			print (RulesCyENombre[RulesCyE.index(m)], fe1[1])
			Total = Total + fe1[1]
		print ("Total: " + str(Total))
		print ("\n")
		dClientesEmpleados = Total
		Total = 0
		
		print ("Datos de documentación Interna")
		if (i == 0): nombres.append(sDocInterna)
		print ("==============================")
		for m in RulesDI:
			buscar = ('SELECT DISTINCT incidentid, count(Rule) FROM ndlp where rule like "') + m +('" and ') + fecha
			cur1.execute (buscar)
			fe1 = cur1.fetchone()
			print (RulesDINombre[RulesDI.index(m)], fe1[1])
			Total = Total + fe1[1]
		print ("Total: " + str(Total))
		print ("\n")
		dDocInterna = Total

		Total = 0
		print ("Datos de protección contra fraudes en tarjetas")
		if (i == 0): nombres.append(sPCI)
		print ("==============================================")
		for m in RulesPFT:
			buscar = ('SELECT DISTINCT incidentid, count(Rule) FROM ndlp where rule like "') + m +('" and ') + fecha
			cur1.execute (buscar)
			fe1 = cur1.fetchone()
			print (RulesPFTNombre[RulesPFT.index(m)], fe1[1])
			Total = Total + fe1[1]
		print ("Total: " + str(Total))
		print ("\n")
		dPCI = Total

		Total = 0
		print ("Datos de envíos a medios de comunicación")
		if (i == 0): nombres.append(sMedios)
		print ("========================================")
		for m in RulesEMC:
			buscar = ('SELECT DISTINCT incidentid, count(Rule) FROM ndlp where rule like "') + m +('" and ') + fecha
			cur1.execute (buscar)
			fe1 = cur1.fetchone()
			print (RulesEMCNombre[RulesEMC.index(m)], fe1[1])
			Total = Total + fe1[1]
		print ("Total: " + str(Total))
		print ("\n")
		dMedios = Total
		"""
		Total = 0
		print ("Datos de envío de adjuntos a Webmail")
		if (i == 0): nombres.append(sAdjuntos)
		print ("====================================")
		for m in RulesAW:
			buscar = ('SELECT DISTINCT incidentid, count(Rule) FROM ndlp where rule like "') + m +('" and ') + fecha
			cur1.execute (buscar)
			fe1 = cur1.fetchone()
			print (RulesAWNombre[RulesAW.index(m)], fe1[1])
			Total = Total + fe1[1]
		print ("Total: " + str(Total))
		print ("\n")
		dAdjuntos = Total
		"""
		#if (i == 0): elementos.append(['State',sGenerales,sClientesEmpleados,sDocInterna,sPCI,sMedios,sAdjuntos])
		if (i == 0): elementos.append(['Categories',sACD,sClientesEmpleados,sDocInterna,sPCI,sMedios])
		#elementos.append([imprimirFechaMes(fechas[i]),dGenerales,dClientesEmpleados,dDocInterna,dPCI,dMedios,dAdjuntos])
		elementos.append([imprimirFechaMes(fechas[i]),dACD,dClientesEmpleados,dDocInterna,dPCI,dMedios])
		#print(nombres)
		for x in range(len(elementos)):
			print(elementos[x])
	

except pymysql.Error as e:

	print ("Error en connexión a BBDD")
	sys.exit(1)

finally:

	if conn:
		conn.close()

filename = '_dbarras.csv'

traspuesta = []
for i in range(len(elementos)):
	traspuesta = map(list, zip(*elementos))

with open(filename, 'wt', encoding='utf8') as f:
	writer = csv.writer(f)
	writer.writerows(traspuesta)
