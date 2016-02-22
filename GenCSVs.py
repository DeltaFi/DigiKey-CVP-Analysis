from configparser import SafeConfigParser
import pandas as pd
import numpy as np
import math

def main():
	try:
		config = SafeConfigParser()
		if config.read('config.ini') != ['config.ini']:
			 raise OSError('no config.ini file present')

		if config.getboolean('Generate CSVs', 'autogen-q'):
			if config.get('Generate CSVs', 'type') == 'logarithmic':
				minQ = config.getint('Generate CSVs', 'min-q')
				maxQ = config.getint('Generate CSVs', 'max-q')
				numQ = config.getint('Generate CSVs', 'num-q')
				pd.Series(np.logspace(round(math.log(minQ, 10)), round(math.log(maxQ,10)), numQ, dtype=int)).to_csv('DataIN/Quantity.csv', index=False)
			if config.get('Generate CSVs', 'type') == 'linear':
				minQ = config.getint('Generate CSVs', 'min-q')
				maxQ = config.getint('Generate CSVs', 'max-q')
				numQ = config.getint('Generate CSVs', 'num-q')
				pd.Series(np.linspace(minQ, maxQ, numQ, dtype=int)).to_csv('DataIN/Quantity.csv', index=False)
			if config.get('Generate CSVs', 'type') == 'digikey':
				pd.Series([1,5,10,25,50,100,250,500,1000,5000,10000]).to_csv('DataIN/Quantity.csv', index=False)

		qs = pd.read_csv('DataIN/Quantity.csv', squeeze=True)

		titlesVarCost = ['Name']
		titlesDigiKey = ['Name', 'URL', 'Quantity']

		for i in range(0, len(qs)):
			titlesVarCost.append('Cost @' + str(qs.iloc[i]) + "pcs")

		if config.getboolean('Generate CSVs', 'gen-fc'):
			pd.DataFrame(columns = ['Name', 'Cost']).to_csv('DataIN/FixedCosts.csv', index=False)

		if config.getboolean('Generate CSVs', 'gen-dkp'):
			pd.DataFrame(columns = titlesDigiKey).to_csv('DataIN/DigiKeyParts.csv', index=False)

		if config.getboolean('Generate CSVs', 'gen-vc'):
			pd.DataFrame(columns = titlesVarCost).to_csv('DataIN/VarCosts.csv', index=False)

		if config.getboolean('Generate CSVs', 'gen-p'):
			pd.DataFrame(columns = ['Price']).to_csv('DataIN/Price.csv', index=False)

	except OSError as e:
		print(e)
	except:
		print("something went wrong, most likely your config.ini file is not properly configured")

if __name__ == '__main__':
	main()
