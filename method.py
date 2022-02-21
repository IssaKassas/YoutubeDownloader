
from tkinter import Entry, Label, Toplevel , Button

def downloadMedia(text : str):
    root = Toplevel()
    root.geometry('400x300')
    
    title = Label(
        root,
        text = f"Download {text} file here",
        fg = "white",
        bg = "black",
        font = ('cortana' , 15 , 'italic')
    )
    title.place(x = 90 , y = 100)
    
    entryLink = Entry(
        root , 
        width = 22,
        font = ('arial' , 13)
    )
    
    entryLink.place(x = 90 , y = 150)
    # install py -3.10 -m pip install pytube
    from pytube import YouTube
    def youtubeDownloader():
        link = entryLink.get()
        video = YouTube(link)
        stream = video.streams
        if text == "mp3":
            stream = stream.get_audio_only()
        elif text == 'mp4':
            stream = stream.get_highest_resolution()
        stream.download()
    
    download = Button(
        root , 
        text = "Download",
        fg = "red",
        bg = "black",
        font = ('arial', 13 , 'bold' ),
        command = youtubeDownloader
    )
    download.place(x = 90 , y = 200)
    
    root.mainloop()