import requests
API_KEY = "3639e3ee1bbac0ce7c00914c8ea8a6f7"


def get_data(place, days):
    URL = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    responce = requests.get(URL)
    data = responce.json()
    filtered_data = data["list"]
    nr_days = 8 * days
    filtered_data = filtered_data[:nr_days]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="chennai", days=3))