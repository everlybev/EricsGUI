from Backend import *
from tkinter import *

class Button_Widget():
    def __init__(self, tk):
        self.root = tk
        self.buttons = []
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1
        self.action = ''
        self.actionargs = ''
    
    def add_widget(self, name, action, action_arg='NA', x_pix_loc=1, y_pix_loc=1,
                   ancor='center', rel=False, plaisce=False, multiargument=False, args=[]):
        self.action = action
        self.actionargs = action_arg
        if multiargument:
            if len(args) == 2:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1, self.actionargs2)))
            elif len(args) == 3:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1, self.actionargs2, self.actionargs3)))
            elif len(args) == 4:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4)))
        else:
            self.buttons.append(Button(self.root, text=name, command=lambda: self.action(self.actionargs)))
        if plaisce:
            if rel:
                self.buttons[len(self.buttons)-1].place(relx=x_pix_loc, rely=y_pix_loc, anchor=ancor)
            else:
                self.buttons[len(self.buttons)-1].place(x=x_pix_loc, y=y_pix_loc, anchor=ancor)
        self.width = self.buttons[len(self.buttons)-1].winfo_reqwidth()
        self.height = self.buttons[len(self.buttons)-1].winfo_reqheight()
        self.x = x_pix_loc
        self.y = y_pix_loc

    def place_here(self, xloc, yloc, paddingx, paddingy, ancor='center', rel=False):
        truex = (self.width/2) + paddingx + xloc
        truey = (self.height/2) + paddingy + yloc
        if rel:
            #xcenterpix = 
            self.buttons[len(self.buttons)-1].place(relx=truex, rely=truex, anchor=ancor)
        else:
            self.buttons[len(self.buttons)-1].place(x=truex, y=truey, anchor=ancor)
        self.x = truex
        self.y = truey

class Label_Widget():
    def __init__(self, tk):
        self.root = tk
        self.labels = []
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1
    
    def add_widget(self, label, xloc, yloc, ancor='center', rel=False, plaisce=False, w='', h=''):
        self.labels.append(Label(self.root, text=label))
        if (w == '') and (not (h == '')):
            self.labels[len(self.labels)-1].config(height=h)
        elif (not (w == '')) and (h == ''):
            self.labels[len(self.labels)-1].config(width=w)
        elif (not (w == '')) and (not (h == '')):
            self.labels[len(self.labels)-1].config(width=w, height=h)
        if plaisce:
            if rel:
                self.labels[len(self.labels)-1].place(relx=xloc, rely=yloc, anchor=ancor)
            else:
                self.labels[len(self.labels)-1].place(x=xloc, y=yloc, anchor=ancor)
        self.width = self.labels[len(self.labels)-1].winfo_reqwidth()
        self.height = self.labels[len(self.labels)-1].winfo_reqheight()
        self.x = xloc
        self.y = yloc

    def place_here(self, xloc, yloc, paddingx, paddingy, ancor='center', rel=False):
        truex = (self.width/2) + paddingx + xloc
        truey = (self.height/2) + paddingy + yloc
        if rel:
            #xcenterpix = 
            self.labels[len(self.labels)-1].place(relx=truex, rely=truex, anchor=ancor)
        else:
            self.labels[len(self.labels)-1].place(x=truex, y=truey, anchor=ancor)
        self.x = truex
        self.y = truey

class Listbox_widget():
    def __init__(self, tk):
        self.root = tk
        self.listboxess = []
        self.width = 2
        self.height = 2
        self.x = 2
        self.y = 2

    def get_legnth_of_text_plus_one(self, listeORtext):
        if type(listeORtext) == type('Timothy Wing-kin Koppisch touches children'):
            fh = listeORtext.count('\n') + 1
            fw = len(listeORtext) + 1
        elif type(listeORtext) == type(['Nipples', 'Dick']):
            lish = []
            lisw = []
            for word in listeORtext:
                if not (type(word) == type('277353')):
                    text = str(word)
                else:
                    text = word
                lisw.append(len(text))
                lish.append(listeORtext.count('\n') + 1)
            if lish == []:
                fh = 1
            else:
                fh = max(lish) + 1
            if lisw == []:
                fw = 1
            else:
                fw = max(lisw) + 1
        else:
            print('<text> must be a list or string')
            fw = 1
            fh = 1
        return fw, fh
    
    def populate_box(self, box, liste):
        for item in liste:
            box.insert(END, item)

    def remove_everything(self):
        box = self.listboxess[len(self.listboxess)-1]
        box.delete(0, END)
    
    def add_widget(self, mode, options, xloc, yloc, window_width, window_height, ancor='center', rel=False, plaisce=False):
        if mode.lower() == 'single':
            self.listboxess.append(Listbox(self.root, selectmode=SINGLE, exportselection=0))
        elif mode.lower() == 'multiple':
            self.listboxess.append(Listbox(self.root, selectmode=MULTIPLE, exportselection=0))
        le, he = self.get_legnth_of_text_plus_one(options)
        self.listboxess[len(self.listboxess)-1].config(width=le, height=int(((20)*window_height)/640))
        while self.width > window_width:
            le = le - 1
            self.listboxess[len(self.listboxess)-1].config(width=le, height=int(((20)*window_height)/640))
        self.populate_box(self.listboxess[len(self.listboxess)-1], options)
        if plaisce:
            if rel:
                self.listboxess[len(self.listboxess)-1].place(relx=xloc, rely=yloc, anchor=ancor)
            else:
                self.listboxess[len(self.listboxess)-1].place(x=xloc, y=yloc, anchor=ancor)
        self.width = self.listboxess[len(self.listboxess)-1].winfo_reqwidth()
        self.height = self.listboxess[len(self.listboxess)-1].winfo_reqheight()
        self.x = xloc
        self.y = yloc

    def place_here(self, xloc, yloc, paddingx, paddingy, ancor='center', rel=False):
        truex = (self.width/2) + paddingx + xloc
        truey = (self.height/2) + paddingy + yloc
        if rel:
            #xcenterpix = 
            self.listboxess[len(self.listboxess)-1].place(relx=truex, rely=truex, anchor=ancor)
        else:
            self.listboxess[len(self.listboxess)-1].place(x=truex, y=truey, anchor=ancor)
        self.x = truex
        self.y = truey

class Textinput_Widget():
    def __init__(self, tk):
        self.root = tk
        self.inputboxes = []
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1
    
    def add_widget(self, number_of_characters, number_of_lines, xloc=1, yloc=1, ancor='center', rel=False, plaisce=False):
        self.inputboxes.append(Text(self.root, width=number_of_characters, height=number_of_lines))
        if plaisce:
            if rel:
                self.inputboxes[len(self.inputboxes)-1].place(relx=xloc, rely=yloc, anchor=ancor)
            else:
                self.inputboxes[len(self.inputboxes)-1].place(x=xloc, y=yloc, anchor=ancor)
        self.width = self.inputboxes[len(self.inputboxes)-1].winfo_reqwidth()
        self.height = self.inputboxes[len(self.inputboxes)-1].winfo_reqheight()
        self.x = xloc
        self.y = yloc

    def remove_widget(self, indexes=[]):
        if indexes == []:
            self.inputboxes = []
        else:
            temp = []
            for index in range(0, len(self.inputboxes)):
                if index not in indexes:
                    temp.append(self.inputboxes[index])
            self.inputboxes = temp

    def place_here(self, xloc, yloc, paddingx=1, paddingy=1, ancor='center', rel=False):
        truex = (self.width/2) + paddingx + xloc
        truey = (self.height/2) + paddingy + yloc
        if rel:
            #xcenterpix = 
            self.inputboxes[len(self.inputboxes)-1].place(relx=truex, rely=truex, anchor=ancor)
        else:
            self.inputboxes[len(self.inputboxes)-1].place(x=truex, y=truey, anchor=ancor)
        self.x = truex
        self.y = truey
        