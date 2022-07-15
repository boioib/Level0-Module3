from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window=Tk()
    window.withdraw()
    main_answer=simpledialog.askstring(title='Question', prompt='Are you happy?')
    if main_answer == ("yes"):
        messagebox.showinfo(message='Keep doing whatever you are doing')
    elif main_answer == ("no"):
        answer_2=simpledialog.askstring(title='Question', prompt='Do you want to be happy?')
        if answer_2 == ("no"):
            messagebox.showinfo(message='Keep doing whatever you are doing')
        elif answer_2 == ("yes"):
            messagebox.showinfo(message='Change something')







pass
