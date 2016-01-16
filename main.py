import pandas as pd
import os
import urllib

def downloadCSV(part, URL):
	downloadURL = URL.replace("http://www.digikey.ca/product-search/en?", "http://www.digikey.ca/product-search/download.csv?")
	quantities = ["quantity=1","quantity=5", "quantity=10", "quantity=25", "quantity=50", "quantity=100", "quantity=250", "quantity=500", "quantity=1000", "quantity=2000", "quantity=5000"]
	for j in range(0, len(quantities)):
		quantityadjustedURL = downloadURL.replace("quantity=0", quantities[j])
		urllib.request.urlretrieve(quantityadjustedURL, "data/" + part + quantities[j] + ".csv")
def main():

	file = open("URLs")
	list = file.read().split()
	for i in range(0, len(list) - 1, 2):
		downloadCSV(list[i], list[i+1])

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
