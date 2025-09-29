# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    _user_height_feetinch = input("What is your height in feet and inches, separated by a ,?")
    user_height_feetinch = _user_height_feetinch.split(",")
    user_height_inches = (int(user_height_feetinch[0]) * 12) + int(user_height_feetinch[1])
    print(user_height_inches)
    _neighbour1_height_feetinch = input("What is your neighbours height in feet and inches, separated by a ,?")
    neighbour1_height_feetinch = _neighbour1_height_feetinch.split(",")
    neighbour1_height_inches = (int(neighbour1_height_feetinch[0]) * 12) +int(neighbour1_height_feetinch[1])
    print(neighbour1_height_inches)
    _neighbour2_height_feetinch = input("What is your neighbours height in feet and inches, separated by a ,?")

    neighbour2_height_feetinch = _neighbour2_height_feetinch.split(",")
    neighbour2_height_inches = (int(neighbour2_height_feetinch[0]) * 12) + int(neighbour2_height_feetinch[1])
    print(neighbour1_height_inches)
    average_height_inches = (user_height_inches+neighbour1_height_inches+neighbour2_height_inches)/3


    print("The average height of your and your neighbours is " + str(int(average_height_inches//12)) + f" feet and {average_height_inches%12:.2f} inches")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
