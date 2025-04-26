# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Загрузите содержимое последнего файла из набора, как ответ на это задание.
import requests

url = "https://stepik.org/media/attachments/course67/3.6.3/699991.txt"

r = requests.get(url.strip())
while True:
    if r.text.startswith("We"):
        print(r.text)
        break
    else:
        url = "https://stepik.org/media/attachments/course67/3.6.3/" + r.text.strip()
        r = requests.get(url.strip())
        print(r.text)

with open(
    "C:\Git_repository\first_project\stepik_tasks\we_are_the_champions.txt", "w"
) as file:
    file.write(r.text)
