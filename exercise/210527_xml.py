from bs4 import BeautifulSoup
with open('users.xml', 'r', encoding='utf-8') as file:
    data = BeautifulSoup(file, 'html.parser')
    users = data.select('user')
    for user in users:
        name = user.select_one('name')
        age = user.select_one('age')
        print(name.text)
        print(age.text)
