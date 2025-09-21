import requests
from concurrent.futures import ThreadPoolExecutor

# sample_url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(sample_url)
# data = response.json()
# # print(data[0])

# def process_data(data):
#     for record in data[:5]:
#         print(record)

# process_data(data)

## Requests with threads
sample_urls = [
    "https://jsonplaceholder.typicode.com/posts",
    # Add more URLs if needed
]

def fetch_and_process(url):
    response = requests.get(url)
    data = response.json()
    for record in data[:5]:
        print(record)

with ThreadPoolExecutor(max_workers=len(sample_urls)) as executor:
    futures = [
        executor.submit(fetch_and_process, url)
        for url in sample_urls
    ]