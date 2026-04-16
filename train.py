#!/usr/bin/python3

import csv
import json
from utils import estimate_price 

def main():

	data = []
	
	theta0 = 0
	theta1 = 0
	learningrate = 0.00001
	with open('data.csv', 'r') as file:
		reader = csv.DictReader(file)
		for row in reader:
			data.append((float(row['km']) / 1000, float(row['price'])))
	for n in range(3000):
		errortheta0 = 0
		errortheta1 = 0
		for mileage, price in data:
			errortheta0 = errortheta0 + ((estimate_price(theta0, theta1, mileage) - price) / len(data) * 1000)
			errortheta1 = errortheta1 + (((estimate_price(theta0, theta1, mileage) - price) * mileage ) / len(data))
			
		print ("iter", n)
		print(f"theta0= " + str(theta0))
		print(f"theta1= " + str(theta1))
		theta0 = theta0 - (learningrate * errortheta0)
		theta1 = theta1 - (learningrate * errortheta1)
	print (theta0)
	print (theta1)




if __name__ == "__main__":
	main()