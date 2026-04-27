#!/usr/bin/python3

import csv
import json
from utils import estimate_price 

def main():

	data = []
	
	theta0 = 0
	theta1 = 0
	learningrate = 0.0001
	with open('data.csv', 'r') as file:
		reader = csv.DictReader(file)
		for row in reader:
			data.append((float(row['km']) / 1000, float(row['price'])))
	for n in range(300000):
		errortheta0 = 0
		errortheta1 = 0
		for mileage, price in data:
			errortheta0 = errortheta0 + ((estimate_price(theta0, theta1, mileage) - price) / len(data))
			errortheta1 = errortheta1 + (((estimate_price(theta0, theta1, mileage) - price) * mileage ) / len(data))
		theta0 = theta0 - (learningrate * errortheta0)
		theta1 = theta1 - (learningrate * errortheta1)
	thetas = dict(
		theta0= theta0,
		theta1 = theta1)
	try:
		with open('thetas.json', 'w') as json_file:
			json.dump(thetas, json_file,  indent=2)
	except FileNotFoundError:
		print(f"Error: no existe el archivo {'thetas.json'}")
		return
	except PermissionError:
		print(f"Error: sin permisos para {'thetas.json'}")
		return
	print("Archivo JSON generado correctamente")

if __name__ == "__main__":
	main()