import customtkinter
from tkinter import *
from hangmangamefunctions import *
import sys

class HangmanApp:
    
    def __init__(self, master):
        self.master = master
        self.master.title('Pedro Hangman')
        self.master.geometry('1600x900')
        self.failed = 0
        self.letterposition = -1
        self.correctletters = []
        self.lettersattempted = []
        self.menu()
    def guessletter(self):
        if len(self.letterentry.get()) > 1:
            self.letter = self.letterentry.get()[:1]
        else:
            self.letter = self.letterentry.get()
        if not self.letter.isalpha():
            index = -2
        else:
            index = checkletter(self.word,self.letter,self.correctletters,self.lettersattempted)
        if index == -1:
            self.failed += 1
        elif index == -2:
            pass
        else:
            self.letterposition = index
        self.hangmangame()
    def hangmangame(self):
        for i in self.master.winfo_children():
            i.destroy()
        #Get list for the word
        wordlist = getword(self.word)
        self.chances = ((len(wordlist)//2) + 3) - self.failed
        self.xForWord = createlist(wordlist,self.correctletters)
        if self.xForWord == True:
            self.game_won_screen()
        else:
            #check if game over
            if self.chances == 0:
                self.game_over_screen()
            else:
                self.wordcomplete = False
                #Title
                self.gamelabel = customtkinter.CTkLabel(master=self.master, text='Hangman',font=('Algerian',100))
                self.gamelabel.pack(pady=20)
                #Display word
                if len(wordlist) == 1:
                    fontsize = 720//3
                else:
                    fontsize = 720//(len(wordlist)+1)
                self.wordlabel = customtkinter.CTkLabel(master=self.master, text=self.xForWord, font=('Bauhaus',fontsize))
                self.wordlabel.pack(pady=10)
                #Letter entry
                self.letterentry = customtkinter.CTkEntry(master=self.master, placeholder_text='Guess a Letter',justify='center', font=('Bauhaus',50), height=100,width=500)
                self.letterentry.pack(pady=10)
                #enter letter button
                self.letterbutton = customtkinter.CTkButton(master=self.master, text='Enter letter',font=('Bauhaus',60), command=self.guessletter)
                self.letterbutton.pack(pady=10)
                #chances label
                self.chanceslabel = customtkinter.CTkLabel(master=self.master, text=f'Chances left = {self.chances}', font=('Bauhaus',50))
                self.chanceslabel.pack(pady=20)
                #letters attempted
                self.letterattemptedlabel = customtkinter.CTkLabel(master=self.master, text=f'Letters attempted: {self.lettersattempted}', font=('Bauhaus',20))
                self.letterattemptedlabel.pack(pady=10)
                #return to menu button
                self.menubutton = customtkinter.CTkButton(master=self.master, text='Menu', font=('Bauhaus',50),anchor='se', command=self.menu)
                self.menubutton.pack(pady=20)
    def hangmanmenu(self):
        for i in self.master.winfo_children():
            i.destroy()
        #Title for the page
        self.gamelabel = customtkinter.CTkLabel(master=self.master, text='Hangman',font=('Algerian',100))
        self.gamelabel.pack(pady=20)
        #Entry to put the word
        self.wordentry = customtkinter.CTkEntry(master=self.master, placeholder_text='Enter the word for the game (Cut at 12 letters)', font=('Bauhaus',30),height=70,width=1000)
        self.wordentry.pack(pady=20)
        #Button to entry the word
        self.entrybutton = customtkinter.CTkButton(master=self.master, text='Enter word', corner_radius=20, border_color='#FF0000', font=('Bauhaus',20), command=self.entryget)
        self.entrybutton.pack(pady=20)
        #return to menu button
        self.menubutton = customtkinter.CTkButton(master=self.master, text='Menu', font=('Bauhaus',50),anchor='se', command=self.menu)
        self.menubutton.pack(pady=60)
        self.failed = 0
        self.letterposition = -1
        self.correctletters = []
        self.lettersattempted = []
    def game_over_screen(self):
        for i in self.master.winfo_children():
            i.destroy()
        #Title for the page
        self.gamelabel = customtkinter.CTkLabel(master=self.master, text='Hangman',font=('Algerian',100))
        self.gamelabel.pack(pady=20)
        #You Lost Label
        self.gamelostlabel = customtkinter.CTkLabel(master=self.master, text='You lost', font=('Algerian', 100),anchor='center')
        self.gamelostlabel.pack(pady=20)
        #Button for menu
        self.menubutton = customtkinter.CTkButton(master=self.master, text='Menu', font=('Bauhaus',200), command=self.menu)
        self.menubutton.pack(pady=20)
        #Button for Play again
        self.playbutton = customtkinter.CTkButton(master=self.master, text='Play', font=('Algerian',200), command=self.hangmanmenu)
        self.playbutton.pack(pady=20)
    def game_won_screen(self):
        for i in self.master.winfo_children():
            i.destroy()
        #Title for the page
        self.gamelabel = customtkinter.CTkLabel(master=self.master, text='Hangman',font=('Algerian',100))
        self.gamelabel.pack(pady=20)
        #Game Won Title
        self.gamewonlabel = customtkinter.CTkLabel(master=self.master, text='You won', font=('Algerian', 100),anchor='center')
        self.gamewonlabel.pack(pady=20)
        #Main Menu button
        self.menubutton = customtkinter.CTkButton(master=self.master, text='Menu', font=('Bauhaus',50),anchor='se', command=self.menu)
        self.menubutton.pack()
    def menu(self):
        for i in self.master.winfo_children():
            i.destroy()
        #start new widgets
        self.menulabel = customtkinter.CTkLabel(master=self.master, text='Main Menu',font=('Algerian',100))
        self.menulabel.pack(pady=20)
        self.playbutton = customtkinter.CTkButton(master=self.master, text='Play', font=('Algerian',100), command=self.hangmanmenu, width=500, height=100)
        self.playbutton.pack(pady=20)
        #rules button
        self.rulesbutton = customtkinter.CTkButton(master=self.master, text='Rules', font=('Algerian',100), command=self.rules, width=500, height=100 )
        self.rulesbutton.pack(pady=10)
        #exit button
        self.exitbutton = customtkinter.CTkButton(master=self.master, text='Exit', font=('Algerian',100), command=sys.exit, width=500, height=100)
        self.exitbutton.pack(pady=10)
    def rules(self):
        for i in self.master.winfo_children():
            i.destroy()
        #Title
        self.gamelabel = customtkinter.CTkLabel(master=self.master, text='Hangman',font=('Algerian',100))
        self.gamelabel.pack(pady=20)
        #Text
        self.ruleslabel = customtkinter.CTkLabel(master=self.master, text='Rules', font=('Algerian',50))
        self.ruleslabel.pack(pady=20)
        #Return to menu button
        self.menubutton = customtkinter.CTkButton(master=self.master, text='Menu', font=('Bauhaus',200), command=self.menu)
        self.menubutton.pack(pady=20)
    def entryget(self):
        #Get the word for the function
        if len(self.wordentry.get()) > 12:
            self.word = self.wordentry.get()[:12]  
        else:
            self.word = self.wordentry.get()
        if not self.word.isalpha():
            self.entryget()
        else:
            self.hangmangame()
if __name__ == '__main__':
    customtkinter.set_appearance_mode('Dark')
    root = customtkinter.CTk()
    HangmanApp(root)
    root.mainloop()