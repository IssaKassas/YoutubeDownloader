
from tkinter import Button, Label, Tk

from sympy import Lambda

from method import downloadMedia


app = Tk()
app.geometry("400x300")

title = Label(
    app ,
    text = "Youtube Downloader",
    fg = "white",
    bg = "black",
    font = ('cortana' , 17 , 'bold')
)

title.place(x = 90 , y = 100)

mp3 = Button(
    app,
    text = "Download mp3",
    fg = "white",
    bg = "black",
    font = ('cortana' , 13 , 'bold'),
    command = lambda: downloadMedia("mp3")
)

mp4 = Button(
    app,
    text = "Download mp4",
    fg = "white",
    bg = "black",
    font = ('cortana' , 13 , 'bold'),
    command = lambda: downloadMedia("mp4")
)

mp3.place(x = 140 , y = 150)

mp4.place(x = 140 , y = 200)

app.mainloop()