import requests


def create_dir(token, name_dir, URL):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}',
    }

    response = requests.put(
        url=URL,
        params={'path': name_dir, "overwrite": "true"},
        headers=headers,
    )
    print(response.json())
    print(response.status_code)


    return response.status_code



if __name__ == '__main__':
    URL = "https://cloud-api.yandex.net/v1/disk/resources"
    token = 'AQAAAAABNrQ-... '
    name_dir = 'NewDir'
    create_dir(token, name_dir, URL)
