import plotly.express as px
from utils import estimate_price
import statistics

def create_graph(data, theta0, theta1):
	x = [km for km, price in data]
	y = [price for km, price in data]
	fig = px.scatter(x=x, y=y, labels={'x': 'Kilómetros (miles)', 'y': 'Precio (€)'}, title='Relación entre Kilómetros y Precio')
	fig.add_scatter(x=x, y=[estimate_price(theta0, theta1, km) for km in x], mode='lines', name='Recta de Regresión')
	fig.show()
	fig.write_html("my_graph.html")

def calculate_precision(data, theta0, theta1):
	precios = [price for km, price in data]
	mean = statistics.mean(precios)
	scr = 0
	sct = 0
	print(f"The mean is {mean}")
	for km, price in data:
		predicted_price = estimate_price(theta0, theta1, km)
		scr += (price - predicted_price) ** 2
		sct += (price - mean) ** 2
	r2 = 1 - (scr / sct)
	print(f"R2 precision is {r2}")