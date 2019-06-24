from graphics import *

def main():
    #introduction
    print("This program   plots the growth of a 10-year investment.")

    # Get principal and interest rate
    principal = float(input("enter the principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    #Create a graphics window label on lefth edge
    win = GraphWin("Investment growth chart", 1280,  960)
    win.setBackground("white")

    value = 0.0
    for y in range(920,0,-200):
        Text(Point(80, y), str(value)+" K").draw(win);
        value += 2.5



    # Drow bar for initial principal
    height = principal * 0.08
    bar = Rectangle(Point(160, 920), Point(260, 920-height))
    bar.setFill("green")
    bar.setWidth(8)
    bar.draw(win)

    # Drow bars for successive years
    for year in range(1,10+1):
        #calculate the value for the next year
        principal *= (1 + apr)
        # draw bar for this value
        xll = year * 100 + 160
        height = principal * 0.08
        bar = Rectangle(Point(xll, 920), Point(xll+100, 920-height))
        bar.setFill("green")
        bar.setWidth(8)
        bar.draw(win)


    input("Press <Enter to quit")
    win.close()
                                

    

main()
        
