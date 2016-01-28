from bs4 import BeautifulSoup
import pandas as pd
import re
import urllib

def recursiveTest(URL, URLlist, df, xmax):
	URLlist.append(URL)
	soup = BeautifulSoup(urllib.request.urlopen(str(URL)), 'html.parser')
	for link in soup.find_all(href=re.compile("http://www.digikey.")):
		x = 0
		newURL = link.get('href')
		for i in URLlist:
			if newURL == i:
				x = 1

		if (len(df) < xmax) and (x == 0):
			print(link.get('href'))
			recursiveTest(newURL, URLlist, df, xmax)

	if re.search("product-detail", URL):
		partID = soup.find("td", {"id": "reportPartNumber"}).contents[2].strip()
		quantityAvail = soup.find("td", {"id": "quantityAvailable"}).find(text=re.compile("Digi"))
		entry = [partID, quantityAvail]
		df.append(entry)

def main():

	xmax = 10
	df = pd.DataFrame(columns = ['partID', 'quantityAvailable'])
	URLlist = []
	recursiveTest("http://www.digikey.com",URLlist, df, xmax)
	df.to_csv('testscraperobustness.csv', index=False)
if __name__ == '__main__':
	main()
