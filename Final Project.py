"""This program is a romance guide for the game "Stardew Valley"."""
__author__ = "Julia Sheldon"


# This guide will focus on three bachelorettes.
# I used the Stardew Valley Wiki page for character information.
# Wiki home page: https://stardewvalleywiki.com/Stardew_Valley_Wiki

# header
# def main function is the starting place for the program
def main():
    """ This main function is to signify the starting point of the program"""
    program_progression = True
    # this signifies that if the program is still running then it will continue
    print("Hello new user! Welcome to "
          "'The Stardew Valley Romance Guide: Bachelorette Addition'.")
    while program_progression:
        print("There are three bachelorettes to learn about in this "
              "program.\nMake a selection by typing either 1, 2, or 3.")
        # When selecting a bachelorette, you can find out specific information
        # The input being a number selection makes it more user
        # -friendly
        # \n creates a new line so it reads better + less print statements
        print("1.) Leah- Secret wood sculptor\n2.) Emily- Gemstone "
              "connoisseur\n3.) Maru- Accomplished engineer")
        # user inputs a number for the character they want to learn more about
        selection = int(input("Enter your selection here: "))
        if selection == 1:
            # After selecting Leah, the user is given four topics/ selections
            print("What would you like to know about Leah?\nSelect by "
                  "entering one of the four options.\n1.) birthday, "
                  "2.) gifts, 3.) favorite movie, or 4.) schedule: ")
            # user prompted to input selection
            answer = str(input())
            if answer == "1":
                print("Leah's birthday is on the 23th of the winter season.")
            elif answer == "2":
                print("Leah's favorite items: goat cheese, poppyseed muffin, "
                      "salad, stir fry, truffle, vegetable medley, and wine")
            elif answer == "3":
                print("Leah's favorite movie: Mysterium.")
                print("Don't forget, a girl usually "
                      "likes a snack at the movies!")
                print("She loves a good: "
                      "panzanella salad and stardrop sorbet")
            # Use if else statements to generate schedule
            elif answer == "4":
                print("On a normal day, Leah will be in different areas in "
                      "Pelican town.\nIf you wish to know where "
                      "you might find her during the day,\n"
                      "enter a number between 6 - 24.\n"
                      "The time inputs are based off a 24 hour clock, "
                      "starting at 6am.")
            # the time_stamp prompts the user to input a time, the input is
            # saved then finds that number in one of the list below,
            # then gives the information as a print statement for the user
            time_stamp = int(input("What time is it?: "))
            morning_list = [6, 7, 8]
            mid_morning_list = [9, 10, 11]
            afternoon_list = [12, 13, 14]
            late_afternoon_list = [15, 16, 17]
            evening_list = [18, 19]
            night_list = [20, 21, 22, 23]
            bed_time = [24]
            if time_stamp in morning_list:
                print("Leah can be found in her cottage, "
                      "her cottage is on the south side of Pelican town.\n"
                      "She will be in her room or kitchen.")
            elif time_stamp in mid_morning_list:
                print("Leah can be found in her cottage, her cottage is on "
                      "the south side of Pelican town.\n"
                      "She will be sculpting with driftwood.")
            elif time_stamp in afternoon_list:
                print("Leah can be found standing near the rive, "
                      "south of her cottage.")
            elif time_stamp in late_afternoon_list:
                print("Leah can be found in the forrest at the west side "
                      "of her cottage.\nWithin the forrest is "
                      "a pond with a pier.\n"
                      "She will be drawing on the end of the pier.")
            elif time_stamp in evening_list:
                print("Leah can be found in the forrest at the "
                      "west side of her cottage.\n"
                      "Within the forrest is a pond with a pier. She will be "
                      "spending her time around the pond in the forrest.\n"
                      "She walks back to her cottage by 7:30PM.")
            elif time_stamp in night_list:
                print("Leah can be found in her cottage, her cottage is on "
                      "the south side of Pelican town.\n"
                      "She will be reading books by her fire place.")
            elif time_stamp in bed_time:
                print("Leah can be found in her cottage, her cottage is on "
                      "the south side of Pelican town.\n"
                      "You can not visit her at this time, she is asleep.")

        elif selection == 2:
            print("What would you like to know about Emily?")
            print("Select by entering one of the four options.")
            print("1.) birthday, 2.) gifts, 3.) favorite movie, or 4.) "
                  "schedule: ")
            # user prompted to input selection
            answer = str(input())
            if answer == "1":
                print("Emily's birthday is on the 27th of the spring season.")
            elif answer == "2":
                print("Emily's favorite items: amethyst, aquamarine, cloth, "
                      "emerald, jade, ruby, survival burger, topaz, and wool")
            elif answer == "3":
                print("Leah's favorite movie: The Miracle At Coldstar Ranch.")
                print("Don't forget, a girl usually likes "
                      "a snack at the movies!")
                print("She loves a good: kale smoothie and stardrop sorbet")
            # if else statements to generate schedule
            elif answer == "4":
                print("On a normal day, Emily will be in different areas in "
                      "Pelican town.\nIf you wish to know where "
                      "you might find her during the day,\n"
                      "enter a number between 6 - 24.\n"
                      "The time inputs are based off a 24 hour clock, "
                      "starting at 6am.")
            # the time_stamp prompts the user to input a time, the input is
            # saved then finds that number in one of the list below,
            # then gives the information as a print statement for the user
            time_stamp = int(input("What time is it?: "))
            morning_list = [6, 7, 8, 9, 10, 11]
            afternoon_list = [12, 13, 14, 15]
            evening_list = [16, 17, 18, 19, 20, 21, 22, 23]
            bed_time = [24]
            if time_stamp in morning_list:
                print("Emily can be found in her home, "
                      "her house is found "
                      "south west of the town's plaza.\n"
                      "She will be in her room.")
            elif time_stamp in afternoon_list:
                print("Emily can be found in her home, "
                      "her house is found "
                      "south west of the town's plaza.\n"
                      "She will be in her sewing room making outfits.\n"
                      "By 3:30PM, "
                      "she will be heading to work at 'The "
                      "Stardrop Saloon', "
                      "the center of the town's plaza.")
            elif time_stamp in evening_list:
                print("Emily is currently working in "
                      "'The Stardrop Saloon', "
                      "which is found in the center of the town's plaza.")
            elif time_stamp in bed_time:
                print("You can not visit her at this time, "
                      "she is heading home to go to bed.")

        elif selection == 3:
            print("What would you like to know about Maru?")
            print("Select by entering one of the four options.")
            print("1.) birthday, 2.) gifts, 3.) favorite movie, or 4.) "
                  "schedule: ")
            # user prompted to input selection
            answer = str(input())
            if answer == "1":
                print("Maru's birthday is on the 10th of the summer season.")
            elif answer == "2":
                print("Maru's favorite items: battery pack, cauliflower, "
                      "diamond, gold bar, iridium bar, pepper poppers, "
                      "rhubarb pie, and strawberry")
            elif answer == "3":
                print("Maru's favorite movie: Natural Wonders: "
                      "Exploring Our Vibrant World.")
                print("Don't forget, a girl usually likes a "
                      "snack at the movies!")
                print("She loves a good: star cookie and stardrop sorbet")
            # If else statements to generate schedule
            elif answer == "4":
                print("On a normal day, Maru will be in different areas in "
                      "Pelican town.\nIf you wish to know where "
                      "you might find her during the day,\n"
                      "enter a number between 6 - 24.\n"
                      "The time inputs are based off a 24 hour clock, "
                      "starting at 6am.")
                # the time_stamp prompts the user to input a time, the input is
                # saved then finds that number in one of the list below,
                # then gives the information as a print statement for the user
                time_stamp = int(input("What time is it?: "))
                morning_list = [6, 7, 8, 9]
                afternoon_list = [10, 11, 12, 13]
                late_afternoon_list = [14, 15, 16, 17]
                evening_list = [18]
                night_list = [19, 20, 21]
                bed_time = [22]
                if time_stamp in morning_list:
                    print("Maru can be found in her home, "
                          "her house is on the north side of Pelican town.\n"
                          "She will be in her room.")
                elif time_stamp in afternoon_list:
                    print("Maru can be found in her home, her house is on "
                          "the north side of Pelican town.\n"
                          "She will be spending time in her father's lab.")
                elif time_stamp in late_afternoon_list:
                    print("Maru has left her house and is spending time "
                          "by the Community Center.")
                    print("The Community Center is found just north of "
                          "the town's plaza.")
                elif time_stamp in evening_list:
                    print("Maru is leaving the Community Center and "
                          "is walking home, "
                          "her house is on the north side of Pelican town.")
                elif time_stamp in night_list:
                    print("Maru can be found in her home, "
                          "her house is on the "
                          "north side of Pelican town.\n"
                          "She will be in her room.")
                elif time_stamp in bed_time:
                    print("Maru can be found in her home, "
                          "her house is on the "
                          "north side of Pelican town.\n"
                          "You can not visit her at this time, "
                          "she is asleep.")
        else:
            program_progression = False


main()
# this is where the program ends
