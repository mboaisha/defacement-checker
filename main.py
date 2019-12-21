#!/usr/bin/env python3

#Imports the base csv reader library.
import csv
#Imports requests. Handles fetching web pages.
import requests
# BeautifulSoup library to parse web pages.
from bs4 import BeautifulSoup

#Initialize lists to store stuff.
bad_words_list = []
targets = []

#The sole purpose of this function is to populate the emply lists from CSV files.
def populate_list_csv(csvfile, emptyList):
	with open(csvfile) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			emptyList.append(row[0])

#Parse all the text from the website and put each word in a list.
def parse_site(url):
	print(url)

#Gather bad words
populate_list_csv("badwords.csv", bad_words_list)

#Gather targets
populate_list_csv("targets.csv", targets)

for x in range(len(targets)):

	pageResponse = requests.get("http://" + targets[x])
	pageContent = BeautifulSoup(pageResponse.content, "html.parser")
	print(pageContent)

