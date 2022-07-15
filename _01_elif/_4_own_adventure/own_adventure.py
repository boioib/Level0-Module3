from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    answer_1=simpledialog.askstring(title='Story', prompt='You are walking in the middle of a highway in the middle of nowhere,\n'
                                                          'suddenly a UFO hovers above you and summons 100 donkeys, you are now\n'
                                                          'running for your life and two exits are in front of you.\n'
                                                          'Exit 1 has a nearby gas station where you can hide and exit 2 has a major city in the next 2 miles.\n'
                                                          'Which exit will you take? ')
    if answer_1==('exit 1'):
        answer_2=simpledialog.askstring(title='Story', prompt='You dash to the convenience shop and hide, the donkeys\n'
                                                              'were at full speed behind you the entire time and burst through the store walls.\n'
                                                              'You are now surfing on top of 100 raging donkeys and they are heading towards a deep canyon\n'
                                                              'and you can either surf your way off of the donkeys or fall off of the donkeys and get ran over by 20 others.\n'
                                                              'surf away or fall off?')
    elif answer_1==('exit 2'):
        answer_2=simpledialog.askstring(title='Story',prompt='You are now sprinting with all your power to get to the city. Halfway to the city you collapse out of exhaustion\n'
                                                             'and get ran over by all of the donkeys. Search and rescue finds you and picks you up. They give you 2 options for your treatment.\n'
                                                             'You can either spend almost all of your savings to recover or be put into a coma for 5 years to recover for free.\n'
                                                             'spend or coma?')
    if answer_2==('surf away'):
        messagebox.showinfo(title='Result', message='You surf your way to the end of the donkeys and they are just about to fall off the canyon.\n'
                                                    'You leap as the last donkey jumps into the canyon. You grab onto the ledge but 1 of your hands have already slipped off.\n'
                                                    'You are now hanging off a cliff until the same UFO hovers over you and pulls you into it. The simulation ends and you wake up\n'
                                                    'to a dozen scientists with notebooks. They were observing what a human would do when put into certain situations.')
    elif answer_2==('fall off'):
        messagebox.showinfo(title='Result', message='You fall off of the donkey you are on and get ran over by the donkeys near the end. You are killed instantly to a neck injury.\n'
                                                    'The UFO picks up your body and brings you to their planet. They bury you as the 74th human to be brought to their planet.\n'
                                                    'pretty lame way to die in my opinion.')
    elif answer_2==('spend'):
        messagebox.showinfo(title='Result', message='You are left with a hundred bucks and decide to test your luck at the casino. You decide you will spend it all on slots.\n'
                                                    'You have spent 90 dollars so far and have lost all hope. Slot 1 rolls a 7 followed by slot 2. You are now at the edge\n'
                                                    'of you seat and watching as slot 3 rolls another 7. You have just won the jackpot of $752,670.\n'
                                                    'You are now rich and living your best life in a long while. Very lucky I would say.')
    elif answer_2==('coma'):
        messagebox.showinfo(title='Result', message='You are left in darkness as everybody you ever knew forgets about you. You are abandoned in the hospital as the hospital\n'
                                                    'gets abandoned itself. You are preserved until the year 2465. You wake up in your capsule in Mars. There is an entire civilization\n'
                                                    'and you are put to work at a greenhouse. You are now living in the future on a completely different planet.')




