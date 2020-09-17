#Project 1 - Loan Repayment Calculator
#It calculates the total amount paid and the time needed and plots it on a graph. If needed,
#it recalculate another set of values given and handle errors.
#reference:
#http://eecs.wsu.edu/~gcilingi/cpts111/LectureNotes/lecture_10_5_2011.txt
#http://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
#http://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index-in-python
#http://stackoverflow.com/questions/19501279/how-do-i-only-round-a-number-float-down-in-python
#http://stackoverflow.com/questions/22275255/applying-the-getmouse-function-to-one-part-of-the-window
#http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/graphics.html
#http://stackoverflow.com/questions/179369/how-do-i-abort-the-execution-of-a-python-script
#http://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed
#http://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
#https://groups.google.com/forum/#!msg/psychopy-users/Lr4LcZIF-K0/YH_Tnkyt8LUJ

from graphics import *
from sys import *
from math import *

def main():
#setting up the window
    win= GraphWin("Loan Repayments Calculator", 1100,500)
    win.setCoords(0,0,1200,500),win.setBackground(color_rgb(243,156,18))
    ipPrincip,ipRate, ipRamount, ipRfreq , calctxt, calcbutton= makeGUI(win) #drawing the main GUI
    button = 'false'
    while button == 'false': #while loop to repeat the calculation
        pClick = win.getMouse()
        button = isClicked(pClick,button)
        if button == 'calculate':#if button is pressed calculate
            try:#check for invalid entries and handle them
                P,r,a,f = getInputs(ipPrincip,ipRate, ipRamount, ipRfreq, win)
                if P > 0 and (f == 'M' or f == 'm') and r >= 0 and r <= 100:#check if frequency is monthly
                    if a > P*(r/100)*(30/365): #check if repayment is greater than interest
                        t, totalpaid, poly, text1 = loanVtime(P,r,a,f,win)
                        labels = makeLabels(poly,t,win,P,f)
                        drawLabels(win, labels)
                        undrawcont(calctxt, calcbutton)
                        finishtxt = Text(Point(150,50),"Please click 'Quit' when done or 'Reset'.")
                        finishtxt.draw(win),finishtxt.setSize(10),finishtxt.setFill(color_rgb(25,25,112))
                        againtxt,againbutton = tryagain(win)
                        while button != 'exit':#checking if user wants to repeat or exit
                            pClick = win.getMouse()
                            button = isClicked(pClick, button)
                            if button == 'continue':
                                undrawLabels(labels),undrawtryagain(againtxt,againbutton)
                                button = 'false'
                                text1.undraw(),finishtxt.undraw(),calcbutton.draw(win),calctxt.draw(win)
                                break
                            elif button == 'exit':
                                quitprogram(win)
                    else: #if repayment is less than interest it will tell the user the min.amount needed
                        undrawcont(calctxt, calcbutton)
                        mintxt, contbutton, conttxt = MminGUI(win,P,r)
                        while button != 'continue':#check if user wants to continue or exit
                            pClick = win.getMouse()
                            button = isClicked(pClick, button)
                            if button == 'exit':
                                quitprogram(win)
                        button = 'false'
                        undrawminGUI(mintxt, contbutton, conttxt, calcbutton, calctxt, win)
                elif P > 0 and (f == 'F' or f == 'f') and r >= 0 and r <= 100:#check if frequency is fortnightly
                    if a > P*(r/100)*(14/365):#check if repayment is greater than interest
                        undrawcont(calctxt, calcbutton)
                        t, totalpaid, poly, text1 = loanVtime(P,r,a,f,win)
                        labels = makeLabels(poly,t,win,P,f)
                        drawLabels(win,labels)
                        finishtxt = Text(Point(150,50),"Please click 'Quit' when done or 'Reset'.")
                        finishtxt.draw(win),finishtxt.setSize(10),finishtxt.setFill(color_rgb(25,25,112))
                        againtxt,againbutton = tryagain(win)
                        while button != 'exit':#checking if user wants to repeat or exit
                            pClick = win.getMouse()
                            button = isClicked(pClick, button)
                            if button == 'continue':
                                undrawLabels(labels),undrawtryagain(againtxt,againbutton)
                                button = 'false'
                                text1.undraw(),finishtxt.undraw(),calcbutton.draw(win),calctxt.draw(win)
                                break
                            elif button == 'exit':#if user wants to exit
                                quitprogram(win)
                    else:#if repayment is less than interest it will tell the user the min. amount needed
                        undrawcont(calctxt, calcbutton)
                        mintxt, contbutton, conttxt = FminGUI(win,P,r)
                        while button != 'continue':#check if user wants to continue or exit
                            pClick = win.getMouse()
                            button = isClicked(pClick, button)
                            if button == 'exit':#will close the window and end the program
                                quitprogram(win)
                        button = 'false'
                        undrawminGUI(mintxt, contbutton, conttxt, calcbutton, calctxt, win)
                else:
                    undrawcont(calctxt, calcbutton)
                    try:#handle errors with the inputs
                        invalidtxt, contbutton, conttxt = failGUI(win)
                        while button != 'continue':#check if user wants to continue or exit
                            pClick = win.getMouse()
                            button = isClicked(pClick, button)
                            if button == 'exit':#will close the window and end the program
                                quitprogram(win)
                        button = 'false'
                        undrawfailGUI(invalidtxt, contbutton, conttxt, calcbutton, calctxt, win)
                    except:
                        quitprogram(win)
            except TypeError:#handle errors with the inputs
                undrawcont(calctxt, calcbutton)
                invalidtxt, contbutton, conttxt = failGUI(win)
                while button != 'continue':#check if user wants to continue or exit
                    pClick = win.getMouse()
                    button = isClicked(pClick, button)
                    if button == 'exit':#will close the window and end the program
                        quitprogram(win)
                button = 'false'
                undrawfailGUI(invalidtxt, contbutton, conttxt, calcbutton, calctxt, win)
        elif button == 'exit':#to exit without calculating
            quitprogram(win)
        elif button == 'continue':#to nullify a button not present
            button = 'false'
    
def makeGUI(win):
#making the text
    loantxt = Text(Point(68.75,450.0), "Loan ($):")
    loantxt.setSize(10),loantxt.setFill(color_rgb(25,25,112))
    ratetxt = Text(Point(68.75,425.0), "Interest Rate (%):")
    ratetxt.setSize(10),ratetxt.setFill(color_rgb(25,25,112))
    repaymenttxt = Text(Point(68.75,400.0), "Repayment ($):")
    repaymenttxt.setSize(10),repaymenttxt.setFill(color_rgb(25,25,112))
    frequencytxt = Text(Point(68.75,375.0), "Freq.(M/F):")
    frequencytxt.setSize(10),frequencytxt.setFill(color_rgb(25,25,112))
#making the loan entry
    ipPrincip = Entry(Point(3*win.getWidth()/16,18*win.getHeight()/20), 16)
    ipPrincip.setText("0.0"),ipPrincip.setSize(10)
#making the interest rate entry
    ipRate = Entry(Point(3*win.getWidth()/16,17*win.getHeight()/20),16)
    ipRate.setText("0.0"),ipRate.setSize(10)
#making the repayment entry
    ipRamount = Entry(Point(3*win.getWidth()/16,16*win.getHeight()/20),16)
    ipRamount.setText("0.0"),ipRamount.setSize(10)
#making the frequency entry
    ipRfreq = Entry(Point(3*win.getWidth()/16,15*win.getHeight()/20),16)
    ipRfreq.setText("Monthly/Fortnightly"),ipRfreq.setSize(10)
#making button
    calcbutton = Rectangle(Point(win.getWidth()/32,14*win.getHeight()/20),Point(6*win.getWidth()/32,11*win.getHeight()/20))
    calcbutton.setFill(color_rgb(0,205,0))
    quitbutton = Rectangle(Point(win.getWidth()/32,10*win.getHeight()/20),Point(6*win.getWidth()/32,7*win.getHeight()/20))
    quitbutton.setFill("red")
    calctxt = Text(Point(((6*win.getWidth()/32)+(win.getWidth()/32))/2,((14*win.getHeight()/20)+(11*win.getHeight()/20))/2),"Calculate")
    calctxt.setStyle('bold'),calctxt.setTextColor(color_rgb(255,255,0)),calctxt.setSize(16)
    quittxt = Text(Point(((6*win.getWidth()/32)+(win.getWidth()/32))/2,((10*win.getHeight()/20)+(7*win.getHeight()/20))/2), "Quit")
    quittxt.setStyle('bold'),quittxt.setTextColor(color_rgb(255,255,0)),quittxt.setSize(16)
#drawing the GUI
    loantxt.draw(win),ratetxt.draw(win),repaymenttxt.draw(win),frequencytxt.draw(win)
    ipPrincip.draw(win),ipRate.draw(win),ipRamount.draw(win),ipRfreq.draw(win)
    calcbutton.draw(win),calctxt.draw(win)
    quitbutton.draw(win),quittxt.draw(win)
    return ipPrincip, ipRate, ipRamount, ipRfreq, calctxt, calcbutton

def getInputs(ipPrincip, ipRate, ipRamount, ipRfreq, win): #get the inputs and convert them into values whilst handling errors
    try:
        ipPrincip = float(ipPrincip.getText())
        ipRate = float(ipRate.getText())
        ipRamount = float(ipRamount.getText())
        ipRfreq = str(ipRfreq.getText())
        P,r,a,f = ipPrincip,ipRate, ipRamount, ipRfreq
        return P,r,a,f
    except:
        return

def isClicked(pClick, button): #check for which button is clicked and return a value
    if 37.5 < pClick.x < 225.0 and 350.0 > pClick.y > 275.0:
        button = 'calculate'
    elif 37.5 < pClick.x < 225.0 and 250.0 > pClick.y > 175.0:
        button = 'exit'
    elif 37.5 < pClick.x < 225.0 and 150.0 > pClick.y > 75.0:
        button = 'continue'
    else:
        button = 'false'
    return button

def loanVtime(P,r,a,f,win): #calculating the total repayment, time required and creating points on the graph
    t,totalpaid=0,0
    resize = P
    poly = [Point(win.getWidth()/3,50),Point(win.getWidth()/3,(P*400/resize)+50)]
    if f == "M":
        days = 30
    elif f == "F":
        days = 14
    elif f == "m":
        days = 30
    elif f == "f":
        days = 14
    while P >= 0:
        P = P +P*(r/100)*(days/365)-a
        t = t + days
        totalpaid = totalpaid + a
    totalpaid = int(totalpaid + P)
    P = resize
    value = t
    t = 0
    while P >= 0:#creating points of the graph
        P = P +P*(r/100)*(days/365)-a
        t = t + days
        poly.append(Point(t*(650/value)+(win.getWidth()/3),P*400/resize+50))
    del poly[-1]
    if P < 0:
        poly.append(Point(t*(650/value)+(win.getWidth()/3),0*400/resize+50))
    if t >365:#if total time for repayment is greater than a year
        y = str(int(t/365))
        m = str(int((t/365 - int(t/365))*12))
        d = str(round((t/365 - int(t/365))*365%30))
        p = str(round(totalpaid))
        text1= Text(Point(660,70), "It will take "+y+" years "+m+" months and "+d+" days to finish and you would have repaid $"+p+".")
        text1.setSize(10),text1.setFill(color_rgb(25,25,112))
        text1.draw(win)
    if t <= 365:#if total time for repayment is equal or less than a year
        d = str(t)
        p = str(round(totalpaid))
        text1=Text(Point(660,70), "It will take "+d+" days to finish and you would have repaid $"+p+".")
        text1.setSize(10),text1.setFill(color_rgb(25,25,112))
        text1.draw(win)
    return t, totalpaid, poly, text1

def makeLabels(poly,t,win,P,f): #making the graph and components
#making the graph
    graph = Polygon(poly)
    xaxis = Line(Point(win.getWidth()/3,50),Point((win.getWidth()/3)+800,50))
    xaxis.setFill('red')
    yaxis = Line(Point(win.getWidth()/3,50),Point(win.getWidth()/3,450))
    yaxis.setFill('red')
#storing objects in a list
    labels = []
    labels.append(graph),labels.append(yaxis),labels.append(xaxis)
#making the y-axis
    yincrease = round(P/10)
    ystart = 50
    ystatement = 0
    for ii in range(11):
        ystatement = str(ystatement)
        ytxt = Text(Point(win.getWidth()/3-50,ystart), "$"+ystatement)
        ytxt.setSize(10)
        ystatement = int(ystatement)
        labels.append(ytxt)
        yline = Line(Point(win.getWidth()/3,ystart),Point(win.getWidth()/3-10, ystart))
        yline.setFill('red')
        labels.append(yline)
        ystart = ystart + 400/10
        ystatement = ystatement +yincrease
#making the x-axis
    if f == "M":
        days = 30
    elif f == "m":
        days = 30
    elif f == "F":
        days = 14
    elif f == "f":
        days = 14
    xstart = win.getWidth()/3
    xstatement = 0
    if t > 365:#if total time for repayment is more than one year
        time = int(t/365)
        xincrease = 365*650/t
        for ii in range(time + 2):
            xtxt = Text(Point(xstart, 25), xstatement)
            xtxt.setSize(8)
            labels.append(xtxt)
            xline = Line(Point(xstart, 50), Point(xstart,40))
            xline.setFill('red')
            labels.append(xline)
            xstart = xstart + xincrease
            xstatement = xstatement + 1
        xlabel = Text(Point(750,10), "No. of Years")
        xlabel.setSize(8)
        labels.append(xlabel)
    elif t < 365:#if total time for repayment is less than one year
        time = int(t/days) 
        xincrease = days*650/t
        for ii in range(time+1):            
            xtxt = Text(Point(xstart, 25), xstatement)
            xtxt.setSize(8)
            labels.append(xtxt)
            xline = Line(Point(xstart, 50), Point(xstart,40))
            xline.setFill('red')
            labels.append(xline)
            xstart = xstart + xincrease
            xstatement = xstatement + days
        xlabel = Text(Point(750, 10), "No. of Days")
        xlabel.setSize(8)
        labels.append(xlabel)
    return labels

def drawLabels(win, labels): #drawing the graph and components
    for ii in range(len(labels)):
        labels[ii].draw(win)

def undrawLabels(labels): #undrawing the graph
    for ii in range(len(labels)):
        labels[ii].undraw()
        
#additional functions to handle errors
def tryagain(win):
    againbutton = Rectangle(Point(win.getWidth()/32,6*win.getHeight()/20),Point(6*win.getWidth()/32,3*win.getHeight()/20))
    againbutton.setFill(color_rgb(0,205,0))
    againtxt = Text(Point(((6*win.getWidth()/32)+(win.getWidth()/32))/2,((6*win.getHeight()/20)+(3*win.getHeight()/20))/2), "Reset")
    againtxt.setStyle('bold'),againtxt.setTextColor(color_rgb(255,255,0)),againtxt.setSize(16)
    againbutton.draw(win),againtxt.draw(win)
    return againtxt,againbutton

def undrawtryagain(againtxt,againbutton):
    againtxt.undraw(),againbutton.undraw()

def failGUI(win):
    invalidtxt = Text(Point(150,45),"Invalid value/s.\nPlease try again.\n Please click 'Continue' to proceed or 'Quit'.")
    invalidtxt.setSize(10),invalidtxt.setFill(color_rgb(25,25,112))
    contbutton = Rectangle(Point(win.getWidth()/32,6*win.getHeight()/20),Point(6*win.getWidth()/32,3*win.getHeight()/20))
    contbutton.setFill(color_rgb(0,205,0))
    conttxt = Text(Point(((6*win.getWidth()/32)+(win.getWidth()/32))/2,((6*win.getHeight()/20)+(3*win.getHeight()/20))/2), "Continue")
    conttxt.setStyle('bold'),conttxt.setTextColor(color_rgb(255,255,0)),conttxt.setSize(16)
#drawing GUI for errors
    invalidtxt.draw(win),contbutton.draw(win),conttxt.draw(win)
    return invalidtxt, contbutton, conttxt

def undrawfailGUI(invalidtxt, contbutton, conttxt, calcbutton, calctxt, win):
    invalidtxt.undraw(),contbutton.undraw(),conttxt.undraw(),calcbutton.draw(win),calctxt.draw(win)

def quitprogram(win):
    win.close(),sys.exit()

def undrawcont(calctxt, calcbutton):
    calctxt.undraw(),calcbutton.undraw()

def MminGUI(win,P,r):#handle interest > repayment for monthly error
#making statement for error
    minamountneeded = str(ceil(P*(r/100)*(30/365)))
    mintxt = Text(Point(150,45),"Unable to repay. Amount repay >= "+minamountneeded+"\nPlease try again.\n Please click continue to proceed.")
    mintxt.setSize(10),mintxt.setFill(color_rgb(25,25,112))
    contbutton = Rectangle(Point(win.getWidth()/32,6*win.getHeight()/20),Point(6*win.getWidth()/32,3*win.getHeight()/20))
    contbutton.setFill(color_rgb(0,205,0))
    conttxt = Text(Point(((6*win.getWidth()/32)+(win.getWidth()/32))/2,((6*win.getHeight()/20)+(3*win.getHeight()/20))/2), "Continue")
    conttxt.setStyle('bold'),conttxt.setTextColor(color_rgb(255,255,0)),conttxt.setSize(16)
#drawing statements
    mintxt.draw(win),contbutton.draw(win),conttxt.draw(win)
    return mintxt, contbutton, conttxt

def undrawminGUI(mintxt, contbutton, conttxt, calcbutton, calctxt, win):
    mintxt.undraw(),contbutton.undraw(),conttxt.undraw(),calcbutton.draw(win),calctxt.draw(win)

def FminGUI(win,P,r):#handle interest > repayment for fortnightly error
#making statement for error
    minamountneeded = str(ceil(P*(r/100)*(14/365)))
    mintxt = Text(Point(150,45),"Unable to repay. Amount repay >= "+minamountneeded+"\nPlease try again.\n Please click continue to proceed.")
    mintxt.setSize(10),mintxt.setFill(color_rgb(25,25,112))
    contbutton = Rectangle(Point(win.getWidth()/32,6*win.getHeight()/20),Point(6*win.getWidth()/32,3*win.getHeight()/20))
    contbutton.setFill(color_rgb(0,205,0))
    conttxt = Text(Point(((6*win.getWidth()/32)+(win.getWidth()/32))/2,((6*win.getHeight()/20)+(3*win.getHeight()/20))/2), "Continue")
    conttxt.setStyle('bold'),conttxt.setTextColor(color_rgb(255,255,0)),conttxt.setSize(16)
#drawing statements
    mintxt.draw(win),contbutton.draw(win),conttxt.draw(win)
    return mintxt, contbutton, conttxt
    
main()
