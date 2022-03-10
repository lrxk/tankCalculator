import tkinter as tk
import tkinter.font as tkFont

class App:
    tankWidth=180
    tankHeight=200
    def __init__(self, root):
        self.root=root
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
        vcmd = (self.root.register(self.callback))
        self.entry=tk.Entry(root,validate='all',validatecommand=(vcmd,'%P'))
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

        self.result=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.result["font"] = ft
        self.result["fg"] = "#333333"
        self.result["justify"] = "center"
        self.result["text"] = ""
        self.result.place(x=240,y=190,width=108,height=30)
        
        self.paramButton=tk.Button(root)
        self.paramButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.paramButton["font"] = ft
        self.paramButton["fg"] = "#000000"
        self.paramButton["justify"] = "center"
        self.paramButton["text"] = "Parameters"
        self.paramButton.place(x=260,y=170,width=70,height=25)
        self.paramButton["command"] = self.paramButtonCommand
    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
    def compute(self):
        if self.entry.get()=='':
            result="Enter a number"
            return result
        result=float(int(self.entry.get())*self.tankHeight*self.tankWidth)/1000.0
        return result
    def okButtonCommand(self):
        self.result["text"] =str(self.compute())+"L"
    def paramButtonCommand(self):
        # function to open a new window
        # on a button click

        # Toplevel object which will
        # be treated as a new window
        width=400
        height=400
        x=(width/2)-70
        self.newWindow = tk.Toplevel(self.root)
        screenwidth = self.newWindow.winfo_screenwidth()
        screenheight = self.newWindow.winfo_screenheight()
        # sets the title of the
        # Toplevel widget
        self.newWindow.title("Parameters")
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        # sets the geometry of toplevel
        self.newWindow.geometry(alignstr)
        self.longueur=tk.Label(self.newWindow)
        ft = tkFont.Font(family='Times',size=10)
        self.longueur["font"] = ft
        self.longueur["fg"] = "#333333"
        self.longueur["justify"] = "center"
        self.longueur["text"] = "Longueur"
        self.longueur.place(x=x,y=30,width=70,height=25)
        vcmd=(self.newWindow.register(self.callback))
        self.longueurEntry=tk.Entry(self.newWindow,validate='all',validatecommand=(vcmd,'%P'))
        self.longueurEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.longueurEntry["font"] = ft
        self.longueurEntry["fg"] = "#333333"
        self.longueurEntry["justify"] = "center"
        self.longueurEntry["text"] = ""
        self.longueurEntry.place(x=x,y=60,width=70,height=25)

        self.largeur=tk.Label(self.newWindow)
        ft = tkFont.Font(family='Times',size=10)
        self.largeur["font"] = ft
        self.largeur["fg"] = "#333333"
        self.largeur["justify"] = "center"
        self.largeur["text"] = "Largeur"
        self.largeur.place(x=x,y=100,width=70,height=25)

        self.largeurEntry=tk.Entry(self.newWindow,validate='all',validatecommand=(vcmd,'%P'))
        self.largeurEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.largeurEntry["font"] = ft
        self.largeurEntry["fg"] = "#333333"
        self.largeurEntry["justify"] = "center"
        self.largeurEntry["text"] = ""
        self.largeurEntry.place(x=x,y=140,width=70,height=25)

        okParameterButton=tk.Button(self.newWindow)
        okParameterButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        okParameterButton["font"] = ft
        okParameterButton["fg"] = "#000000"
        okParameterButton["justify"] = "center"
        okParameterButton["text"] = "Ok"
        okParameterButton.place(x=x,y=190,width=70,height=25)
        okParameterButton["command"] = self.okParameterButton_command

    def okParameterButton_command(self):
        self.tankWidth=int(self.largeurEntry.get())
        self.tankHeight=int(self.longueurEntry.get())
        self.newWindow.destroy()
        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
