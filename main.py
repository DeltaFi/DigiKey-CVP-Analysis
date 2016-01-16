import pandas as pd
import os
import re
import urllib

def downloadCSV(part, quantityString, URL):
	quantities = quantityString.split(",")
	downloadURL = re.sub("/product-search/[^ \t\n\r\f\v]*\?", "/product-search/download.csv?", URL)
	for j in range(0, len(quantities)):
		quantities[j] = "-quantity=" + quantities[j]
		quantityadjustedURL = downloadURL.replace("quantity=0", quantities[j])
		urllib.request.urlretrieve(quantityadjustedURL, "data/" + part + quantities[j] + ".csv")

def main():
	file = open("URLs")
	list = file.read().split()
	for i in range(0, len(list) - 2, 3):
		downloadCSV(list[i], list[i+1], list[i+2])

'''
	mdf = pd.read_csv("data/2.csv")
	mdfi = mdf.set_index(["Digi-Key Part Number"])
	for file in os.listdir("data"):
		if file.endswith("0.csv"):
			df = pd.read_csv("data/" + file)
			dfi = df.set_index(["Digi-Key Part Number"])
			dfi = dfi.rename(columns={'Unit Price (CAD)': file})
			mdfi = mdfi.join(dfi[8])

	print(dfm)
'''

if __name__ == '__main__':
	main()
