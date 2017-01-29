#########################################
#     David Fernández  24.313.648       #
#########################################


import csv, operator
import matplotlib.pyplot as plt
import pandas as pd


with open('student-mat.csv') as csvarchivo:
	entrada = csv.reader(csvarchivo, delimiter=';')
	for index,row in enumerate(entrada):
		print ("persona: " + str(index+1))
		print ("------------------------")
		print ("school: " + row[0])
		print ("sex: " + row[1])
		print ("age: " + row[2])
		print ("address: " + row[3])	
		print ("famsize: " + row[4])	
		print ("Pstatus: " + row[5])	
		print ("Medu: " + row[6])	
		print ("Fedu: " + row[7])	
		print ("Mjob: " + row[8])	
		print ("Fjob: " + row[9])	
		print ("reason: " + row[10])	
		print ("guardian: " + row[11])	
		print ("traveltime: " + row[12])	
		print ("studytime: " + row[13])	
		print ("failures: " + row[14])	
		print ("schoolsup: " + row[15])	
		print ("famsup: " + row[16])	
		print ("paid: " + row[17])	
		print ("activities: " + row[18])	
		print ("nursery: " + row[19])	
		print ("higher: " + row[20])	
		print ("internet: " + row[21])	
		print ("romantic: " + row[22]) 	
		print ("famrel: " + row[23]) 
		print ("freetime: " + row[24])	
		print ("goout: " + row[25])	
		print ("Dalc: " + row[26])	
		print ("Walc: " + row[27])
		print ("health: " + row[28])	
		print ("absences: " + row[29])
		print ("G1: " + row[30])	
		print ("G2: " + row[31])	
		print ("G3: " + row[32])
		print ("\n")

#  Histograma sobre la cantidad de alumnos agrupados por sus edades
data = pd.read_csv('student-mat.csv',sep=';', index_col=0)
data['age'].hist()
plt.xlim([14,23])
plt.title("Histograma sobre la cantidad de alumnos agrupados por sus edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()


# Diagrama de Dispersión entre consumo de alcohol y ausencias
plt.scatter(data['Walc'], data['absences'], c='red')
plt.title('Diagrama de Dispersión entre consumo de alcohol y ausencias')
plt.xlabel('Consumo de alcohol los fines de semana')
plt.ylabel('Ausencias')
plt.show()