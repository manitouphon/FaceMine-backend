import time
from random import randrange
from facebook_scraper import get_posts
import csv

tmp=[]



for post in get_posts('PhnomPenhPost', pages=500, cookies='cookie.txt'):
    f = open('PPPostFBScrape.csv','a', encoding='UTF8') #open csv with append moode
    append = csv.writer(f) #make writer var
    tmp=[] #Clear tmp

    time.sleep(randrange(30,60)) #sleep to avoid getting temp banned by FB

    post_title = post['post_text']
    likes = post['likes']
    shares = post['shares']
    print(post_title,'\n' ,likes,'\n',shares)

    tmp.append(post_title)
    tmp.append(likes)
    tmp.append(shares)
    
    append.writerow(tmp) #append csv
    f.close() #close file in case FB ban, result in losing data. 
        




