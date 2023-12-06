import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from collections import Counter
import allsite
import os
from sys import argv

if len(argv) != 2:
	print("Usage: python manip_txt.py <url>")
	exit(1)
base_url = argv[1]
all_links = [base_url]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
output = os.getcwd() + "/output.txt"
nltk.download('punkt')
with open(output, "w") as f:
    f.write("")
allsite.scrape_all(base_url, headers, base_url, all_links)
for link in all_links[:30]:
	allsite.scrap_and_save(link, headers, output)

with open('output.txt', 'r', encoding='utf-8') as file:
    text = file.read()

custom_stop_words = ["les", ",", "le", "la", "'", ":", "?", "’", "''", "``", ".", "...", "-", "+", "!", "\"", "a", "quel", "quels", "quelle", "quelles", "plus", "pas", "cette", "cet" , "cela", "&", "(", ")", "un", "une", "d'un", "h/fl'industrie", "/"]
stop_words = set(stopwords.words('french'))
stop_words.update(custom_stop_words)

words = word_tokenize(text)

filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
word_count = len(words)
word_freq = FreqDist(filtered_words)
most_common_words = word_freq.most_common(50)
common_words, frequencies = zip(*most_common_words)

plt.figure(figsize=(30, 6))
plt.bar(common_words, frequencies)
plt.title('Mots les plus fréquents')
plt.xlabel('Mots')
plt.ylabel('Fréquence')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('figure.png')

print(f"Nombre total de mots : {word_count}")
print("Mots les plus fréquents (sans mots d'arret):")
for word, freq in most_common_words:
    print(f"{word}: {freq}")
