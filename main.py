from weather_get import getWeather
import pyttsx3

def main():

    # start speak engine, the voice is your system default
    engine = pyttsx3.init()
    weather_list = getWeather()

    # create weather message
    message = "The weather at " + str(weather_list[0]) + " is " + str(weather_list[-1]) + "." \
    " The current temperature is " + str(weather_list[2])+ " celsius" + "." +\
    " The current humidity is " + str(weather_list[1])+ "%" + "."

    # speak and reveal
    engine.say("Hello Admin") # you can custume your name here
    engine.runAndWait()
    engine.say(message)
    print(message)
    engine.runAndWait()

    return

main()
