import time
import tweepy

C_KEY="Put your Consumer API Key  here"
C_SECRET="Put your Consumer API Secret Key  here"
A_TOKEN="Put your Access Token   here"
A_TOKEN_SECRET="Put your Access Token Secret here"

print("Twitter developer basics")
print("\n")
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

#Get your twitter handle name

current_user=api.me()
print("current user: ", current_user.screen_name)
print("\n")

#Update twitter status

#new_status=api.update_status("Every day is a chance to begin again")
print("Your latest tweet is posted",)



#Get the list of users you follow

print("--------------------following-------------------\n")
user = api.get_user("Sowmya0602")
fr =[f.id for f in user.friends()]
size=(len(fr))
for i in range(0,size):
 u = api.get_user(fr[i])
 print("the_user_id:",fr[i])
 print("screen_name:",u.screen_name)
 print("\n")

#Get the list of users following you

print("--------------------followers-------------------\n")
user = api.get_user("Sowmya0602")
fr =[f.id for f in user.followers()]
size=(len(fr))
for i in range(0,size):
 u = api.get_user(fr[i])

 print("the_user_id:",fr[i])
 print("screen_name:",u.screen_name)
 print("\n")

#Get the list of your tweets

print("--------------------Recent tweets-------------------\n")
#you can change the screen name to any user and get their recent tweets
tweets = api.user_timeline(screen_name="BillGates",
                           count=10,
                           include_rts = False,
                           tweet_mode = 'extended'
                           )
for info in tweets:
    print("Tweet Id: {}".format(info.id))
    print(info.created_at)
    print(info.full_text)
    print("\n")




