import urllib3
import unicodedata
from bs4 import BeautifulSoup
import pandas

#Código begins trying to link to web site below
url = 'https://time.com/personal-finance/article/how-to-make-money-online/'
file_html_txt = 'html-to-txt.txt

http = urllib3.PoolManager()
web_modifier = http.request("GET", url, 
                            preload_content = False)                  
web_modifier.auto_close = False
binary = web_modifier.read()
conversor = binary.decode('utf-8')

# Avoinding error charmap unicodedata.
# First attempt was iowrapper enconding utf-8, but error persisted.
conversor = unicodedata.normalize('NFKD', conversor).encode('ascii', 'ignore').decode('utf-8')
with open(file_html_txt,'w') as file_handle:
        file_handle.write(conversor)
web_modifier.close()
       
     
# Scraping information from html file with beautifulsoup lib
file_h =  open('path/to/file.txt', 'r')
soup = BeautifulSoup(file_h,'html.parser')
file_h.close()
# Cathing the especific <div> with comments i want. First identified in html file.
# Then tried taking it from here.
class_especific_in_div = "mdx-styled-renderer___StyledDiv-sc-1khx60n-0 eQvyMj main___\
StyledStyledMDXRenderer-sc-1ql5noe-1 kcKaXX"
class_especific_in_div = class_especific_in_div.split(' ')
length_class = len(class_especific_in_div) # len = 4


def tracking_div(anyList): # Method to find the right <div>
    for div in anyList:
        try: # If a div has no class, skip it.
            class_in = div['class'] 
        except:
            continue
        counts = 0
        for strings in class_in:
            if (strings in class_especific_in_div) == True:
                counts += 1
                if counts == length_class:
                    return div
            else:
                break
    return False 

def flip(coin_face): # method to shift what i should append in list.
    if coin_face == '<h3>':
        return '<p>'
    else:
        return '<h3>'
    
divs = soup.find_all('div') # List of <div>s
matched_div = tracking_div(divs)

get_content_lst = []
turn = '<h3>'
max_content_web = 32

for child in matched_div.descendants: # All elements inside this <div>
    if turn in str(child):
        get_content_lst.append(child.get_text()) # Getting the content
        turn = flip(turn)
        if len(get_content_lst) == max_content_web:
            break

row_csv = []
for index in range(0,len(get_content_lst),2): # Organizing a list of tuples
    row_csv.append((get_content_lst[index],get_content_lst[index+1]))
    
    
df = pandas.DataFrame(row_csv, 
                      columns = ['Way to win','Description'])
df.to_csv('ways_to_win_money_online.csv',index = True, encoding = 'utf-8')
