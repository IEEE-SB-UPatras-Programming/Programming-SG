from pytube import YouTube
from tkinter import*



main_download=Tk()
main_download.geometry("300x100")
main_download.title("YTdownloader")
main_download.configure(bg="red")




def get_it():
    url=url_entry.get()

    YouTube('{}'. format(url)).streams.first().download('downloaded_videos')

label_info1=Label(main_download,text="Paste here the video's URL",bg="red",fg="black").grid(row=0,column=1)



url_entry=Entry(main_download,width=50)
url_entry.grid(row=1,column=1)



get_the_video=Button(main_download,text="DOWNLOAD",bg="green",fg="red",width=15,height=2,command=get_it).grid(row=2,column=1)

main_download.mainloop()
