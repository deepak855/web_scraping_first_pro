import csv
import requests
from bs4 import BeautifulSoup
page = requests.get('https://kannadamoviesinfo.wordpress.com/movies/')
	soup = BeautifulSoup(page.text, 'html.parser')	
	for link in soup.find_all('a'):
		file=open("movies_page.csv",'a')
		data=(link.get('href'))	
		writer = csv.writer(file)
		writer.writerow([data])

for i in range(2,48):
	page = requests.get('https://kannadamoviesinfo.wordpress.com/movies'+str(i)+'/')
	soup = BeautifulSoup(page.text, 'html.parser')	
	for link in soup.find_all('a'):
		file=open("movies_page.csv",'a')
		data=(link.get('href'))	
		writer = csv.writer(file)
		writer.writerow([data])


