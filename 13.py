import requests
import re
from bs4 import BeautifulSoup

'''get page content'''
url = 'https://maktabkhooneh.org/plus/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

'''get title & tag'''
all_title = soup.find_all('div', attrs={'course-card__title'})
all_tag = soup.find_all('div', attrs={'course-card__badge--PLUS'})

'''output'''
pattern = r'\s+'
for title, tag in zip(all_title, all_tag):
    title_out = re.sub(pattern, ' ', title.text).strip()
    tag_out = re.sub(pattern, ' ', tag.text).strip()
    print(title_out, tag_out)


