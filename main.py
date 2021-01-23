from weather_get import getWeather
import pyttsx3

def main(lang = "en"):
    # start speak engine, the voice is your system default
    engine = pyttsx3.init()
    weather_list = getWeather(lang)

    # create weather message
    if lang == "en":
        message = "The weather at " + str(weather_list[0]) + " is " + str(weather_list[-1]) + "." \
        " The current temperature is " + str(weather_list[2])+ " celsius" + "." +\
        " The current humidity is " + str(weather_list[1])+ "%" + "."

    else:
        message = "现在位于" + str(weather_list[0]) + "的天气是" + str(weather_list[-1]) + "。" \
        "现在的温度是" + str(weather_list[2])+ "摄氏度" + "。" +\
        "现在的相对湿度是" + "百分之" + str(weather_list[1])+ "。"

    # speak and reveal
    if lang == "en":
        print("Hello Admin!")
        engine.say("Hello Admin!") # you can custume your name here
        engine.runAndWait()
    else:
        print("你好，管理员!")
        engine.say("你好，管理员!")
        engine.runAndWait()

    engine.say(message)
    print(message)
    engine.runAndWait()

    return


# zh_cn is Chinese, en is for English
# You have to change your system speech setting accordingly
main(lang = "zh_cn")
