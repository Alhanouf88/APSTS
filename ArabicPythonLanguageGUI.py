# The Arabic-Python Translation System GUI
from tkinter import *
from tkinter import PhotoImage
import sys
import os
import APtranslatorGUI
import subprocess

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="ادخل اسم الملف")
        self.l.grid()
        self.e=Entry(top)
        self.e.grid()
        self.b=Button(top,text='تم',command=self.cleanup)
        self.b.grid()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class Display(Frame):

    def __init__(self, parent=None):
       Frame.__init__(self)
       # The GUI methods' buttons
       self.load = Button(self,text="جديد", command=self.New, width = 6, padx=15, pady=20)
       self.load.grid(row=1, column=3)

       self.load = Button(self,text=" فتح", command=self.Open, width = 6, padx=15, pady=20)
       self.load.grid(row=1, column=2)

       self.doIt = Button(self,text="تنفيذ", command=self.Run, width = 6, padx=15, pady=20)
       self.doIt.grid(row=1, column=1)

       self.doIt = Button(self,text="اغلاق", command=self.Exit, width = 6, padx=15, pady=20)
       self.doIt.grid(row=1, column=0)

       self.grid()

    # The GUI methods' body
    def Run(self):
        try:
            subprocess.call(["/usr/bin/open", "-a", "/Applications/Utilities/Terminal.app"])
            if os.path.getsize(self.name+'.txt')<1 :
                print("لا يوجد برنامج للتشغيل\n")
            else:
                print("جاري تشغيل البرنامج")
                coderead= open(self.name+'.txt', 'r')
                APtranslatorGUI.main(coderead)
                coderead.close()
                print("انتهى\n")
        except:
            print("حدث خطأ في تشغيل الملف: لا يوجد ملف قيد التشغيل")

    def New(self):
        self.w=popupWindow(self.master)
        self.master.wait_window(self.w.top)
        self.name= self.w.value
        TempFile= open(self.name+'.txt', 'w')
        cwd = os.getcwd()
        subprocess.call(["/usr/bin/open", "-n", "-a", "/Applications/TextEdit.app", cwd+'/'+self.name+'.txt'])
        TempFile.close()

    def Open(self):
        self.w=popupWindow(self.master)
        self.master.wait_window(self.w.top)
        self.name= self.w.value
        try:
            TempFile= open(self.name+'.txt', 'r+')
            cwd = os.getcwd()
            subprocess.call(["/usr/bin/open", "-n", "-a", "/Applications/TextEdit.app", cwd+'/'+self.name+'.txt'])
            TempFile.close()
        except:
            print("الملف غير موجود")

    def Exit(self):
        root.destroy()

    def flush(self):
        pass

if __name__ == '__main__':
    root = Tk()
    root.title("لغة بايثون العربية")
    photo = PhotoImage(file="/Users/macbookpro/Desktop/python.gif")
    photo_label = Label(image=photo)
    label = Label(image=photo)
    label.image = photo
    label.grid()

    app = Display(root)
    root.mainloop()
