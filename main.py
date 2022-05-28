from pprint import pprint
import requests

# ------------------------ЗАДАНИЕ_1------------------------ #

def get_name_list(): # Принимает список с именами
    name_list = input("Введите прозвище(-а) супер героя(-ев): ").strip().split(', ')
    return name_list

def get_character_iq():
    name_list = get_name_list()
    intelligence_list = []
    result = {}
    for name in name_list:
        url = f"https://superheroapi.com/api/2619421814940190/search/{name}"
        response = requests.get(url)
        response_data = response.json()
        intelligence_list += response_data['results'][0]['powerstats']['intelligence'].split(', ')
    for x, y in zip(name_list, intelligence_list):
        result[x] = int(y)
    pprint(max(result))


# ------------------------ЗАДАНИЕ_2------------------------ #


TOKEN = ""

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_header(self):
        return {
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_header()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_to_disk(self, disk_file_path, file_path):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")



if __name__ == '__main__':
    ya = YaUploader(token=TOKEN)
    ya.upload_to_disk(disk_file_path, file_path)
