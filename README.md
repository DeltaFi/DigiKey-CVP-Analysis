# Digikey-Volume-Cost-Analysis

A tool to aid in BOM decision making for electronics products. Automatically scrapes and outputs part data from DigiKey including price breaks for all packaging variants. Provides part selection suggestions in all else held equal situations where cost and part availability are the only factors. Allows for A|B comparison of design decisions.

<h2>Scripts</h2>
GenCSVs.py             - produces the necessary CSV file templates for the user to fill in.
RetrieveDigiKeyData.py - retrieves data from the urls specified in the DigiKeyParts.csv file.
PartSelection.py       - finalize BOM based on cost and availability of candidate components
CVPAnalysis.py         - outputs CVP graph and table

<h2>Data</h2>
config.ini  - settings for the Scripts
DataIN      - location of CSV template files
  DigiKeyParts.csv - part list with URLs for digikey product or search pages
	FixedCosts.csv   - non-variable costs
	VarCosts.csv     - variable costs
	Price.csv        - hypothetical product price points
  Quantity.csv     - hypothetical quantities sold
DigiKeyData - retrieved CSV files
DataOUT     - finalized BOM and CVP tables

<h2>Directions</h2>

<ol>
<li>modify the configuration file according to your needs</li>
<li>run GenCSVs.py</li>
<li>Fill DataIN files with data</li>
<li>run RetrieveDigiKeyData.py</li>
<li>run PartSelection.py </li>
<li>run CVPAnalysis.py </li>
</ol>
