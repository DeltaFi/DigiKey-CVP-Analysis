from configparser import SafeConfigParser
import pandas as pd
import numpy as np
import math

def main():
	config = SafeConfigParser()
	try:
		if config.read('config.ini') != ['config.ini']:
			 raise OSError('no config.ini file present')

		if config.getboolean('Generate CSVs', 'autogen quantity.csv'):
			if config.get('Generate CSVs', 'type') == 'logarithmic':
				minQ = config.getint('Generate CSVs', 'minquantity')
				maxQ = config.getint('Generate CSVs', 'maxquantity')
				numQ = config.getint('Generate CSVs', 'numquantities')
				pd.Series(np.logspace(round(math.log(minQ, 10)), round(math.log(maxQ,10)), numQ, dtype=int)).to_csv('DataIN/Quantity.csv', index=False)
			if config.get('Generate CSVs', 'type') == 'linear':
				minQ = config.getint('Generate CSVs', 'minquantity')
				maxQ = config.getint('Generate CSVs', 'maxquantity')
				numQ = config.getint('Generate CSVs', 'numquantities')
				pd.Series(np.linspace(minQ, maxQ, numQ, dtype=int)).to_csv('DataIN/Quantity.csv', index=False)
			if config.get('Generate CSVs', 'type') == 'digikey':
				pd.Series([1,5,10,25,50,100,250,500,1000,5000,10000]).to_csv('DataIN/Quantity.csv', index=False)

		qs = pd.read_csv('DataIN/Quantity.csv', squeeze=True)

		titlesVarCosts = ['Name']
		titlesDigiKey = ['Name', 'URL']
		for j in range(1, config.getint('Generate CSVs', 'initdependencies') + 1 ):
			titlesVarCosts.append('Dependency'+str(j))
			titlesDigiKey.append('Dependency'+str(j))
			titlesDigiKey.append('Quantity'+str(j))
			for i in range(0, len(qs)):
				titlesVarCosts.append('Cost @' + str(qs.iloc[i]) + 'pcs for D' + str(j))

		if config.getboolean('Generate CSVs', 'generate FixedCosts.csv'):
			pd.DataFrame(columns = ['Name', 'Cost']).to_csv('DataIN/FixedCosts.csv', index=False)

		if config.getboolean('Generate CSVs', 'generate VarCosts.csv'):
			pd.DataFrame(columns = titlesVarCosts).to_csv('DataIN/VarCosts.csv', index=False)

		if config.getboolean('Generate CSVs', 'generate DigiKeyParts.csv'):
			pd.DataFrame(columns = titlesDigiKey).to_csv('DataIN/DigiKeyParts.csv', index=False)

	except OSError as e:
		print(e)
	except:
		print("something went wrong, most likely your config.ini file is not properly configured")

if __name__ == '__main__':
	main()
