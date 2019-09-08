
# * Importing Required Libraries
from datetime import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pytz import all_timezones, country_timezones, timezone

# * Creating and configuring the Root Window
root = Tk()
root.title('United States Clock')
root.resizable(0, 0)  # * To restrict resizing the window
root.config(bg='#075E54')

# * Function to display the window at the center of the screen
def center_window(w, h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# * Function to display Honolulu Time
def time01():
    honolulu = timezone('Pacific/Honolulu')
    de_time = datetime.now(honolulu)
    string_01 = de_time.strftime('%I:%M:%S %p \n %d-%b-%Y')
    lbl1.config(text=string_01, bg='#25D366',
                fg='black', borderwidth=2, relief='raised')  # 075E54
    lbl1.after(1000, time01)

# * Function to display Anchorage Time
def time02():
    anchorage = timezone('America/Anchorage')
    in_time = datetime.now(anchorage)
    string_02 = in_time.strftime('%I:%M:%S %p \n %d-%b-%Y')
    lbl2.config(text=string_02, bg='#075E54',
                fg='white', borderwidth=2, relief='raised')
    lbl2.after(1000, time02)

# * Function to display Los_Angeles Time
def time03():
    los_Angeles = timezone('America/Los_Angeles')
    de_time = datetime.now(los_Angeles)
    string_03 = de_time.strftime('%I:%M:%S %p \n %d-%b-%Y')
    lbl3.config(text=string_03, bg='#25D366',
                fg='black', borderwidth=2, relief='raised')  # 075E54
    lbl3.after(1000, time03)

# * Function to display SaltLakeCity Time
def time04():
    india = timezone('America/Denver')
    in_time = datetime.now(india)
    string_04 = in_time.strftime('%I:%M:%S %p \n %d-%b-%Y')
    lbl4.config(text=string_04, bg='#25D366',
                fg='black', borderwidth=2, relief='raised')
    lbl4.after(1000, time04)

# * Function to display Chicago Time
def time05():
    chicago = timezone('America/Chicago')
    in_time = datetime.now(chicago)
    string_05 = in_time.strftime('%I:%M:%S %p \n %d-%b-%Y')
    lbl5.config(text=string_05, bg='#075E54',
                fg='white', borderwidth=2, relief='raised')
    lbl5.after(1000, time05)

# * Function to display NewYork Time
def time06():
    newYork = timezone('America/New_York')
    in_time = datetime.now(newYork)
    string_06 = in_time.strftime('%I:%M:%S %p \n %d-%b-%Y')
    lbl6.config(text=string_06, bg='#25D366',
                fg='black', borderwidth=2, relief='raised')
    lbl6.after(1000, time06)

# * Function to display Phoenix Time
def time07():
    phoenix = timezone('America/Phoenix')
    in_time = datetime.now(phoenix)
    string_07 = in_time.strftime('%I:%M:%S %p \n %d-%b-%Y')
    lbl7.config(text=string_07, bg='#075E54',
                fg='white', borderwidth=2, relief='raised')
    lbl7.after(1000, time07)

lbl1 = Label(root, font=('calibri', 20, 'bold'))
lbl2 = Label(root, font=('calibri', 20, 'bold'))
lbl3 = Label(root, font=('calibri', 20, 'bold'))
lbl4 = Label(root, font=('calibri', 20, 'bold'))
lbl5 = Label(root, font=('calibri', 20, 'bold'))
lbl6 = Label(root, font=('calibri', 20, 'bold'))
lbl7 = Label(root, font=('calibri', 20, 'bold'))

# * Function Calls
center_window(255, 525)
time01()
time02()
time03()
time04()
time05()
time06()
time07()

# * Windows Size
widthValue = 100
heightValue = 65

# * Honolulu Flag Source and Configuration
img1 = Image.open('./Images/HonoluluFlag.png')
img1 = img1.resize((widthValue, heightValue), Image.ANTIALIAS)
photoImg1 = ImageTk.PhotoImage(img1)
panel1 = Label(root, image=photoImg1)
panel1.config(borderwidth=2, relief='raised')

# * Anchorage Flag Source and Configuration
img2 = Image.open('./Images/AnchorageFlag.png')
img2 = img2.resize((widthValue, heightValue), Image.ANTIALIAS)
photoImg2 = ImageTk.PhotoImage(img2)
panel2 = Label(root, image=photoImg2)
panel2.config(borderwidth=2, relief='raised')

# * Los Angeles Flag Source and Configuration
img3 = Image.open('./Images/LosAngelesFlag.png')
img3 = img3.resize((widthValue, heightValue), Image.ANTIALIAS)
photoImg3 = ImageTk.PhotoImage(img3)
panel3 = Label(root, image=photoImg3)
panel3.config(borderwidth=2, relief='raised')

# * SaltLakeCity Flag Source and Configuration
img4 = Image.open('./Images/SaltLakeCityFlag.png')
img4 = img4.resize((widthValue, heightValue), Image.ANTIALIAS)
photoImg4 = ImageTk.PhotoImage(img4)
panel4 = Label(root, image=photoImg4)
panel4.config(borderwidth=2, relief='raised')

# * Chicago Flag Source and Configuration
img5 = Image.open('./Images/ChicagoFlag.png')
img5 = img5.resize((widthValue, heightValue), Image.ANTIALIAS)
photoImg5 = ImageTk.PhotoImage(img5)
panel5 = Label(root, image=photoImg5)
panel5.config(borderwidth=2, relief='raised')

# * NewYork Flag Source and Configuration
img6 = Image.open('./Images/NewYorkFlag.png')
img6 = img6.resize((widthValue, heightValue), Image.ANTIALIAS)
photoImg6 = ImageTk.PhotoImage(img6)
panel6 = Label(root, image=photoImg6)
panel6.config(borderwidth=2, relief='raised')

# * Phoenix Flag Source and Configuration
img7 = Image.open('./Images/PhoenixFlag.png')
img7 = img7.resize((widthValue, heightValue), Image.ANTIALIAS)
photoImg7 = ImageTk.PhotoImage(img7)
panel7 = Label(root, image=photoImg7)
panel7.config(borderwidth=2, relief='raised')

# * Aligning the TKinter widgets in a Grid
panel1.grid(row=0, column=0, sticky=W, pady=2)
panel2.grid(row=1, column=0, sticky=W, pady=2)
panel3.grid(row=2, column=0, sticky=W, pady=2)
panel4.grid(row=4, column=0, sticky=W, pady=2)
panel5.grid(row=5, column=0, sticky=W, pady=2)
panel6.grid(row=6, column=0, sticky=W, pady=2)
panel7.grid(row=3, column=0, sticky=W, pady=2)

lbl1.grid(row=0, column=1, sticky=W, pady=2)
lbl2.grid(row=1, column=1, sticky=W, pady=2)
lbl3.grid(row=2, column=1, sticky=W, pady=2)
lbl4.grid(row=4, column=1, sticky=W, pady=2)
lbl5.grid(row=5, column=1, sticky=W, pady=2)
lbl6.grid(row=6, column=1, sticky=W, pady=2)
lbl7.grid(row=3, column=1, sticky=W, pady=2)

# * End of the Window
root.mainloop()
