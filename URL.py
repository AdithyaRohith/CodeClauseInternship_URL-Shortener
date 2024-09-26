import random
import string

url_mapping = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

def shorten_url(long_url):
    if long_url in url_mapping:
        return url_mapping[long_url]
    short_url = generate_short_url()
    while short_url in url_mapping.values():
        short_url = generate_short_url()
    url_mapping[long_url] = short_url
    return short_url

def get_long_url(short_url):
    for long_url, short in url_mapping.items():
        if short == short_url:
            return long_url
    return None

long_url = input("Enter the long URL: ")
short_url = shorten_url(long_url)
print(f"Shortened URL: {short_url}")

retrieved_url = get_long_url(short_url)
print(f"Original URL: {retrieved_url}")
