import requests 
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL) 
print(r.content)
import requests 
from bs4 import BeautifulSoup 
  
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
print(soup.prettify()) 
#r.content is the raw html content
#html5lib specifies the parser to be used
##soup.prettify() is printed, it gives the visual representation of the parse tree created from the raw HTML content.