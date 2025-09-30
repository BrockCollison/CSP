import turtle as trtl

#Make list of months and seasons 
Months = ["January", "Feburary", "March", "April", "May","June","July", "August", "September","October", "November", "December"]
Seasons = ["Winter", "Spring","Summer","Fall"]


#Ask what season they want 
x = (input("Choose a month...")) #Enter a Month
x= x.capitalize()

if x not in Months:
        print("That's not a valid month, sorry.")

else:

 if x in ["October", "November", "September"]:
        Season_Ask = (input("Choose a season..."))
        Season_Ask = Season_Ask.capitalize()
        if Season_Ask == "Fall":
                print(f"{Season_Ask} is a nice season!")
        else:
                print("That's not a fall season...")

        
                
 elif x in ["June", "July", "August"]:
        Season_Ask = (input("Choose a season..."))
        Season_Ask = Season_Ask.capitalize()
        if Season_Ask == "Summer":
                print(f"{Season_Ask} is a nice season!")
        else:
                print("That's not a summer season...")


 elif x in ["November", "December", "January"]:
        Season_Ask = (input("Choose a season..."))
        Season_Ask = Season_Ask.capitalize()
        if Season_Ask == "Winter":
                print(f"{Season_Ask} is a nice season!")
        else:
                print("That's not a Winter season...")

 elif x in ["March", "Feburary", "April", "May"]:
        Season_Ask = (input("Choose a season..."))
        Season_Ask = Season_Ask.capitalize()
        if Season_Ask == "Spring":
                print(f"{Season_Ask} is a nice season!")
        else:
                print("That's not a Spring season...")

    
     
        



#Create different drawings based on the seasons



#Choose night of day 
wn = trtl.Screen()
wn.mainloop()