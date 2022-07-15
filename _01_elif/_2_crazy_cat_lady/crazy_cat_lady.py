from tkinter import simpledialog, messagebox, Tk
import webbrowser


# Use this function to play a video from the internet
def play_video(url):
    webbrowser.open(url)

# =================== DO NOT MODIFY THE CODE ABOVE ===========================


if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    answer=simpledialog.askstring(title='Question',prompt='How many cats do you have?')
    if int(answer) >=3:
        messagebox.showinfo(title='response',message='You are a crazy cat lady')
    elif int(answer) <3 and int(answer) >0:
        play_video('https://www.youtube.com/watch?v=NsUWXo8M7UA')
    elif int(answer) == 0:
        play_video('https://www.youtube.com/watch?v=ZJT9CeEhM10')






    # TODO 1) Make a new window variable, window = Tk()
    #      2) Hide the window using the window's .withdraw() method
    #      3) Ask the user how many cats they have
    #      4) If they have 3 or more cats, tell them they are a crazy cat lady
    #      5) If they have less than 3 cats AND more than 0 cats, call the
    #         play_video function below to show them a cat video
    #      6) If they have 0 cats, show them a video of A Frog Sitting on a
    #         Bench Like a Human

    pass
