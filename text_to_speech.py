import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = tk.Tk()
root.title('Text To Speech')
root.geometry('900x450+200+200')
root.resizable(False, False)
root.configure(bg='#305056')

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, tk.END)
    gender = gender_combobox.get()
    seed = speed_combobox.get()
    voice = engine.getProperty('voices')

    def set_voice():
        if (gender=='Male'):
            engine.setProperty('voice', voice[0].id)
            engine.say(text)
            engine.runAndWait()

        elif(gender=='Female'):
            engine.setProperty('voice', voice[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if (seed=='Fast'):
            engine.setProperty('rate', 250)
            set_voice()
        elif (seed=='Normal'):
            engine.setProperty('rate', 150)
            set_voice()
        else:
            engine.setProperty('rate', 60)
            set_voice()            

def download():
    text = text_area.get(1.0, tk.END)
    gender = gender_combobox.get()
    seed = speed_combobox.get()
    voice = engine.getProperty('voices')

    def set_voice():
        if (gender=='Male'):
            engine.setProperty('voice', voice[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

        elif(gender=='Female'):
            engine.setProperty('voice', voice[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if (text):
        if (seed=='Fast'):
            engine.setProperty('rate', 250)
            set_voice()
        elif (seed=='Normal'):
            engine.setProperty('rate', 150)
            set_voice()
        else:
            engine.setProperty('rate', 60)
            set_voice()            
               

# TOP FRAME
Top_frame = tk.Frame(root, bg='white', width=900, height=100)
Top_frame.place(x=0, y=0)

maike_img = tk.PhotoImage(file='maike.png')
tk.Label(Top_frame, image=maike_img, bg='white').place(x=10, y=10)

tk.Label(Top_frame, text='TEXT TO SPEECH', font='arial 20 bold', bg='white', fg='black').place(x=100, y=30)

# ===========
text_area = tk.Text(root, font='Roboto 20', bg='white', relief=tk.GROOVE, wrap=tk.WORD)
text_area.place(x=5, y=115, width=500, height=320)

tk.Label(root, text='VOICE', font="arial 15 bold", bg='#305056', fg='white').place(x=580, y=160)
tk.Label(root, text='SPEECH', font="arial 15 bold", bg='#305056', fg='white').place(x=760, y=160)


gender_combobox = Combobox(root, values=['Male', 'Female'], font='arial 14', state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font='arial 14', state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

speek_img = tk.PhotoImage(file='speek.png')
btn = tk.Button(root, text='Speech', compound=tk.LEFT, image=speek_img, width=130, font='arial 14 bold', command=speaknow)
btn.place(x=550, y=280)

save_img = tk.PhotoImage(file='svae.png')
save = tk.Button(root, text='Save', compound=tk.LEFT, width=130, bg='#39c790', image=save_img, font='arial 14 bold', command=download)
save.place(x=730, y=280)



root.mainloop()