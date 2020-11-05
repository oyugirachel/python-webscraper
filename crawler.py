#Python program to scrape website  
#and save quotes from website 

# The first argument is the HTML tag you want to search and second argument is a dictionary type element to specify the additional attributes associated with that tag. find() method returns the first matching element. You can try to print table.prettify() to get a sense of what this piece of code does.

# Now, in the table element, one can notice that each quote is inside a div container whose class is quote. So, we iterate through each div container whose class is quote.
# Here, we use findAll() method which is similar to find method in terms of arguments but it returns a list of all matching elements. Each quote is now iterated using a variable called row.
import requests 
from bs4 import BeautifulSoup 
import csv 
   
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content, 'html5lib') 
   
quotes=[]  # a list to store quotes 
   
table = soup.find('div', attrs = {'id':'all_quotes'})  
   
for row in table.findAll('div', 
                         attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}): 
    quote = {} 
    #We create a dictionary to save all information about a quote. The nested structure can be accessed using dot notation. To access the text inside an HTML element, we use .text :
    quote['theme'] = row.h5.text 
    #We can add, remove, modify and access a tag’s attributes. This is done by treating the tag as a dictionary:
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quote['lines'] = row.img['alt'].split(" #")[0] 
    quote['author'] = row.img['alt'].split(" #")[1] 
    quotes.append(quote) 
    #Lastly, all the quotes are appended to the list called quotes
 #then we save all the data in the csv file  
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f: 
    w = csv.DictWriter(f,['theme','url','img','lines','author']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote) 

#Here we create a CSV file called inspirational_quotes.csv and save all the quotes in it for any further use.
