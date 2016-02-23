# Digikey-Volume-Cost-Analysis

A tool to aid in BOM decision making for electronics products. Automatically scrapes and outputs part data from DigiKey including price breaks for all packaging variants. Provides part selection suggestions in all else held equal situations where cost and part availability are the only factors. Allows for A|B comparison of design decisions.

<h2>Requirements</h2>
<ul>
<li>BeautifulSoup</li>
<li>Pandas</li>
<li>Numpy</li>
<li>Matplotlib</li>
</ul>

<h2>Scripts</h2>
<ul>
<li>GenCSVs.py             - produces the necessary CSV file templates for the user to fill in.</li>
<li>RetrieveDigiKeyData.py - retrieves data from the urls specified in the DigiKeyParts.csv file.</li>
<li>PartSelection.py       - finalize BOM based on cost and availability of candidate components</li>
<li>CVPAnalysis.py         - outputs CVP graph and table</li>
</ul>
<h2>Data</h2>
<ul>
<li>config.in	     - settings for the Scripts</li>
<li>DataIN	     - location of CSV template files</li>
<li>DigiKeyParts.csv - part list with URLs for digikey product or search pages</li>
<li>FixedCosts.csv   - non-variable costs</li>
<li>VarCosts.csv     - variable costs</li>
<li>Price.csv        - hypothetical product price points</li>
<li>Quantity.csv     - hypothetical quantities sold</li>
<li>DigiKeyData      - retrieved CSV files</li>
<li>DataOUT	     - finalized BOM and CVP tables</li>
</ul>
<h2>Directions</h2>

<ol>
<li>modify the configuration file according to your needs</li>
<li>run GenCSVs.py</li>
<li>Fill DataIN files with data</li>
<li>run RetrieveDigiKeyData.py</li>
<li>run PartSelection.py </li>
<li>run CVPAnalysis.py </li>
</ol>
