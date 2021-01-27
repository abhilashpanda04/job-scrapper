
#import all the libraries
import requests
import time
from bs4 import BeautifulSoup as bs

# take the input from the user
print('write unfamiliar skills')
unfamiliar_skills=input()
print(f'filtering the {unfamiliar_skills}')

# scrape the data from the website

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup=bs(html_text,'html.parser')
jobs=soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

# create a funtion that can create a doc writting inside it

def find_jobs():
    for index,job in enumerate(jobs):
        posted=job.find('span',class_='sim-posted').span.text
        if 'few' in posted:
            company=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            # print(company)
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            link_to_the_job_post=job.find('header','clearfix').h2.a['href']
            if unfamiliar_skills not in skills:
                with open('{index}.txt','w') as f:
                    f.write(f'''company name: {company.strip()}
                    skills: {skills.strip()}
                    published_date={posted.strip()}
                    link={link_to_the_job_post.strip()}''')
                print(f'file saved:{index}')
            # print(skills)
            # print(posted)

# used dunder method to make used of the function by creating an app saving it every 10 minutes

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'waiting time remaining {time_wait} seconds ')
        time.sleep(time_wait*60)











