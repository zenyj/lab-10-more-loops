maximum_stories = 20
usernum = int(input("On what floor of the building is your office?:"))

while usernum > maximum_stories: 
    usernum=int(input("You entererd: " + str(usernum) + " but there are only " + str(maximum_stories) + " floors in this building:"))
    
print("Congrats! You work on floor: " + str(usernum))
