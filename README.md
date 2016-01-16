# Digikey-Volume-Cost-Analysis

A script I wrote used to optimize BOM selection for small/medium run electronics projects according to anticipated product demand, using volume adjusted unit prices from DigiKey.

<h3>How to use:</h3>

In the text file named "URLs", write down the title for your component, followed by whitespace and then the url for the component search on Digikey. The Digikey URL has to be formatted with form information, so you must first customize your search using at least one parameter for the right formatting to be in place. The quantity must be set to zero.


<h3>Limitations:</h3>
<ul>
  <li>The "results per page" setting limits the number of results that will be contained in the csv. this can be fixed fairly easily</li>
</ul>
