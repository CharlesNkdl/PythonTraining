import requests
from bs4 import BeautifulSoup

def scrape_all(url, headers, base_url, all_links):
	try:
		response = requests.get(url, headers=headers)
		if (response.status_code == 200):
			soup = BeautifulSoup(response.text, "html.parser")
			for link in soup.find_all('a', href=True):
				absolute_url = link['href']
				if (absolute_url.startswith('/') or absolute_url.startswith('#')):
					absolute_url = base_url + absolute_url
				if (absolute_url not in all_links):
					all_links.append(absolute_url)
	except Exception as e:
		print(f"Error: {e} , lors {url}")

def scrap_and_save(url, headers, output):
	r = requests.get(url, headers=headers)
	if r.status_code == 200:
		soup = BeautifulSoup(r.text, "html.parser")
		text = soup.get_text()
		clean = ' '.join(text.split())
		with open(output, "a") as f:
			f.write(clean + "\n")
	else:
		print("Error: " + str(r.status_code))
		exit()
