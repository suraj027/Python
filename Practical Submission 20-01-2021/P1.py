from tkinter import *


root=Tk()

photo=PhotoImage(file="NUV-Logo.png")
label=Label(root, image=photo)
label.pack()

label1=Label(root, text="Navrachana University").place(x=0, y=80)
label2=Label(root, text="Navrachana University is a Private University located in Vadodara, Gujarat. It was created by the state of Gujarat under the Private University Act, 2009.").place(x=0, y=100)
label3=Label(root, text="Address: Vasna - Bhayli Main Rd, Bhayli, Vadodara, Gujarat 391410").place(x=0, y=120)
label4=Label(root, text="Phone: 088822 06206").place(x=0, y=140)

root.mainloop()