from tkinter import *
from tkinter.messagebox import *

# Import Dialog box for opening or saving a file
from tkinter.filedialog import *

#Import OS for using all Operating System features 
import os

# Create the Notepad Class
class Notepad:
    root = Tk()
    root.wm_iconbitmap('C:/Python Scripts/notepad.ico')
    root.title("Untitled - Notepad")
    root.geometry("700x400")
    TextArea = Text(root, font = ("arial, 15"))
    menubar = Menu(root)
    FileMenu = Menu(menubar, tearoff = 0)
    EditMenu = Menu(menubar, tearoff = 0)
    HelpMenu = Menu(menubar, tearoff = 0)
    
    Scrollbar = Scrollbar(TextArea)
    file = None
    
    def __init__(self):
        # Text Area resizable
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)
        self.TextArea.grid(sticky = N + E + S + W)
        
        #File Nenu
        self.FileMenu.add_command(label = "New")
        self.FileMenu.add_command(label = "Save")
        self.FileMenu.add_command(label = "Open", command=self.openFile)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label = "Exit", activebackground ="red", command=self.quitApp)
        self.menubar.add_cascade(label = "File", menu = self.FileMenu)
       
        #Edit Menu
        self.EditMenu.add_command(label = "Select All     CTRL-A")
        self.EditMenu.add_command(label ="Cut               CTRL-X")
        self.EditMenu.add_command(label ="Copy            CTRL-C")
        self.EditMenu.add_command(label ="Paste            CTRL-V")
        
        self.menubar.add_cascade(label = "File", menu = self.EditMenu)
        
        #Help Menu
        self.HelpMenu.add_command(label = "About Notepad", command=self.showAppInfo)
        self.menubar.add_cascade(label = "Help", menu = self.HelpMenu)
        
        #Config & Pack
        self.root.config(menu = self.menubar)
        self.Scrollbar.pack(side = RIGHT, fill = Y)
        self.Scrollbar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand = self.Scrollbar.set)

    def quitApp(self):
        self.root.destroy()

    def showAppInfo(self):
        showinfo("Notepad", "This is the Notepad application")
    
    def openFile(self):
        self.file = askopenfilename(defaultextension='.txt', filetypes = [('All Files', '*.*'), ('Text Document', '*.txt')])

        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file)+" - Notepad")
            self.TextArea.delete(1.0, END)
            file = open(self.file, "r")
            self.TextArea.insert(1.0, file.read())
            file.close()
    
    def run(self):
        self.root.mainloop()

notepad = Notepad()
notepad.run()
