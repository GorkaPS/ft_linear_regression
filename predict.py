

import json
from utils import estimate_price 
import sys

def main():
	if len(sys.argv) == 2 and sys.argv[1] in ("--help", "-h"):
		return help_message()
	if len(sys.argv) != 2:
		print("uso: python3 predict.py kilometers")
		return
	if not sys.argv[1].isnumeric():
		print("Argument 2 must be a positive number")
		return
	for i,arg in enumerate(sys.argv):
		if len(arg) == 0:
			print(f"Argumento {i} inválido, string vacío.")
			return
	try:
		with open('thetas.json', 'r') as json_file:
			thetas = json.load(json_file)
		required = ["theta1", "theta0"]
		missing = [key for key in required if key not in thetas]
		if missing:
			print("Faltan claves o valores:", missing)
			return
		if thetas["theta0"]:
			theta0 = thetas['theta0']
		if thetas["theta1"]:
			theta1 = thetas['theta1']
	except FileNotFoundError:
		print(f"Error: no existe el archivo {'thetas.json'}")
		return
	except PermissionError:
		print(f"Error: sin permisos para {'thetas.json'}")
		return
	
	predicted_price = round(estimate_price(theta0, theta1, int(sys.argv[1]) / 1000), 2)
	if predicted_price < 0:
		predicted_price = 0
	print(f"Precio estimado para {sys.argv[1]} km es: {predicted_price}$")



def help_message():
	print("usage: ft_turing [-h] jsonfile input\n")
	print("positional arguments:")
	print("\tjsonfile	json description of the machine\n")
	print("\tinput		input of the machine\n")
	print("optional arguments:")
	print("\t-h, --help	show this help message and exit\n")

if __name__ == "__main__":
	main()