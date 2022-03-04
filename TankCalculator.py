import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("TankCalculator")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.entry=tk.Entry(root)
        self.entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.entry["font"] = ft
        self.entry["fg"] = "#333333"
        self.entry["justify"] = "center"
        self.entry["text"] = ""
        self.entry.place(x=240,y=60,width=111,height=33)

        self.okButton=tk.Button(root)
        self.okButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.okButton["font"] = ft
        self.okButton["fg"] = "#000000"
        self.okButton["justify"] = "center"
        self.okButton["text"] = "Ok"
        self.okButton.place(x=260,y=110,width=70,height=25)
        self.okButton["command"] = self.okButtonCommand

        self.indicator=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.indicator["font"] = ft
        self.indicator["fg"] = "#333333"
        self.indicator["justify"] = "center"
        self.indicator["text"] = "Enter a number"
        self.indicator.place(x=240,y=20,width=108,height=30)

        self.paramButton=tk.Button(root)
        self.paramButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.paramButton["font"] = ft
        self.paramButton["fg"] = "#000000"
        self.paramButton["justify"] = "center"
        self.paramButton["text"] = "Parameters"
        self.paramButton.place(x=260,y=170,width=70,height=25)
        self.paramButton["command"] = self.paramButtonCommand

    def okButtonCommand(self):
        print(self.entry.get())


    def paramButtonCommand(self):
        # function to open a new window
        # on a button click
     
        # Toplevel object which will
        # be treated as a new window
        newWindow = tk.Toplevel(root)
    
        # sets the title of the
        # Toplevel widget
        newWindow.title("Parameters")
    
        # sets the geometry of toplevel
        newWindow.geometry("200x200")
        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
