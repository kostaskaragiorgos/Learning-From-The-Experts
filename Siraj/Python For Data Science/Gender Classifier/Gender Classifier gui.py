from tkinter import *
from tkinter import messagebox as msg 
from sklearn import tree
from tkinter import simpledialog

class Gender_Classifier():
    def __init__(self,master):
        self.master = master
        self.master.title("Gender Classifier")
        self.master.geometry("200x200")
        
        #[height , weight, shoe size]
        self.x = [[180,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,410],
                  [190,90,47],[175,64,39],
                  [177,70,40],[159,55,37],[171,75,42],[181,85,43]]
        self.y = ['male','male','female','female','male','male','female','female','female','male','male']
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(self.x,self.y)
        height = simpledialog.askinteger("Height","What is the Height in cm",parent = self.master,minvalue = 159,maxvalue = 190)
        
def main():
    root=Tk()
    myexp = Gender_Classifier(root)
    root.mainloop()
    
if __name__=='__main__':
    main()
    
"""
prediction  = clf.predict([[190,70,43]])
print(prediction)
"""