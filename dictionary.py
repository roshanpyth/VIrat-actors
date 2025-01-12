games={
    'cricket':"Cricket is a bat and ball game and one of the best players  is called Shivam Dube",
    'football': " This is a universal sport and is expanding on a global scale, a well-known player is Ronaldo",
    'wrestling': "Wrestling is sports entertainment and is very aggresive, a well known wrestler is the Great Khali" ,

}

#print (games)
user=input("Please enter game name!!!")
#this will print the user input
print(user)

#this will express the value the user has entered
print(games[user])
#b) create a new entery for volleyball in the dictionary.
games["volleyball"]= "Volleyball is a beach sport"
print (games)
# in this library you can create a new key value by doing the dictionary name["key"]="value"
# c) Change the descriptio of cricket in the abive dictionary.
games["cricket"]="The best player in cricket is Surya-Kumar-Yadav"
print (games)

#sorting
game=[]
for user in games: 
    game.append(user)
game.sort()
print(game)