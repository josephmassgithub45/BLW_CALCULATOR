from tkinter import *

window=Tk()

#OUTPUT
output=Frame(window,bg='grey',width=400,height=75)
output.grid(row=0,columnspan=4)


#BUTTONROW 1
button1=Button(window,text='7',width=7,height=3,font='times 17 bold ',bg='lightblue')
button1.grid(row=1,column=0)

button2=Button(window,text='8',width=7,height=3,font='times 17 bold ',bg='lightblue')
button2.grid(row=1,column=1)

button3=Button(window,text='9',width=7,height=3,font='times 17 bold ',bg='lightblue')
button3.grid(row=1,column=2)

button4=Button(window,text='/',width=7,height=3,font='times 17 bold ',bg='lightblue')    
button4.grid(row=1,column=3)


#BUTTONROW 2
button5=Button(window,text='4',width=7,height=3,font='times 17 bold ',bg='lightblue')
button5.grid(row=2,column=0)

button6=Button(window,text='5',width=7,height=3,font='times 17 bold ',bg='lightblue')
button6.grid(row=2,column=1)

button7=Button(window,text='6',width=7,height=3,font='times 17 bold ',bg='lightblue')
button7.grid(row=2,column=2)

button8=Button(window,text='+',width=7,height=3,font='times 17 bold ',bg='lightblue')    
button8.grid(row=2,column=3)


#BUTTONROW 3
button9=Button(window,text='1',width=7,height=3,font='times 17 bold ',bg='lightblue')
button9.grid(row=3,column=0)

button10=Button(window,text='2',width=7,height=3,font='times 17 bold ',bg='lightblue')
button10.grid(row=3,column=1)

button11=Button(window,text='3',width=7,height=3,font='times 17 bold ',bg='lightblue')
button11.grid(row=3,column=2)

button12=Button(window,text='-',width=7,height=3,font='times 17 bold ',bg='lightblue')    
button12.grid(row=3,column=3)


#BUTTONROW 4
button13=Button(window,text='C',width=7,height=3,font='times 17 bold ',bg='lightblue')
button13.grid(row=4,column=0)

button14=Button(window,text='%',width=7,height=3,font='times 17 bold ',bg='lightblue')
button14.grid(row=4,column=1)

button15=Button(window,text='!',width=7,height=3,font='times 17 bold ',bg='lightblue')
button15.grid(row=4,column=2)

button16=Button(window,text='x',width=7,height=3,font='times 17 bold ',bg='lightblue')    
button16.grid(row=4,column=3)

#LOWER BUTTONS
#LOWER BUTTONS
#LOWER BUTTONS

#BUTTONROW 1
button1=Button(window,text='7',width=5,height=2,font='times 17 bold ',bg='lightblue')
button1.grid(row=1,column=0)

button2=Button(window,text='8',width=5,height=2,font='times 17 bold ',bg='lightblue')
button2.grid(row=1,column=1)

button3=Button(window,text='9',width=5,height=2,font='times 17 bold ',bg='lightblue')
button3.grid(row=1,column=2)

button4=Button(window,text='/',width=5,height=2,font='times 17 bold ',bg='lightblue')    
button4.grid(row=1,column=3)


#BUTTONROW 2
button5=Button(window,text='4',width=5,height=2,font='times 17 bold ',bg='lightblue')
button5.grid(row=2,column=0)

button6=Button(window,text='5',width=5,height=2,font='times 17 bold ',bg='lightblue')
button6.grid(row=2,column=1)

button7=Button(window,text='6',width=5,height=2,font='times 17 bold ',bg='lightblue')
button7.grid(row=2,column=2)

button8=Button(window,text='+',width=5,height=2,font='times 17 bold ',bg='lightblue')    
button8.grid(row=2,column=3)


#BUTTONROW 3
button9=Button(window,text='1',width=5,height=2,font='times 17 bold ',bg='lightblue')
button9.grid(row=3,column=0)

button10=Button(window,text='2',width=5,height=2,font='times 17 bold ',bg='lightblue')
button10.grid(row=3,column=1)

button11=Button(window,text='3',width=5,height=2,font='times 17 bold ',bg='lightblue')
button11.grid(row=3,column=2)

button12=Button(window,text='-',width=5,height=2,font='times 17 bold ',bg='lightblue')    
button12.grid(row=3,column=3)


#BUTTONROW 4
button13=Button(window,text='C',width=5,height=2,font='times 17 bold ',bg='lightblue')
button13.grid(row=4,column=0)

button14=Button(window,text='%',width=5,height=2,font='times 17 bold ',bg='lightblue')
button14.grid(row=4,column=1)

button15=Button(window,text='!',width=5,height=2,font='times 17 bold ',bg='lightblue')
button15.grid(row=4,column=2)

button16=Button(window,text='x',width=5,height=2,font='times 17 bold ',bg='lightblue')    
button16.grid(row=4,column=3)


window.mainloop()