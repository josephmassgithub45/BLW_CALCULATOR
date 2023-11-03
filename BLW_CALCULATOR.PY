from tkinter import *

class Calculator:
    def __init__(self,title,colour):
        self.titlename=title
        self.colour=colour

    def home_page(c):
        c.window=Tk()
        c.window.title(c.titlename)
        c.window.configure(background=c.colour)

        #OUTPUT
        output=Frame(c.window,bg='grey',width=400,height=75)
        output.grid(row=0,columnspan=4)


        #BUTTONROW 1
        button1=Button(c.window,text='7',width=7,height=3,font='times 17 bold ',bg='lightblue')
        button1.grid(row=1,column=0)

        button2=Button(c.window,text='8',width=7,height=3,font='times 17 bold ',bg='lightblue')
        button2.grid(row=1,column=1)

        button3=Button(c.window,text='9',width=7,height=3,font='times 17 bold ',bg='lightblue')
        button3.grid(row=1,column=2)

        button4=Button(c.window,text='/',width=7,height=3,font='times 17 bold ',bg='lightblue')    
        button4.grid(row=1,column=3)


        #BUTTONROW 2
        button5=Button(c.window,text='4',width=7,height=3,font='times 17 bold ',bg='lightblue')
        button5.grid(row=2,column=0)

        button6=Button(c.window,text='5',width=7,height=3,font='times 17 bold ',bg='lightblue')
        button6.grid(row=2,column=1)

        button7=Button(c.window,text='6',width=7,height=3,font='times 17 bold ',bg='lightblue')
        button7.grid(row=2,column=2)

        button8=Button(c.window,text='+',width=7,height=3,font='times 17 bold ',bg='lightblue')    
        button8.grid(row=2,column=3)


        #BUTTONROW 3
        button9=Button(c.window,text='1',width=7,height=3,font='times 17 bold ',bg='lightblue')
        button9.grid(row=3,column=0)

        button10=Button(c.window,text='2',width=7,height=3,font='times 17 bold ',bg='lightblue')
        button10.grid(row=3,column=1)

        button11=Button(c.window,text='3',width=7,height=3,font='times 17 bold ',bg='lightblue')
        button11.grid(row=3,column=2)

        button12=Button(c.window,text='-',width=7,height=3,font='times 17 bold ',bg='lightblue')    
        button12.grid(row=3,column=3)


        #BUTTONROW 4
        button13=Button(c.window,text='C',width=7,height=3,font='times 17 bold ',bg='lightblue')
        button13.grid(row=4,column=0)

        button14=Button(c.window,text='%',width=7,height=3,font='times 17 bold ',bg='lightblue')
        button14.grid(row=4,column=1)

        button15=Button(c.window,text='!',width=7,height=3,font='times 17 bold ',bg='lightblue')
        button15.grid(row=4,column=2)

        button16=Button(c.window,text='x',width=7,height=3,font='times 17 bold ',bg='lightblue')    
        button16.grid(row=4,column=3)

        #LOWER BUTTONS
        #LOWER BUTTONS
        #LOWER BUTTONS

        #BUTTONROW 1
        button1=Button(c.window,text='7',width=5,height=2,font='times 17 bold ',bg='lightblue')
        button1.grid(row=1,column=0)

        button2=Button(c.window,text='8',width=5,height=2,font='times 17 bold ',bg='lightblue')
        button2.grid(row=1,column=1)

        button3=Button(c.window,text='9',width=5,height=2,font='times 17 bold ',bg='lightblue')
        button3.grid(row=1,column=2)

        button4=Button(c.window,text='/',width=5,height=2,font='times 17 bold ',bg='lightblue')    
        button4.grid(row=1,column=3)


        #BUTTONROW 2
        button5=Button(c.window,text='4',width=5,height=2,font='times 17 bold ',bg='lightblue')
        button5.grid(row=2,column=0)

        button6=Button(c.window,text='5',width=5,height=2,font='times 17 bold ',bg='lightblue')
        button6.grid(row=2,column=1)

        button7=Button(c.window,text='6',width=5,height=2,font='times 17 bold ',bg='lightblue')
        button7.grid(row=2,column=2)

        button8=Button(c.window,text='+',width=5,height=2,font='times 17 bold ',bg='lightblue')    
        button8.grid(row=2,column=3)


        #BUTTONROW 3
        button9=Button(c.window,text='1',width=5,height=2,font='times 17 bold ',bg='lightblue')
        button9.grid(row=3,column=0)

        button10=Button(c.window,text='2',width=5,height=2,font='times 17 bold ',bg='lightblue')
        button10.grid(row=3,column=1)

        button11=Button(c.window,text='3',width=5,height=2,font='times 17 bold ',bg='lightblue')
        button11.grid(row=3,column=2)

        button12=Button(c.window,text='-',width=5,height=2,font='times 17 bold ',bg='lightblue')    
        button12.grid(row=3,column=3)


        #BUTTONROW 4
        button13=Button(c.window,text='C',width=5,height=2,font='times 17 bold ',bg='lightblue')
        button13.grid(row=4,column=0)

        button14=Button(c.window,text='%',width=5,height=2,font='times 17 bold ',bg='lightblue')
        button14.grid(row=4,column=1)

        button15=Button(c.window,text='!',width=5,height=2,font='times 17 bold ',bg='lightblue')
        button15.grid(row=4,column=2)

        button16=Button(c.window,text='x',width=5,height=2,font='times 17 bold ',bg='lightblue')    
        button16.grid(row=4,column=3)

        c.window.mainloop()

calculator=Calculator('BLUE LIGHT WAVES','BLUE')
calculator.home_page()
