import requests
import bs4
import re

def request_page(web_direction=str):
    response = requests.get(web_direction)
    #print(response.text)
    #print(type(response))
    #print(type(response.text))
    soup = bs4.BeautifulSoup(response.text,'lxml')
    #print(soup)
    #print(type(soup))
    return soup

def get_author_names(soup=bs4.BeautifulSoup):
    author_names = []
    class_author = soup.select('.author')
    #print(class_author)
    #print(type(class_quote))
    #print(type(class_quote[0]))
    #print('-----------')
    #print(class_quote[0])
    #print(class_quote[0].attrs)
    #print(list(class_quote[0].children))
    #print(class_quote[0].select(".author"))
    #print(class_quote[0].text)
    for n in class_author:
        author_names.append(n.text)
    #return [*set(author_names)]
    return list(dict.fromkeys(author_names))

def get_quotes(soup=bs4.BeautifulSoup):
    quotes = []
    class_quote = soup.select('.text')
    for quote in class_quote:
        quotes.extend(quote)
    return list(dict.fromkeys(quotes))

def get_tags_top_ten(soup=bs4.BeautifulSoup):
    top_ten = []
    class_top_ten = soup.select('.col-md-4.tags-box')
    #print(type(soup))
    #print(type(class_top_ten))
    #print(type(class_top_ten[0]))
    #print(list(class_top_ten[0].children))
    childrens = list(class_top_ten[0].children)
    #print(childrens[1].text)
    #print(type(childrens[1]))
    #print('-----')
    for children in childrens:
        #print((children.text))
        re_serch = re.findall(r'[\w]+',children.text)
        #print(' '.join(re_serch))
        if re_serch != []:
                top_ten.append(' '.join(re_serch))
    top_ten.pop(0)
    return list(dict.fromkeys(top_ten))

def loop_pages(web_direction=str,stop=int):
    i=1
    j=0
    web_counter = ''
    all_authors = []
    while i < stop:
        web_counter = web_direction + str(i)
        print(f'{i}',end=' ',flush=True)
        try:
            soup = request_page(web_counter)
            authors_names = get_author_names(soup)
            if authors_names == []:
                 raise ValueError('There is no value on the page:', i, j, web_counter)
        except ValueError as err:
            j += 1
            print('')
            print(err.args)
            if j > 1:
                break
        except:
            print(f'\nThe requested direction dont work: \n{web_counter}')
            break
        all_authors.extend(authors_names)
        i += 1
        
    return list(dict.fromkeys(all_authors)), i-j
     
    



web_direction = 'http://quotes.toscrape.com/page/'
#authors_names = get_author_names(request_page(web_direction))
#print(authors_names)
#quotes = get_quotes(request_page(web_direction))
#print(quotes)
#top_ten = get_tags_top_ten(request_page(web_direction))
#print(top_ten)

all_authors,pages = loop_pages(web_direction,20)
print(f'\nThe authors on all the "{pages}" pages are:\n')
print(all_authors)
