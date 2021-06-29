# from urllib.request import urlopen #opens url library module
import unidecode                                                               #opens module for decoding and encoding text -  fixed ' to â€™ conversion when writing file to csv
import pickle 
import xlsxwriter
import requests
# import time
from bs4 import BeautifulSoup                                                  #imports BeautifulSoup web scraping module

with open('BOTWlist', 'rb') as zelda:                                          #opens pickled list of link 
    savedlinks = pickle.load(zelda)
    
print(savedlinks)
print(len(savedlinks))  

# Codeblock to remove erroneous links that haven't been removed when scraped
for link in savedlinks:
    if link.find('http://') or link.find('https://') == True:
        continue
    else:
        savedlinks.remove(link)
        continue
    
print(savedlinks)
print(len(savedlinks))


counter = 0                                                                    # Creates a count per link/article accessed
paragraphcounter = 0                                                           # Creates a count per paragraph in article
workbook   = xlsxwriter.Workbook('Breath of the Wild Reviews.xlsx')
worksheet1 = workbook.add_worksheet()

for link in savedlinks:
    print(link)
    print("counter =", counter)  
    if counter != 13: #and counter != 75:                                        #Identified as problematic articles so ignored by script
#    session = requests.Session()
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
        page = requests.get(link, headers=headers) 
#    print(page.text)
    
#    requests.get(link) 
        bsObj = BeautifulSoup(page.text, features="lxml")
#    print(bsObj)
        results = bsObj.find_all("p")                                          #finds all html tags on the website stored as <p> (paragraph)
        print(results)
    
    
#    result = bsObj.find("p") in link


    
#    worksheet2 = workbook.add_worksheet()

#    worksheet1.write('A1', 123)

    
#    exceldump = open("DSR3.csv","a", encoding="utf-8")                        #opens the file we want to write the pulled <p> tags to as text
        wholeparagraph = ''
        for potentialparagraph in results:                                     #for each paragraph, pull the text, decode the encoding and switch to utf-8, then print the text in the console
            paragraph = potentialparagraph.text
            paragraph = unidecode.unidecode(paragraph)
            print(paragraph)
            paragraphnew = (paragraph.replace(",", ";"))                       #replaces all of the commas in the text with semi-colons and writes this new specification of the output to the csv then close the file
#       wholeparagraph = wholeparagraph + paragraphnew
#       exceldump.write(paragraphnew)
            worksheet1.write(paragraphcounter, 0, paragraphnew)
            paragraphcounter += 1
#    exceldump.close()
#    if counter == 30:
#        break
     
    counter += 1
workbook.close()




























#    except "HTTPError: Forbidden":
#        print("HTTP Error Encountered, skipping to next entry")
#        continue
    
#        

##html = urlopen(, headers = {""}) #the website link we want to 
#        bsObj = BeautifulSoup(req.text, features="lxml")
#        result = bsObj.find("p")
#        results = bsObj.find_all("p") #finds all html tags on the website stored as <p> (paragraph)
#    exceldump = open("DSR3.csv","a", encoding="utf-8") #opens the file we want to write the pulled <p> tags to as text
##for result in results: #for each paragraph, pull the text, decode the encoding and switch to utf-8, then print the text in the console
#    paragraph = result.get_text()
#    paragraph = unidecode.unidecode(paragraph)
#    print(paragraph)
##    paragraphnew = (paragraph.replace(",", ";")) #replaces all of the commas in the text with semi-colons and writes this new specification of the output to the csv then close the file
##    exceldump.write(paragraphnew)
#exceldump.close()


    
    
#for result in results:
#    
#resultnew = (result.get_text().replace(",", ";"))
#output.write(resultnew)