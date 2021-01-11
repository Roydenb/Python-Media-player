from tkinter import *
import pygame
import os

window=Tk()

class MusicPlayerGui():
      def __init__(self,root):
          self.root = root
          # Title of the window
          self.root.title("Music_Player")
          # Window Geometry
          self.root.geometry("1000x200+200+200")
          # Initiating Pygame
          pygame.init()
          # Initiating Pygame Mixer
          pygame.mixer.init()
          # Declaring track Variable
          self.track = StringVar()

          # Track frame for te song labels
          self.trackframe = LabelFrame(self.root,text="Track",
                                       font=("FreeMono",20,"bold")
                                       ,bg="black",fg="yellow",bd=5,relief=GROOVE)
          self.trackframe.place(x=0,y=0,width=1000,height=100)

          # Song lable
          self.songtrack = Label(self.trackframe,textvariable=self.track,width=35,
                                 font=("times new roman",15,"bold"),fg="gold",bg="black")\
                                 .grid(row=0,column=0,padx=10,pady=10)

           # Btn frames
          self.button_frame = LabelFrame(self.root,text="Controls",
                                        font=("FreeMono",20,"bold")
                                         ,bg="black",fg="yellow",bd=5,relief=GROOVE)
          self.button_frame.place(x=0,y=100,width=600,height=100)

          # Play Btn
          self.playbtn = Button(self.button_frame,text="PLAYSONG",
                                command=self.playsong,width=10,height=1,
                                font=("times new roman",16,"bold"),fg="yellow",bg="red")\
                                .grid(row=0,column=0,padx=40,pady=5)
          # Pause Btn
          self.playbtn = Button(self.button_frame,text="PAUSE",
                                command=self.pausesong,width=8,height=1,
                                font=("times new roman",16,"bold"),fg="yellow",bg="black")\
                                .grid(row=0,column=1,padx=10,pady=5)

          # Unpause Btn
          self.playbtn = Button(self.button_frame,text="UNPAUSE",
                                command=self.unpausesong,width=10,height=1,
                                font=("times new roman",16,"bold"),fg="yellow",bg="red").grid(row=0,column=2,padx=40,pady=5)

           # Playlist frame
          self.songs_frame = LabelFrame(self.root,text="Playlist",
                                       font=("FreeMono",20,"bold")
                                        ,bg="black",fg="yellow",bd=5,relief=GROOVE)
          self.songs_frame.place(x=600,y=0,width=400,height=200)

          # Scrollbar for the listbox
          scroll_bar= Scrollbar(self.songs_frame,orient=VERTICAL)

          # Adding the playlist to the listbox
          self.song_playlist = Listbox(self.songs_frame,yscrollcommand=scroll_bar.set,selectbackground="gold",
                                  selectmode=SINGLE,font=("times new roman",15,"bold")
                                  ,bg="black",fg="red",bd=5,relief=GROOVE)

          # Combines the scrollbar and the listbox
          scroll_bar.pack(side=RIGHT,fill=Y)
          scroll_bar.config(command=self.song_playlist.yview)
          self.song_playlist.pack(fill=BOTH)

          # The folder of the songs/Directory
          os.chdir('Music')

          # Getting the songs out of the folder/directory
          self.tracks = os.listdir()

          # Inserting Songs into Playlist
          for track in self.tracks:
              self.song_playlist.insert(END,track)

      #F-U-N-C-T-I-O-N-S
      #PLAY
      # PAUSE
      # UNPAUSE
      def playsong(self):
            # View the selected song
            self.track.set(self.song_playlist.get(ACTIVE))
            # Loads the selected song
            pygame.mixer.music.load(self.song_playlist.get(ACTIVE))
            # Plays the selected song
            pygame.mixer.music.play()

      def pausesong(self):
          # function to pause the song
          pygame.mixer.music.pause()

      def unpausesong(self):
        # function to play the song where the song was paused
        # (continues the song)
        pygame.mixer.music.unpause()

window=MusicPlayerGui(window)
mainloop()
