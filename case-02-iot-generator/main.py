import random

def generator_suhu():
    while True:
        suhu = random.uniform(20.0, 40.0)
        yield suhu

sensor = generator_suhu()

print(f"Suhu yang terbaca adalah: {next(sensor):.2f} celcius")
print(f"Suhu yang terbaca adalah: {next(sensor):.2f} celcius")
print(f"Suhu yang terbaca adalah: {next(sensor):.2f} celcius")

