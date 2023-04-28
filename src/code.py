import eel
import pyowm
from tabulate import tabulate
from prettytable import PrettyTable
owm = pyowm.OWM("178b3f1af37efa266b1b8ff3db366faa")

@eel.expose
def get_weather(city):
	mrg = owm.weather_manager()

	observation = mrg.weather_at_place(city)
	w = observation.weather

	temp =  w.temperature('celsius')['temp']
	res = "В городе " + city + " сейчас " + str(temp) + " градусов"
	data = [[city, str(temp)]]
	col_name = ["Город", "Температура"]
	print(tabulate(data, headers=col_name, tablefmt="fancy_grid"))

	return res




eel.init("browse")

eel.start('code.html', size=(1000, 1000))

