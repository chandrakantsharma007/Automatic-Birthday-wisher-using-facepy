
from facepy import GraphAPI
import time
import random
k=0
# token u have to generate for your own profile.
token =''
ck   = GraphAPI(token)
friend_list = ck.get("me/friends?fields=birthday,name")
print(friend_list)

birthday_wishes = ["Happy birthday yr,may god bless u :) ",
                   "Wish u very Happy Birthday ,party hard ,keep smiling :) ",
                   "Happy Birthday Bhai ,stay blessed :) ",
                   "Happy Birthday to you :) "]

localtime = time.localtime(time.time())
print(localtime)
month_day = [localtime[1], localtime[2]]

for friend in friend_list['data']:

    if 'birthday' in friend:
        bday = friend['birthday'].split('/')
        if int(bday[0]) == month_day[0] and int(bday[1]) == month_day[1]:
            print(friend['name'])
            bday_wish = birthday_wishes[random.randint(0, 3)]
            ck.post(friend['id'] + '/feed', 0, message=bday_wish)
            print("wished " + friend['name'])
            k=1

if k==0:
 print("sorry! no birthday for today")





