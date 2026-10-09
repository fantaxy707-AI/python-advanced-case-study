import random

def generator_suhu():
    while True:
        suhu = random.uniform(15.0, 38.0)
        yield suhu

sensor = generator_suhu()

for i in range(1, 11):
    suhu_sekarang = next(sensor)

    if suhu_sekarang < 20.0:
        status = "Dingin"
    elif  20.0 <= suhu_sekarang <= 30.0:
        status = "normal"
    else :
        status = "panas"

    print(f"data ke-{i:02d}: Suhu {suhu_sekarang:.2f} Celcius termasuk katergori: {status}")
