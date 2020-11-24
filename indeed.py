import requests
from bs4 import BeautifulSoup

job = "python"
limit = 50
url = f"https://www.indeed.com/jobs?q={job}&limit={limit}"

def extract_page():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find('ul', class_='pagination-list')
    links = pagination.find_all('a')

    pages = []

    for link in links[:-1]:
        pages.append(int(link.find('span').string))

    max_page = pages[-1]
    return max_page

def extract_job(result):
    title = result.find('h2', class_="title").find('a')['title']
    company = result.find('span', class_="company")
    company_anchor = company.find('a')
    if company_anchor is not None:
        company = company_anchor.string
    else:
        company = company.string.strip()
    location = result.find('span', class_="location")
    if location is not None:
        location = location.string
    job_id = result['data-jk']
    return {
        'title': title,
        'company': company,
        'location': location,
        'job-id': f"https://www.indeed.com/viewjob?jk={job_id}"
    }

def extract_jobs(lastpage):
    jobs = []
    for page in range(lastpage):
        print(f"scrapping page: {page}")
        result = requests.get(f"{url}&start={page*limit}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all('div', class_='jobsearch-SerpJobCard')
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    lastpage = extract_page()
    jobs = extract_jobs(lastpage)
    print (jobs)

get_jobs()