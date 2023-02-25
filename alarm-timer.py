from playsound import playsound
import time
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(sec):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < sec:
        time.sleep(1)
        time_elapsed += 1
        time_left = sec - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"{CLEAR_AND_RETURN}Alarm will start in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("sound.mp3")


def get_input(text):
    user_input = input(text) or '0'
    while not user_input.isdigit():
        print("Enter a number!")
        user_input = input(text) or '0'
    return int(user_input)


if __name__== "__main__":
    minutes = get_input("Enter minutes to wait: ")
    seconds = get_input("Enter seconds to wait: ")
    total_seconds = minutes * 60 + seconds
    alarm(total_seconds)





