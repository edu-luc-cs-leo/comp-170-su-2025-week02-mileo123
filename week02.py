// Miles Gray
def greet(name):
    #def defines the fucntion which is greet
    return f"Hello {name}. How are you?"

print(greet("Miles"))

#friends
my_friends = ["Carl", "Vince", "Paul"]

#the list

def greet_friends(friend_list):
   for friend in friend_list:
       print(greet(friend))

greet_friends(my_friends)
