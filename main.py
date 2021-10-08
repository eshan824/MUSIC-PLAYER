from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import Image, ImageTk

mixer.init()
root = Tk()
root.geometry("450x500")
root.resizable(0,0)
root.title("MUSIC PLAYER")
root.iconbitmap("E:/PROJECTS/PYTHON PROJECTS/GUI MP3 PLAYER/MP3-PLAYER[can browse .mp3 files]/MAIN CODE FILE/data/musicplayericon.ico")
root.config(background="black")

def add_playlist_song ():
    file = open("E:/PROJECTS/PYTHON PROJECTS/GUI MP3 PLAYER/MP3-PLAYER[can browse .mp3 files]/MAIN CODE FILE/playlist/PLAYLIST1.txt","r")
    file = file.read()
    file = file.split("\n")
    for x in file:
        x = x.split("/")
        for x in x:
            if x.find(".mp3") != -1:
                playlist.insert(END,x)


def add_song ():
    file = filedialog.askopenfilenames()
    file1 = []
    for x in file:
        x = x.split("\n")
        file1.append(x)
    file2 = []
    for x in file1:
        for x in x:
            x = x.split("/")
            file2.append(x)
    file3 = []
    i=0
    for x in file2:
        for x in x:
            if x.find(".mp3") != -1:
                file3.append(x)
                playlist.insert(END, x)
        i += 1
    k = 0
    for x in file:
        if x.find(file3[k]) != -1:
            print(x)
        k += 1
    file_ = open("E:/PROJECTS/PYTHON PROJECTS/GUI MP3 PLAYER/MP3-PLAYER[can browse .mp3 files]/MAIN CODE FILE/playlist/PLAYLIST1.txt","w")
    for x in file:
        file_.write(f"{x}\n")
        

#SCROLLBAR & LISTBOX INITIALIZATION & CONTROL
scrollbar = Scrollbar(root, background="yellow"
        ,activebackground="pink")
scrollbar.pack(side = RIGHT, fill = 'y')
scrollbar1 = Scrollbar(root, background="black", orient=HORIZONTAL)
scrollbar1.pack(side = BOTTOM, fill = 'x')
playlist = Listbox(root, yscrollcommand= scrollbar.set, xscrollcommand= scrollbar1.set
                , background="purple", borderwidth=3, cursor="circle"
                ,foreground="gold", font="timesnewroman 10 italic", highlightbackground="pink"
                , highlightcolor="red", relief = GROOVE ,selectbackground= "purple"
                , selectforeground= "orange")
playlist.pack(ipadx=150, ipady = 50, pady = 10, padx=20)
scrollbar.config(command= playlist.yview)
scrollbar1.config(command= playlist.xview)


def play_(event):
    song = playlist.get(ACTIVE)
    file = open("E:/PROJECTS/PYTHON PROJECTS/GUI MP3 PLAYER/MP3-PLAYER[can browse .mp3 files]/MAIN CODE FILE/playlist/PLAYLIST1.txt","r")
    file = file.read()
    file = file.split("\n")
    for x in file:
        if x.find(song) != -1:
            mixer.music.load(x)
            mixer.music.set_volume(0.3)
            mixer.music.play()

def stop():
    mixer.music.fadeout(1000)
    playlist.selection_clear(ACTIVE)

def pause (event):
    mixer.music.pause()

def unpause (event):
    mixer.music.unpause()

def rewind ():
        mixer.music.rewind()

def loop ():
        mixer.music.play(-1)

i = 1
def next ():
        global i
        file = open("E:/PLAYLIST1.txt","r")
        file = file.read()
        file = file.split("\n")
        for item in playlist.curselection():
                song = playlist.get(item+i)
                for x in file:
                    if x.find(song) != -1:
                        mixer.music.load(x)
                        mixer.music.set_volume(0.3)
                        mixer.music.play()
        i += 1

def cover ():
        l1 = Label(root, image = image_volume_cover, background="black")
        l1.place(x = 220,y=290)

def volume ():
        volume_slider = Scale(root, from_ = 0, to=10, background="black"
             ,foreground="white",length=200 ,orient= HORIZONTAL,tickinterval=1)
        volume_slider.place(x = 220, y = 320)
        def change_volume ():
                new_volume = volume_slider.get()/10
                mixer.music.set_volume(new_volume)
        b_set_volume = Button(root, text = "SET VOLUME", command=change_volume)
        b_set_volume.place(x = 220, y = 290)
        b_close = Button(root, text = "X", font = ("cambriamath 9 bold")
                ,background="red",foreground="black",padx = 2,command= cover)
        b_close.place(x = 305, y = 290)


#MENU AND SUB-MENU CONTROL
main_menu = Menu(root)
slider_menu = Menu(main_menu, tearoff=False, bd=3
        ,activebackground="black", activeforeground="red")
slider_menu.add_command(label="Add Songs", background= "white"
        , foreground="black", command=add_song)
slider_menu.add_command(label="Open Playlist", background= "white"
        , foreground="black", command=add_playlist_song )
root.config(menu= main_menu)
main_menu.add_cascade(label = "File", activebackground = "blue"
                , menu = slider_menu)


#ALL IMAGES
image_pause =  Image.open("E:/PROJECTS/PYTHON PROJECTS/GUI MP3 PLAYER/MP3-PLAYER[can browse .mp3 files]/MAIN CODE FILE/data/pause.png")
resized_image= image_pause.resize((40,40))
image_pause= ImageTk.PhotoImage(resized_image)
image_play =  Image.open("E:/PROJECTS/PYTHON PROJECTS/GUI MP3 PLAYER/MP3-PLAYER[can browse .mp3 files]/MAIN CODE FILE/data/start.png")
resized_image= image_play.resize((40,40))
image_play= ImageTk.PhotoImage(resized_image)
image_stop =  Image.open("E:/PROJECTS/PYTHON PROJECTS/GUI MP3 PLAYER/MP3-PLAYER[can browse .mp3 files]/MAIN CODE FILE/data/stop.png")
resized_image= image_stop.resize((40,40))
image_stop= ImageTk.PhotoImage(resized_image)
image_rewind =  Image.open("E:/PROJECTS/PYTHON PROJECTS/GUI MP3 PLAYER/MP3-PLAYER[can browse .mp3 files]/MAIN CODE FILE/data/rewind.png")
resized_image= image_rewind.resize((40,40))
image_rewind= ImageTk.PhotoImage(resized_image)
image_volume =  Image.open("E:/PROJECTS/PYTHON PROJECTS/GUI MP3 PLAYER/MP3-PLAYER[can browse .mp3 files]/MAIN CODE FILE/data/volume.png")
resized_image= image_volume.resize((40,40))
image_volume= ImageTk.PhotoImage(resized_image)
image_loop =  Image.open("E:/PROJECTS/PYTHON PROJECTS/GUI MP3 PLAYER/MP3-PLAYER[can browse .mp3 files]/MAIN CODE FILE/data/loop.jpg")
resized_image= image_loop.resize((40,40))
image_loop= ImageTk.PhotoImage(resized_image)
image_next =  Image.open("E:/PROJECTS/PYTHON PROJECTS/GUI MP3 PLAYER/MP3-PLAYER[can browse .mp3 files]/MAIN CODE FILE/data/next.png")
resized_image= image_next.resize((40,40))
image_next= ImageTk.PhotoImage(resized_image)
image_volume_cover =  Image.open("E:/PROJECTS/PYTHON PROJECTS/GUI MP3 PLAYER/MP3-PLAYER[can browse .mp3 files]/MAIN CODE FILE/data/volume_cover.jpg")
resized_image= image_volume_cover.resize((210,90))
image_volume_cover= ImageTk.PhotoImage(resized_image)


#ALL BUTTONS
pause_button = Button(root, image=image_pause, background="black"
        ,foreground="black",activebackground="black")
pause_button.place(x = 154, y = 390)
pause_button.bind("<Button-1>", pause)
pause_button.bind("<Double-1>",  unpause)
play_button = Button(root, image=image_play, background="black"
        ,foreground="black",activebackground="black")
play_button.place(x = 200, y = 390)
play_button.bind("<Button-1>",play_)
stop_button = Button(root, image=image_stop, background="black"
        ,foreground="black",activebackground="black", command=stop)
stop_button.place(x = 108, y = 390)
rewind_button = Button(root, image=image_rewind, background="black"
        ,foreground="black",activebackground="black", command=rewind)
rewind_button.place(x = 62, y = 390)
volume_button = Button(root, image=image_volume, background="black"
        ,foreground="black",activebackground="black", command=volume)
volume_button.place(x = 338, y = 390)
loop_button = Button(root, image=image_loop, background="black"
        ,foreground="black",activebackground="black", command=loop)
loop_button.place(x = 292, y = 390)
next_button = Button(root, image=image_next, background="black"
        ,foreground="black",activebackground="black", command= next)
next_button.place(x = 246, y = 390)



root.mainloop()