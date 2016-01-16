# Digikey-Volume-Cost-Analysis

A script I wrote used to optimize BOM selection for small/medium run electronics projects according to anticipated product demand, using volume adjusted unit prices from DigiKey. 

<h3>How to use:</h3>

In the text file named "URLs", write down the title for your component, followed by whitespace and then the url for the component search on Digikey. The Digikey URL has to be formatted with form information, so you must first customize your search using at least one parameter for the right formatting to be in place. The quantity must be set to zero. 


<h3>Limitations:</h3>
<ul>
  <li>The "results per page" setting limits the number of results that will be contained in the csv. this can be fixed fairly easily</li>
  <li>the quantities that data is collected for are hardcoded. they are; 1,5,10,25,50,100,250,500,1000,2000,5000.</li>
  <li>the url strings are hardcoded for the canadian website, in english. Again, this could also be easily improved upon</li>
</ul>
