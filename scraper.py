import time
from random import randrange
from facebook_scraper import get_posts
import csv

tmp=[]
def doSleep():
    sleep_time = randrange(30,90)
    print("Sleeping for ",sleep_time, " seconds.")
    time.sleep(sleep_time)



for post in get_posts('phnompenhpost', pages=10):
    print(post['text'])




# Comment these for continous scrapping:

# f = open('PPPostFBScrape.csv','a', encoding='UTF8')
# append = csv.writer(f) 
# append.writerow(["TITLE","LIKES","SHARES"])
# f.close()
    

# Alternate between these if no need to use your account's cookie:

# for post in get_posts('PhnomPenhPost', pages=500, cookies='cookie.txt'):
for post in get_posts('PhnomPenhPost', pages=500):

    #sleep to avoid getting temp banned by FB
    doSleep()
    f = open('PPPostFBScrape.csv','a', encoding='UTF8') #open csv with append moode
    append = csv.writer(f) #make writer var
    tmp=[] #Clear tmp


    post_title = post['post_text']
    likes = post['likes']
    shares = post['shares']
    print(post_title,'\n' ,likes,'\n',shares)

    tmp.append(post_title)
    tmp.append(likes)
    tmp.append(shares)
    
    append.writerow(tmp) #append csv
    f.close() #close file in case FB ban, result in losing data. 
        




