import requests

URL = 'https://official-joke-api.appspot.com/random_joke'


def __check_valid_response_code(request):
    if request.status_code == 200:
        return request.json()

    return False


def get_joke():
    request = requests.get(URL)
    data = __check_valid_response_code(request)

    return data
