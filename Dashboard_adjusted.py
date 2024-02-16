#!/usr/bin/env python3

import tkinter as tk
import random
import os, sys, subprocess, threading, time, datetime, socket, select, webbrowser, base64, platform, base64, requests, hashlib, re
import PIL.Image, PIL.ImageTk
import datetime
import string
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from pymsgbox import *


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.serv = None
        self.withdraw()
        self.run_server()

    @staticmethod
    def get_random_datetime():
#        year = random.randint(2023, 2024)
#        month = random.randint(1, 12)
#        day = random.randint(1, 28)
#        hour = random.randint(0, 23)
#        minute = random.randint(0, 59)
#        second = random.randint(0, 59)
#        return datetime.datetime(year, month, day, hour, minute, second).strftime('%Y-%m-%d %H:%M:%S')
         ct = datetime.datetime.now()
         return (ct)
    
    def get_random_username(self):
        names = ["john_doe", "jane_smith", "bob_ross", "mary_jackson", "alexander", "emily", "sam_wilson", "lily_adams", "will_turner"]
        return random.choice(names)
    
    def get_random_os(self):
        os_options = ["Windows", "macOS", "Linux", "Unix"]
        return random.choice(os_options)
    
    def get_random_hostname(self):
        hostnames = ["example-host", "test-server", "data-center", "web-server", "local-machine", "production-01", "dev-machine"]
        return random.choice(hostnames)
    
    def get_random_key(self):
        key_length = 24
        characters = string.ascii_letters + string.digits
        key = ''.join(random.choice(characters) for i in range(key_length))
        return key
    
    def get_random_ip(self):
        return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    
    def get_random_continent(self):
        continents = ["North America", "Europe", "Asia", "South America", "Africa", "Australia"]
        return random.choice(continents)
    
    def get_random_country(self):
        countries = ["United States", "Canada", "United Kingdom", "Germany", "Australia", "Brazil", "India", "China", "Japan", "France"]
        return random.choice(countries)
    
    def display_random_details(self):
    
        for i in range(1, 5):
            details = {
                "\n\nOccurred": {"value": self.get_random_datetime()},
                "Username": {"value": self.get_random_username()},
                "Hostname": {"value": self.get_random_hostname()},
                "Key": {"value": self.get_random_key()},
                "Remote IP": {"value": self.get_random_ip()},
                "Local IP": {"value": self.get_random_ip()},
                "Continent": {"value": self.get_random_continent()},
                "Country": {"value": self.get_random_country()},
                
            }
    
            for field, data in details.items():
                log_entry = f"{field}: {data['value']}\n"
                log_label = f"log{i}"
                self.serv.options[log_label].insert("1.0", log_entry, "green")
                
                
            # Schedule the function to run again after a random time interval
            #time_interval = random.randint(2000, 2100)  # In milliseconds (3 to 6 seconds)
            #self.serv.after(time_interval, self.display_random_details)
        
    def increment_label_value_randomly(self, label):
        current_value = int(label["text"])
        new_value = current_value + 1
        label.config(text=str(new_value))

        labelname=f'{label}'
        if re.search("label6",labelname):
            #print("windows")
            time_interval = random.randint(5000, 10000)
        elif re.search("label7",labelname):
            #print("mac")
            time_interval = random.randint(20000, 50000)
        elif re.search("label8",labelname):
            #print("linux")
            time_interval = random.randint(10000, 20000)
        elif re.search("label9",labelname):
            #print("other")
            time_interval = random.randint(50000, 100000)    
        
        # Schedule the next increment after a random time interval
        #time_interval = random.randint(5000, 100000)  # In milliseconds (1 to 5 seconds)
        self.serv.after(time_interval, self.increment_label_value_randomly, label)
        self.display_random_details()

    def start_increment_randomly(self):
        # Call the increment_label_value_randomly function for each label with different time intervals
        self.serv.after(
            random.randint(5000, 10000),
            self.increment_label_value_randomly,
            self.serv.options["win"],
        )
        self.serv.after(
            random.randint(20000, 50000),
            self.increment_label_value_randomly,
            self.serv.options["mac"],
        )
        self.serv.after(
            random.randint(10000, 20000),
            self.increment_label_value_randomly,
            self.serv.options["linux"],
        )
        self.serv.after(
            random.randint(50000, 100000),
            self.increment_label_value_randomly,
            self.serv.options["other"],
        )

    def run_server(self):
        #self.set.destroy()
        self.serv = Toplevel()
        self.serv.title(string="Dashboard")
        self.serv.iconbitmap("images/title.ico")
        self.serv.configure(background="white")
        self.serv.resizable(True, True)
        self.serv.protocol("WM_DELETE_WINDOW", self.close_server_by_click)

        self.serv.bind("<Escape>", self.close_server)  # Press ESC to close window
        self.serv.geometry("+00+00")        
        # Input field data is being inserted in this dict
        self.serv.options = {
            "host": StringVar(),
            "port": IntVar(),
            "remote": StringVar(),
            "local": StringVar(),
            "platform": StringVar(),
            "key": StringVar(),
            "mac": IntVar(),
            "linux": IntVar(),
            "other": IntVar(),
        }

        # Canvas for image
        canvas = Canvas(
            self.serv, highlightthickness=0, height=150, width=500, background="white"
        )
        canvas.grid(row=0, column=0, columnspan=4)
        
     
        # photo = PIL.ImageTk.PhotoImage(PIL.Image.open(BytesIO(base64.b64decode(photo_code))))
        if platform.system() == "Linux":
            photo1 = Image.open(resource_path("images/windows.png"))
            resized = photo1.resize((75, 75), Image.LANCZOS)
            photo1 = PIL.ImageTk.PhotoImage(resized)
        else:
            photo1 = PIL.Image.open(resource_path("images/windows.png"))
            resized = photo1.resize((75, 75), PIL.Image.LANCZOS)
            photo1 = PIL.ImageTk.PhotoImage(resized)

        if platform.system() == "Linux":
            photo2 = Image.open(resource_path("images/mac.png"))
            resized = photo2.resize((75, 75), Image.LANCZOS)
            photo2 = PIL.ImageTk.PhotoImage(resized)
        else:
            photo2 = PIL.Image.open(resource_path("images/mac.png"))
            resized = photo2.resize((75, 75), PIL.Image.LANCZOS)
            photo2 = PIL.ImageTk.PhotoImage(resized)

        if platform.system() == "Linux":
            photo3 = Image.open(resource_path("images/linux.png"))
            resized = photo3.resize((75, 75), Image.LANCZOS)
            photo3 = PIL.ImageTk.PhotoImage(resized)
        else:
            photo3 = PIL.Image.open(resource_path("images/linux.png"))
            resized = photo3.resize((75, 75), PIL.Image.LANCZOS)
            photo3 = PIL.ImageTk.PhotoImage(resized)

        if platform.system() == "Linux":
            photo4 = Image.open(resource_path("images/other.png"))
            resized = photo4.resize((75, 75), Image.LANCZOS)
            photo4 = PIL.ImageTk.PhotoImage(resized)
        else:
            photo4 = PIL.Image.open(resource_path("images/other.png"))
            resized = photo4.resize((75, 75), PIL.Image.LANCZOS)
            photo4 = PIL.ImageTk.PhotoImage(resized)
            
        
        label_t = Label(self.serv, text="                                                                                            INFECTED TARGETS", foreground = 'red', font='arial 16 bold', background = 'white')
        label_t.grid(row = 0, column = 1)

        label = Label(self.serv, image=photo1, background="white")
        label.image = photo1  # keep a reference!
        label.grid(row=1, column=0, padx=200)

        label2 = Label(self.serv, image=photo2, background="white")
        label2.image = photo2  # keep a reference!
        label2.grid(row=1, column=1, padx=200)

        label3 = Label(self.serv, image=photo3, background="white")
        label3.image = photo3  # keep a reference!
        label3.grid(row=1, column=2, padx=200)

        label4 = Label(self.serv, image=photo4, background="white")
        label4.image = photo4  # keep a reference!
        label4.grid(row=1, column=3, padx=200)

        self.serv.options["win"] = Label(
            self.serv,
            text=0,
            background="white",
            foreground="red",
            font="Helvetica 16 bold",
        )
        self.serv.options["win"].grid(row=2, column=0, columnspan=1)
        self.serv.options["mac"] = Label(
            self.serv,
            text=0,
            background="white",
            foreground="red",
            font="Helvetica 16 bold",
        )
        self.serv.options["mac"].grid(row=2, column=1, columnspan=1)
        self.serv.options["linux"] = Label(
            self.serv,
            text=0,
            background="white",
            foreground="red",
            font="Helvetica 16 bold",
        )
        self.serv.options["linux"].grid(row=2, column=2, columnspan=1)
        self.serv.options["other"] = Label(
            self.serv,
            text=0,
            background="white",
            foreground="red",
            font="Helvetica 16 bold",
        )
        self.serv.options["other"].grid(row=2, column=3, columnspan=1)

        self.start_increment_randomly()

        # Log Frame
        result = LabelFrame(self.serv, text="Log", relief=GROOVE)
        result.grid(row=3, column=0, rowspan=4, columnspan=5)
        
        self.serv.options["log"] = Text(
            result,
            foreground="white",
            background="black",
            highlightcolor="white",
            highlightbackground="black",
            height=85,
            width=275,
        )
        self.serv.options["log"].grid(row=0, column=1)

        scroll = Scrollbar(self.serv, command=self.serv.options["log"].yview)
        scroll.grid(row=1, column=5, sticky="nsew")
        self.serv.options["log"]["yscrollcommand"] = scroll.set

        # Tags
        self.serv.options["log"].tag_configure("yellow", foreground="yellow")
        self.serv.options["log"].tag_configure("red", foreground="red")
        self.serv.options["log"].tag_configure("deeppink", foreground="deeppink")
        self.serv.options["log"].tag_configure("orange", foreground="orange")
        self.serv.options["log"].tag_configure("green", foreground="green")
        self.serv.options["log"].tag_configure("bold", font="bold")


        result1 = LabelFrame(self.serv, text="New Target Details", relief=GROOVE)
        result1.grid(row=4, column=0, rowspan=6, columnspan=5)
        
        self.serv.options["log1"] = Text(
            result1,
            foreground="yellow",
            background="black",
            highlightcolor="white",
            highlightbackground="black",
            height=40,
            width=68,
        )
        self.serv.options["log1"].grid(row=0, column=0, pady=5)
        self.serv.options["log2"] = Text(
            result1,
            foreground="yellow",
            background="black",
            highlightcolor="white",
            highlightbackground="black",
            height=40,
            width=68,
        )
        self.serv.options["log2"].grid(row=0, column=1)
        self.serv.options["log3"] = Text(
            result1,
            foreground="yellow",
            background="black",
            highlightcolor="white",
            highlightbackground="black",
            height=40,
            width=68,
        )
        self.serv.options["log3"].grid(row=0, column=2)
        self.serv.options["log4"] = Text(
            result1,
            foreground="yellow",
            background="black",
            highlightcolor="white",
            highlightbackground="black",
            height=40,
            width=68,
        )
        self.serv.options["log4"].grid(row=0, column=3)
       


        # scroll = Scrollbar(self.serv, command=self.serv.options["log"].yview)
        # scroll.grid(row=2, column=5, sticky="nsew")
        # self.serv.options["log1"]["yscrollcommand"] = scroll.set

        

        self.start_increment_randomly()

                
        
        
        
        self.insert_banner()
        
    def close_server_by_click(self):
        self.serv.destroy()

    def insert_banner(self):
        banner = """
Server started on port 8989 on host 127.0.0.1

                                                                                                                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                                                                                           @@@@@@@@@@@@@@@@@@*++*@@@@@@@@@@@@@@@@@@
                                                                                                                           @@@@@@@@@@@@@@%+: -++- :+%@@@@@@@@@@@@@@
                                                                                                                           @@@@@@@@@@@*-.:+#@@@@@@#=:.-*@@@@@@@@@@@
                                                                                                                           @@@@@@@%+: -*@@@@@@@@@@@@@@*- :+%@@@@@@@
                                                                                                                           @@@@@#..=#@@@@@@@@@@@@@@@@@@@@#=..#@@@@@
                                                                                                                           @@@@@ :@@@@@@@@@@@@@@@@@@@@@@@@@@: @@@@@
                                                                                                                           @@@@% -@@%::+%@@@@@@@@@@@@%+::%@@- %@@@@
                                                                                                                           @@@@% -@@@@%+:.=#@@@@@@*=.:+@@@@@- %@@@@
                                                                                                                           @@@@% -@@@@@@@@*-.-++-.=#@@@@@@@@- %@@@@
                                                                                                                           @@@@% -@@@@@@@@@@@%..%@@@@@@@@@@@- %@@@@
                                                                                                                           @@@@% -@@@@@@@@@@@@:-@@@@@@@@@@@@- %@@@@
                                                                                                                           @@@@% -@@@@@@@@@@@@:-@@@@@@@@@@@@- %@@@@
                                                                                                                           @@@@% :@@@@@@@@@@@@:-@@@@@@@@@@@@: %@@@@
                                                                                                                           @@@@@*.:+%@@@@@@@@@:-@@@@@@@@@%+..*@@@@@
                                                                                                                           @@@@@@@#+:.-*@@@@@@:-@@@@@@*-.:+%@@@@@@@
                                                                                                                           @@@@@@@@@@@*- :+%@@@@@@%+: -*@@@@@@@@@@@
                                                                                                                           @@@@@@@@@@@@@@#=..=**=..=#@@@@@@@@@@@@@@
                                                                                                                           @@@@@@@@@@@@@@@@@%*==*%@@@@@@@@@@@@@@@@@
                                                                                                                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

                                                                                                                          

                                                                                ____  _        _    ____ _  ______    _    ____ _____  _            ____      _    _   _ ____   ___  __  ____        ___    ____  _____ 
                                                                               | __ )| |      / \  / ___| |/ / __ )  / \  / ___|_   _|/ \          |  _ \    / \  | \ | / ___| / _ \|  \/  \ \      / / \  |  _ \| ____|
                                                                               |  _ \| |     / _ \| |   | ' /|  _ \ / _ \ \___ \ | | / _ \         | |_) |  / _ \ |  \| \___ \| | | | |\/| |\ \ /\ / / _ \ | |_) |  _|  
                                                                               | |_) | |___ / ___ \ |___| . \| |_) / ___ \ ___) || |/ ___ \        |  _ <  / ___ \| |\  |___) | |_| | |  | | \ V  V / ___ \|  _ <| |___ 
                                                                               |____/|_____/_/   \_\____|_|\_\____/_/   \_\____/ |_/_/   \_\       |_| \_\/_/   \_\_| \_|____/ \___/|_|  |_|  \_/\_/_/   \_\_| \_\_____|
                                                                                                                                    
                                                                                                                                     
                                                                                                                            
        """

        self.serv.options["log"].insert("1.0", banner + "\n", "red")
        
    def close_server(self, event):
        self.serv.destroy()


mm = MainWindow()
mm.mainloop()
