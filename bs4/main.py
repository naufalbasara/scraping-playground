from bs4 import BeautifulSoup
import requests

# with open('home.html', 'r') as html_file:
#     content = html_file.read()
#     soup = BeautifulSoup(content, 'lxml')
#     courses = soup.find_all('div', class_='card')
#     for course in courses:
#         print(course.h5.text)
#         print(course.a.text)
#         print("------------")

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').content
soup = BeautifulSoup(html_text, 'lxml')
companies = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for data in companies:
    jobTitle = data.find('h2').text
    company = data.find('h3').text.split()
    print(f"""
    Job\t\t: {company[0]}
    Position\t: {jobTitle.strip()}
    """)