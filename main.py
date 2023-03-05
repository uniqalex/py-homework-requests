import requests

#Task_1 start
url_all = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url_all)
all_stats = {heroe['name']:heroe['powerstats']['intelligence'] for heroe in resp.json()}
print(max(all_stats, key=all_stats.get))
#Task_1 end

#Task_2 start
class YaUploader:

    def __init__(self, token: str):
        self.token = token
        self.yandex_api = 'https://cloud-api.yandex.net:443/'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_href(self, destination_file_path):
        upload_ulr = f'{self.yandex_api}v1/disk/resources/upload'
        hdrs = self.get_headers()
        params = {'path': destination_file_path, 'overwrite':'true'}
        response = requests.get(upload_ulr, headers=hdrs, params=params)
        return response.json()

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        href = self.get_upload_href(destination_file_path=file_path).get('href', '')
        with open(file_path, 'rb') as file:
            f = file.read()
            response = requests.put(url=href, data=f)
            if response.status_code == 201:
                print('File uploaded')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'TestFile1.txt'
    token = 'password'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
#Task_2 end

