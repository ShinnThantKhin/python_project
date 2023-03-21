songList=["Good Day","Going Crazy","Love Scenario","Attention","Love Dive","Next Level","Shut Down","Gee","Tell Me","Really Really","Clap","Gashina","Give Love","Fine","Rollin"]
descriptionList=["Artist:IU, Album:REAL, Year:2010",
                 "Artist:TREASURE, Album:THE FIRST STEP:TREASURE EFFECT, Year:2021",
                 "Artist:iKON, Album:Return, Year:2018",
                 "Artist:NewJeans, Album:New Jeans, Year:2022",
                 "Artist:IVE, Album:LOVE DIVE, Year:2022",
                 "Artist:aespa, Album:Next Level, Year:2021",
                 "Artist:BLACKPINK, Album:BORN PINK, Year:2022",
                 "Artist:Girls' Generation, Album:Gee, Year:2009",
                 "Artist:Wonder Girls, Album:2 Different Tears, Year:2010",
                 "Artist:WINNER, Album:FATE NUMBER FOR, Year:2017",
                 "Artist:SEVENTEEN, Album:TEEN,AGE, Year:2017",
                 "Artist:SUNMI, Album:Gashina, Year:2017",
                 "Artist:AKMU, Album:PLAY, Year:2014",
                 "Artist:TAEYEON, Album:My Voice, Year:2017",
                 "Artist:Brave Girls, Album:Rollin, Year:2017"]
intro="This is My Favorite Song List. This program will recommend you to some kpop songs with details.\n"
print(intro)

def song():
    sh1="Song List"
    sh2="="*60
    print(sh1)
    print(sh2)
    no=1
    for i in songList:
            print(no, i)
            no+=1
    print(sh2)



    choice=input("Enter the number of song you would like to know about : ")
    print("\n")

    if choice.isdigit():
        choice=int(choice)
        if choice>=1 and choice<=15:
            print(choice, songList[choice-1])
            print(descriptionList[choice-1])

        else:
            print("Invalid Number! The Number should be between 1 and 15.")
    else:
        print("Worng Input! It must be number between 1 and 15.")

song()

while (True):
    print("\n")
    quit=input("Do you like to quit? y/n:")

    print("\n")
    if quit=="y":
        l=10
        for k in range(1,11):
            print("!"*l,"BYE","!"*l)
            l-=1
        break
    elif quit=="n":
        song()
    else:
        print("Invalid input! Please only enter 'y' or 'n'.")
            

        
    

        



    
