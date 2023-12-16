from random import randint
from datetime import time
hash_table = {}


def store_sensors_data():
    sensor_id = 1

    while True:
        temperature = randint(26, 50) # ºC
        pressure = randint(1, 5) # atm
        humidity = randint(30, 120) # kg/m³
        registration_time = time()
        hash_table