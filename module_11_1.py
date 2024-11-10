import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 54.8444400,  # широта Каширы
    "longitude": 38.1669400,  # долгота Каширы
    "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum",
    # минимальная и максимальная температура, сумма осадков
    "timezone": "Europe/Moscow"  # временная зона для Каширы
}
response = requests.get(BASE_URL, params=params)
if response.status_code == 200:
    data = response.json()
    # Поскольку индекс 0 представляет собой данные на текущий день, индекс 1 будет представлять данные на завтра
    tomorrow_temp_min = data['daily']['temperature_2m_min'][1]
    tomorrow_temp_max = data['daily']['temperature_2m_max'][1]
    tomorrow_precipitation = data['daily']['precipitation_sum'][1]

    print(f"Прогноз погоды в Кашире на завтра:")
    print(f"Минимальная температура: {tomorrow_temp_min}°C")
    print(f"Максимальная температура: {tomorrow_temp_max}°C")
    print(f"Ожидаемое количество осадков: {tomorrow_precipitation} мм")
else:
    print(f"Ошибка {response.status_code}: {response.text}")
