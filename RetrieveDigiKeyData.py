from configparser import SafeConfigParser
import bs4 as BeautifulSoup
import pandas as pd
import numpy as np
import os
import re
import urllib

def requestURL(URL):
	if re.search("http://www.digikey", URL):
		urllib.request.urlopen(str(URL))
	else:
		raise Exception("URL for part " + str(Name) + " is Invalid")


def downloadCSV(name, URL, quantities):
	soup = BeautifulSoup(requestURL(URL), 'html.parser')
	if re.search("product-detail", URL):
	 	partID = soup.find("td", {"id": "reportPartNumber"}).contents[2].strip()
		quantityAvail = soup.find("td", {"id": "quantityAvailable"}).find(text=re.compile("Digi"))

		pd.DataFrame(columns = ['Digi-Key Part Number', 'Datasheet', 'Quantity Available', ]).to_csv('DigiKeyData/' + name + ".csv", index=False)


	if re.search("product-search", URL):
		URL = re.sub("/product-search/", "/product-search/download.csv?", URL)
		for j in range(0, len(quantities)):
			quantities[j] = "-quantity=" + quantities[j]
			quantityadjustedURL = downloadURL.replace("quantity=0", quantities[j])
			urllib.request.urlretrieve(quantityadjustedURL, "data/" + Name + quantities[j] + ".csv")

def main():
	pdf = pd.read_csv("DataIN/DigiKeyParts.csv")
	qdf = pd.read_csv("DataIN/Quantity.csv", squeeze=True)

	for i in range(0, len(pdf)):
		x = pdf.iloc[i].values
		y = x[2]*qdf
		try:
			downloadCSV(x[0], x[1], y.values)
		except:
			


if __name__ == '__main__':
	main()
