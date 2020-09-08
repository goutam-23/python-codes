#wap to convert year into months,minute,hours,seconds,days.
import time
t=0
while(t<=5):
    t = t + 1
    yr=int(input("enter the year:"))
    print("1 for months.")
    print("2 for days.")
    print("3 for hours.")
    print("4 for minutes.")
    print("5 for seconds.")
    print("0 for exit.")
    ch=int(input("enter your choice:"))
    print("please wait for 2 sec.......")
    time.sleep(2)
    month=12*yr
    day=month*30
    day=day+yr*5
    hrs=day*24
    min=hrs*60
    sec=min*60
    if ch==1:
        print(f"{yr} years have {month} months.")
    elif ch==2:
        print(f"{yr} years have {day} days.")
    elif ch==3:
        print(f"{yr} years have {hrs} hours.")
    elif ch==4:
        print(f"{yr} years have {min} minutes.")
    elif ch==5:
        print(f"{yr} years have {sec} seconds.")
    elif ch==0:
        exit(0)
