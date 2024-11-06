'''rpn_display
   by: James R Brown
'''

from tkinter import *
from tkinter import ttk
from rpn_calc import RPN_Calc


T_FONT = ("Arial", 24, "bold")
W_FONT = ("Arial", 16, "normal")

class RpnDisplay:

    def __init__(self):
        self.root =  Tk()
        self.rpncalc = RPN_Calc()
        self.root.title('RPN Calc')
        self.eq = ["0"]
        self.display_text = StringVar(value=self.eq)


    def setup_display(self):
        '''Sets up main frame and second frame for buttons'''
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.buttonframe = ttk.Frame(self.root, padding="2 2 2 2")
        self.buttonframe.grid(column=0, row=1, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.minsize(width=300, height=500)
        # Rows
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=1)
        self.buttonframe.rowconfigure(0, weight=1)
        self.buttonframe.rowconfigure(1, weight=1)
        self.buttonframe.rowconfigure(2, weight=1)
        self.buttonframe.rowconfigure(3, weight=1)
        self.buttonframe.rowconfigure(4, weight=1)
        self.buttonframe.rowconfigure(5, weight=1)

        # Column
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

    def gen_display(self):
        '''Generates the display and runs main window'''
        self.setup_display()
        dis_title = ttk.Label(self.mainframe, text="RPN Calc", font=T_FONT)
        dis_title.grid(column=0, row=0)
        self.nl = Listbox(self.mainframe, height=5, listvariable=self.display_text)
        self.nl.grid(column=0, row=1, sticky=(N,W,E,S))
        self.s = ttk.Scrollbar(self.mainframe, orient=VERTICAL,
                               command=self.nl.yview)
        self.s.grid(column=1, row=1, sticky=(N, S))
        self.nl['yscrollcommand'] = self.s.set
        
        button1 = ttk.Button(self.buttonframe, text='1', command=lambda : self.btn_press('1'))
        button2 = ttk.Button(self.buttonframe, text='2', command=lambda : self.btn_press('2'))
        button3 = ttk.Button(self.buttonframe, text='3', command=lambda : self.btn_press('3'))
        button4 = ttk.Button(self.buttonframe, text='4', command=lambda : self.btn_press('4'))
        button5 = ttk.Button(self.buttonframe, text='5', command=lambda : self.btn_press('5'))
        button6 = ttk.Button(self.buttonframe, text='6', command=lambda : self.btn_press('6'))
        button7 = ttk.Button(self.buttonframe, text='7', command=lambda : self.btn_press('7'))
        button8 = ttk.Button(self.buttonframe, text='8', command=lambda : self.btn_press('8'))
        button9 = ttk.Button(self.buttonframe, text='9', command=lambda : self.btn_press('9'))
        button0 = ttk.Button(self.buttonframe, text='0', command=lambda : self.btn_press('0'))
        button_pnt = ttk.Button(self.buttonframe, text='.', command=lambda : self.btn_press("."))
        button_add = ttk.Button(self.buttonframe, text='+', command=lambda : self.btn_press("+"))
        button_sub = ttk.Button(self.buttonframe, text='-', command=lambda : self.btn_press("-"))
        button_multi = ttk.Button(self.buttonframe, text='*', command=lambda : self.btn_press("*"))
        button_div = ttk.Button(self.buttonframe, text='/', command=lambda : self.btn_press("/"))
        button_eq = ttk.Button(self.buttonframe, text='=', command=self.eq_press)
        button_clr = ttk.Button(self.buttonframe, text='C', command=self.clr_press)
        button_ent = ttk.Button(self.buttonframe, text='↵', command=self.ent_press)
        
        # row 2
        button_div.grid(column=0, row=1)
        button_multi.grid(column=1, row=1)
        button_add.grid(column=2, row=1)
        button_sub.grid(column=3, row=1)
        button7.grid(column=0, row=2)
        button8.grid(column=1, row=2)
        button9.grid(column=2, row=2)
        
        # row 3
        button4.grid(column=0, row=3)
        button5.grid(column=1, row=3)
        button6.grid(column=2, row=3)
        
        # row 4
        button1.grid(column=0, row=4)
        button2.grid(column=1, row=4)
        button3.grid(column=2, row=4)
        button_ent.grid(column=3, row=4)
        
        # row 5
        button_pnt.grid(column=0, row=5)
        button0.grid(column=1, row=5)
        button_clr.grid(column=2, row=5)
        button_eq.grid(column=3, row=5)
        
        

        self.root.mainloop()

    def btn_press(self, num):
        '''sets the number value displayed when a key is pressed'''
        if len(self.eq) > 0:
            value = self.eq.pop()
            if value != '0':
                temp = value + num
                self.eq.append(temp)
            else:
                self.eq.append(num)
        else:
            self.eq.append(num)

        self.display_text.set(self.eq)

    def ent_press(self):
        '''Advances stack'''
        self.eq.append("")

    def clr_press(self):
        '''Clears the display'''
        self.eq.clear()
        self.display_text.set(self.eq)

    def eq_press(self):
        '''Gets values and executes equation'''
        num1 = int(self.eq[0])
        num2 = int(self.eq[1])
        op = self.eq[2]
        answer = 0

        answer = self.rpncalc.calculate(num1, num2, op)
        self.eq.clear()
        print(answer)
        self.eq.append(str(answer))
        self.display_text.set(self.eq)

