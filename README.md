# 16-ways-earn-money-online

This is an example of an application using the BeautifulSoup library. BeautifulSoup is a Python library that takes an HTML file or a string containing HTML code and transforms it into a tree of Python objects, making web scraping easier.
The goal here is to provide a scraping example using the library and export a list with the content. The choice of the webpage was made randomly, with the aim of having examples of information that can be listed in a tabular format. Other pages could be chosen, such as newspapers, gaming websites, or sites with political themes...
The specific website mentions 16 ways to generate extra income from the internet. The information is stored within the <div> element, where the subtitles are delimited in the descendants within <h3>, and the information about the subtitles is delimited between <p> elements.
In the file, the extraction of the HTML code is performed, then the correct div containing the information is located, the information is extracted, and finally, a list of tuples is created to organize them into a table. This table will be exported as a CSV file.
