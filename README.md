# keyword_extraction

Keyword Extraction from a single document using two different approaches.

1. Using simple tf-idf scores to find the keywords. In order to find the inverse document frequency, treated every page of the pdf as a separate document.

2. Using Rapid Automated Keyword Extraction (RAKE) algorithm which finds the candidate keywords and then score them based on the degree of every word in the document (much like in undirected graphs).

3. Results are saved in separate csv files.
