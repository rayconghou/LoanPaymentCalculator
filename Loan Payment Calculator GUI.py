# Loan Payment Calculator GUI

import canBeConverted
import json
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

window = Tk()

window.geometry('400x150+150+150')
window.title('Loan Payment Calculator')

filenameroot = simpledialog.askstring('Loan Payment Calculator',
                'What is the root name of the file to save to?', parent=window)

if filenameroot == '' or filenameroot == None:

    filenameroot = 'loandata'

principalLabel = Label(window, text='Principal:')
principalLabel.grid(row=0, column=0)

interestRateLabel = Label(window, text='Interest Rate (%):')
interestRateLabel.grid(row=1, column=0)

termLabel = Label(window, text='Term (years):')
termLabel.grid(row=2, column = 0)

paymentLabel = Label(window, text='Monthly Payment:')
paymentLabel.grid(row=3, column=0)

principalEntryBox = Entry(window)
principalEntryBox.configure(width=20)
principalEntryBox.grid(row=0, column=1)
principalEntryBox.insert(0, '1000')

interestRateChoices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
interestRateVar = StringVar(window)

interestRateMenu = OptionMenu(window, interestRateVar, *interestRateChoices)
interestRateMenu.configure(width=25)
interestRateMenu.grid(row=1, column=1)
interestRateVar.set('5')

termEntryBox = Entry(window)
termEntryBox.configure(width=20)
termEntryBox.grid(row=2, column=1)
termEntryBox.insert(0, '1')

showPayment = Entry(window)
showPayment.grid(row=3, column=1)
showPayment.configure(width=25)
showPayment.config(state=DISABLED)

def calculatePayment():

    p = principalEntryBox.get()
    i_in_percent = interestRateVar.get()
    t_in_years =  termEntryBox.get()

    if canBeConverted.toReal(p) == False:
        messagebox.showerror('Invalid Data',
                'The principal value is invalid.')
        p = None
        
    elif canBeConverted.toReal(t_in_years) == False:
        messagebox.showerror('Invalid Data',
                'The term value is invalid.')
        t_in_years = None

    if p != None and t_in_years != None:

        i = float(i_in_percent) / 100.0
        t = float(t_in_years) * 12.0

        numerator = i * float(p)
        denominator = 1.0 - 1.0/(1.0 + i)**t

        monthly_payment = round(numerator / denominator, 2)

        s = '${:.2f}'.format(monthly_payment)

        showPayment.config(state=NORMAL)
        showPayment.delete(0, END)
        showPayment.insert(0, s)
        showPayment.config(state=DISABLED)

        with open(filenameroot + '.json', 'a') as f:

            d = {'principal': float(p), 'interest rate': float(i_in_percent),
                 'term': float(t_in_years), 'payment amount': monthly_payment}

            s = json.dumps(d)

            f.write(s + '\n')

calculateButton = Button(window, text='Calculate Payment',
                         command=calculatePayment)
calculateButton.configure(width=20)
calculateButton.grid(row=4, column=1)

mainloop()





                          
