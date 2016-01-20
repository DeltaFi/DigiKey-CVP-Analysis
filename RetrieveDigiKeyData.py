from configparser import SafeConfigParser
import pandas as pd
import numpy as np
import os
import re
import urllib

def downloadCSV(Name, quantityString, URL):
	downloadURL = re.sub("/product-search/[^ \t\n\r\f\v]*\?", "/product-search/download.csv?", URL)
	for j in range(0, len(quantities)):
		quantities[j] = "-quantity=" + quantities[j]
		quantityadjustedURL = downloadURL.replace("quantity=0", quantities[j])
		urllib.request.urlretrieve(quantityadjustedURL, "data/" + Name + quantities[j] + ".csv")

def main():
	partsdf = pd.read_csv("DataIN/DigiKeyParts.csv")
	quantitydf = pd.read_csv("DataIN/Quantity.csv", squeeze=True)

	for i in range(0, len(partsdf)):

		downloadCSV(partsdf['Name'], partsdf[''], parts[i+2])


if __name__ == '__main__':
	main()
