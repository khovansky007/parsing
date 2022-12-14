from requests import Session
from bs4 import BeautifulSoup
import lxml


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

cookies = Session()
cookies.get('https://quotes.toscrape.com/', headers = headers)
responce = cookies.get('https://quotes.toscrape.com/login', headers = headers)
soup = BeautifulSoup(responce.text, 'lxml')
tokenkey = soup.find('input').get('value')

data = { 
    'csrf_token': tokenkey,
    'username': 'admin',

}

cookies.post('https://quotes.toscrape.com/login', headers = headers, data = data, allow_redirects=True)

for x in range(10):
    url = 'https://quotes.toscrape.com/page/' + str(x) + '/'
    result = cookies.get(url, headers=headers, data=data, allow_redirects=True)
    soup1 = BeautifulSoup(result.text, 'lxml')
    for i in soup1.find_all(class_='quote'):
        with open('txt.txt', 'a') as file:
            file.write(i.find('span').text + '\n')
