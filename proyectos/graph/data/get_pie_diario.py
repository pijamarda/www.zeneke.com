#!/usr/bin/python3
# -*- coding:utf-8 -*-


import pymysql
import sys
import datetime
import csv
import re

from collections import Counter

dClientes = 0
dActas = 0
dDoc = 0
dFraudes = 0
dMedios = 0
dWebmail = 0

sClientes='Clientes y Empleados'
sActas='Actas de Direccion'
sDoc='Documentacion interna'
sFraudes='Fraudes PCI'
sMedios='Envios a medios'
sWebmail='Webmail'

fichero = '/home/administrator/Scripts/peticiones/listados/datos.csv'
f = csv.reader(open(fichero, newline = "", encoding="utf-8"))
elements = []
for row in f:
	elements.append(row)
for cosas in elements:
	#print(cosas)
	dClientes = dClientes + int(cosas[0])
	dActas = dActas + int(cosas[1])
	dDoc = dDoc + int(cosas[2])
	dFraudes = dFraudes + int(cosas[3])
	dMedios = dMedios + int(cosas[4])
	dWebmail = dWebmail + int(cosas[5])

dTotal = dClientes + dActas + dDoc + dFraudes + dMedios + dWebmail

def porcentage(part, whole):
	resultado = round(100 * float(part)/float(whole))
	return int(resultado)


testClientes = porcentage(dClientes, dTotal)
testActas = porcentage(dActas, dTotal)
testDoc = porcentage(dDoc, dTotal)
testFraudes = porcentage(dFraudes, dTotal)
testMedios = porcentage(dMedios, dTotal)
testWebmail = porcentage(dWebmail, dTotal)
testSuma = 0
def Sumatorio():
	return testClientes + testActas + testDoc + testFraudes + testMedios + testWebmail
testSuma = Sumatorio()
if testSuma > 100:
	while testSuma > 100:
		testWebmail = testWebmail - 1
		testSuma = Sumatorio()
elif testSuma < 100:
	while testSuma < 100:
		testWebmail = testWebmail + 1
		testSuma = Sumatorio()		

pClientes = str(testClientes)
pActas = str(testActas)
pDoc = str(testDoc)
pFraudes = str(testFraudes)
pMedios = str(testMedios)
pWebmail = str(testWebmail)

elementos = []

elementos.append([sClientes,pClientes])
elementos.append([sActas,pActas])
elementos.append([sWebmail,pWebmail])
elementos.append([sFraudes,pFraudes])
elementos.append([sMedios,pMedios])
elementos.append([sDoc,pDoc])

#print(pClientes+' '+pActas+' '+pDoc+' '+pFraudes+' '+pMedios+' '+pWebmail)

fichero_salida = '_dpie_diario.csv'

with open(fichero_salida, 'wt',newline='', encoding='utf8') as f:
	writer = csv.writer(f)
	writer.writerows(elementos)

