# -*- coding: utf-8 -*-
# COPYRIGHT BVB-ASR[class: XII-B] @ 2022

import os
if os.name == 'posix':
    operating_system = "linux"
else:
    operating_system = "windows"

def ClearScreen():
    if operating_system.upper() == "LINUX":
        os.system('clear')
    else:
        os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main ():
    csv_file = pd.read_csv("C:/Users/pc/OneDrive/Desktop/Theatres CSV.csv")
from csv import reader
ClearScreen()

print("\n" + "#"*20 + " Movie Tickets Reservation Management System " + "#"*20 + "\n")
print("\nMENU :-->\n")

print("[1] Display Bookings")
print("[2] Now Showing Movies")
print("[3] Show Timings")
print("[4] Show Orders For Food And Beverages")
print("[5] Show Mode Of Reservation Of Tickets")
print("[6] Show Type Of Tickets")
print("[7] Show Amount Due For Each Customer")
print("[8] Add a Booking")
print("[9] Search Bookings by Name")
print("[10] Search Bookings by Screen Alloted")
print("[11] Search Bookings by Seat Number")
print("[12] Check Seats Available")
print("[13] Delete a Booking")
print("[14] Financial Graph [Line]")
print("[15] Financial Graph [Bar]")
print("[16] QUIT")

choice = int(input("\nEnter a choice : "))

if choice < 0 or choice > 16:
    ClearScreen()
    print("Wrong Choice !")
    main()


elif choice == 1:
        ClearScreen()
        print(csv_file)
        input("\n\nPress Enter to Continue...")
        main()


elif choice == 2:
        ClearScreen()
        showmovies = pd.read_csv("Theatres CSV.csv", usecols = ['Movie'])
        print(showmovies)


elif choice == 3:
        ClearScreen()
        showtimings = pd.read_csv("Theatres CSV.csv", usecols = ['Show Timings'])
        print(showtimings)


elif choice == 4:
        ClearScreen()
        showorders = pd.read_csv("Theatres CSV.csv", usecols = ['Order For Food And Beverages'])
        print(showorders)


elif choice == 5:
        ClearScreen()
        showmode = pd.read_csv("Theatres CSV.csv", usecols = ['Mode Of Reservation'])
        print(showmode)


elif choice == 6:
        ClearScreen()
        showtype = pd.read_csv("Theatres CSV.csv", usecols = ['Ticket'])
        print(showtype)


elif choice == 7:
        ClearScreen()
        showamountdue = pd.read_csv("Theatres CSV.csv", usecols = ['Amount Due'])
        print(showamountdue)


elif choice == 8:
        ClearScreen()
        fName = str(input("Enter First Name: "))
        lName = str(input("Enter Last Name : "))
        contact = int(input("Enter Contact Details : +91 "))
        emailid = int(input("Enter Email Address : "))
        movie = int(input("Movie : "))
        screen = int(input("Enter Screen Alloted : "))
        seat = int(input("Enter Seat No. Alloted : "))
        showtimings = int(input("Enter Show Timings [Format:HH:MM] : "))
        order = int(input("Enter Order Placed For Foods And Beverages : "))
        mode = int(input("Enter Mode Of Reservation : "))
        ticket = int(input("Enter Type Of Ticket : "))
        amountdue = int(input("Enter Amount Due : ₹ "))
        ClearScreen()
        csv_file = csv_file.append({"Customer's First Name":fName, "Customer's Last Name":lName, "Customer's Contact Number":contact, "Customer's Email Address":emailid , "Movie":movie , "Screen Alloted":screen , "Seat Alloted":seat , "Show Timings":showtimings , "Order For Food And Beverages":order , "Mode Of Reservation":mode , "Ticket":ticket , "Amount Due":amountdue}, ignore_index=True)
        csv_file.to_csv('hotel.csv', index = False)
        print("Record added.")
        input("Press Enter to Continue...")
        main()


elif choice == 9:
        ClearScreen()
        fName = str(input("Customer's First Name: "))
        condition = csv_file["Customer's First Name"] == fName
        ClearScreen()
        print(csv_file[condition].head())
        input("\n\nPress Enter to Continue...")
        main()


elif choice == 10:
        ClearScreen()
        fName = str(input("Enter Screen Number: "))
        condition = csv_file["Screen Alloted"] == screen
        ClearScreen()
        print(csv_file[condition].head())
        input("\n\nPress Enter to Continue...")
        main()

elif choice == 11:
        ClearScreen()
        fName = str(input("Enter Seat Number: "))
        condition = csv_file["Seat Alloted"] == seat
        ClearScreen()
        print(csv_file[condition].head())
        input("\n\nPress Enter to Continue...")
        main()


elif choice == 12:
        ClearScreen()
        seat = int(input("Enter Seat Number To Check For Availability : "))
        condition = csv_file['Seat Alloted'] == seat
        ClearScreen()
        empty_ = csv_file[condition].head()
        if str(empty_).splitlines()[0].upper() == 'EMPTY DATAFRAME':
            print(f"Seat Number : {seat} is Available.\nGo ahead for Bookings..")
        else:
            print(f"Seat Number : {seat} is Cccupied.\nTry another Seat..")
        input("\n\nPress Enter to Continue...")
        main()


elif choice == 13:
        ClearScreen()
        roomNo = int(input("Enter Seat No. To Be Made Available : ")) 
        csv_file = pd.read_csv("Theatres CSV.csv")
        csv_file = csv_file[csv_file['Seat'] != seatNo]
        csv_file.to_csv('Theatres CSV.csv', index = False)
        
        ClearScreen()

        print("Entry Deleted !")
        input("Press Enter to Continue...")
        main()


elif choice == 14:
        pl.ylabel('Amount Due')
        pl.xlabel("Seats")
        pl.plot(csv_file['Seat Alloted'],csv_file['Amount Due'])
        pl.title("Financial Graph")
        pl.show()

        ClearScreen()
        main()
        
elif choice == 15:
        pl.bar(csv_file['Seat Alloted'],csv_file['Amount Due'])
        pl.title('Financial Graph')
        pl.xlabel('Seats')
        pl.ylabel('Amount Due')
        pl.show()

        ClearScreen()
        main()





elif choice == 16:
        ClearScreen()
        print("BVB-ASR [Made By: Abhay Bagla; Class&Sec: XII-B] @ 2022\nThanks for Using!\n")
        exit(0)

if __name__ == "__main__":
    main()
