import sys
import os


def show_weather(city):
    os.system("curl wttr.in/" + city + "?1nF")


def check_param():
    if len(sys.argv) >=2:
        city = sys.argv[1]
        show_weather(city) if type(city) == str else print("ERROR! Please use a proper location name!")
    else:
        city = input("Please insert the location:")
        show_weather(city) if type(city) == str else print("ERROR! Please use a proper location name!")


if __name__ == '__main__':
    check_param()

