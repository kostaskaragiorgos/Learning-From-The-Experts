from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
from tkinter import simpledialog
from sklearn import tree

class Genderclass():
    def __init__(self,master):
        self.master = master
        self.master.title("Gender Classifier")
        self.master.resizable(False,False)
        self.master.geometry("250x120")
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator = 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        
        self.x = [[180,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,410],
                  [190,90,47],[175,64,39],
                  [177,70,40],[159,55,37],[171,75,42],[181,85,43]]
        self.y = ['male','male','female','female','male','male','female','female','female','male','male']
        self.pred = Button(self.master,text = "Prediction",command = self.prediction)
        self.pred.pack()
        
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def aboutmenu(self):
        pass
    
    def helpmenu(self):
        pass
    
    def prediction(self):
        height = simpledialog.askinteger("Height","What is the Height in cm",parent = self.master,minvalue = 159,maxvalue = 190)
        weight = simpledialog.askinteger("Weight","What is the Weight in kg",parent = self.master,minvalue = 55,maxvalue = 90)
        Shoesize = simpledialog.askinteger("Show Size","What is the Shoe size",parent = self.master,minvalue = 36,maxvalue = 45)
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(self.x,self.y)
        prediction  = clf.predict([[height,weight,Shoesize]])
        """
        self.x.append([height,weight,Shoesize])
        """
        msg.showinfo("Prediction",str(prediction))
        """
        self.y.append(str(prediction))
        print(self.x)
        print(self.y)
        """
def main():
    root=Tk()
    CC = Genderclass(root)
    root.mainloop()
    
if __name__=='__main__':
    main()