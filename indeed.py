import requests
import re
from bs4 import BeautifulSoup
from math import ceil

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")

  case = soup.find("div", {"id" : "searchCountPages"})
  case = str(case)
  case = case.replace(",","")
  numbers = re.findall("\d+", case)
  number = numbers[1]
  number= int(number)
  pages = (ceil(number/50))

  max_page = pages

  # links = pagination.find_all('b')
  # pages = []
  # for link in links :
  #     pages.append(int(link.String))

  # max_page = pages

  return max_page

def extract_indeed_jobs(last_page) :
  jobs = []
  for page in range(last_page) :
    result = requests.get(f"{URL}&start=(page*LIMIT")
    print(result.status_code)
  return jobs