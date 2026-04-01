from customtkinter import *
from tkinter import messagebox
from PIL import Image
import random
import sys
import os
def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, path)

#categories------------------------------------------------------------
#sports
sports = [
"Lamborghini","Ferrari","Bugatti","BMW","Audi","Mercedes-Benz","Porsche",
"Toyota","Honda","Hyundai","Kia","Maruti Suzuki","Tata Motors","Mahindra","Renault",
"Volkswagen","Nissan","Ford","Chevrolet","Jeep","Rolls-Royce","Bentley",
"McLaren","Pagani","Koenigsegg","Aston Martin","Jaguar","Land Rover","Volvo","Skoda"
]
# countries_states
countries_states = [
"Uttar Pradesh","Maharashtra","Bihar","Rajasthan","Madhya Pradesh",
"West Bengal","Karnataka","Tamil Nadu","Gujarat","Punjab",
"Haryana","Odisha","Kerala","Assam","Jharkhand","India",
"United States","United Kingdom","Canada","Australia","Germany","Japan",

"China","Russia","France","Italy","Spain","Brazil","Mexico","Indonesia",
"South Africa","Argentina","Netherlands","Switzerland","Sweden","Norway",
"Denmark","Finland","New Zealand","Singapore","Thailand","Vietnam"
]
# Games
games = [
"Minecraft","Free Fire","PUBG","Fortnite","Call of Duty",
"GTA V","Roblox","Valorant","Among Us","Clash Royale",
"BGMI","FIFA","Need for Speed","Subway Surfers",

"Apex Legends","Cyberpunk 2077","Elden Ring","Skyrim","Doom",
"Halo","NBA 2K","Clash of Clans","Brawl Stars","Terraria",
"Stardew Valley","Overwatch","Rocket League","Fall Guys",
"Battlefield","Far Cry","Assassin's Creed","Hitman","Resident Evil","The Witcher 3"
]

#Animals
animals = [
"Tiger","Lion","Elephant","Giraffe","Zebra","Monkey","Kangaroo","Panda","Bear","Wolf",
"Fox","Deer","Leopard","Cheetah","Hyena","Rhinoceros","Hippopotamus","Buffalo","Camel","Horse",
"Donkey","Goat","Sheep","Cow","Dog","Cat","Rabbit","Squirrel","Rat","Mouse",
"Bat","Otter","Koala","Sloth","Chimpanzee","Gorilla","Jaguar","Panther","Lynx","Moose",
"Reindeer","Walrus","Seal","Dolphin","Whale","Shark","Octopus","Penguin","Ostrich","Peacock"
]

# variable define
cm_choice = "Random"
cp_finalchoice = ""
attempts = 1
# functions
def category_choice1_func():
    global cm_choice
    cm_choice = "games"
    category_win.destroy()
    category_win.after(1000,open_singleplayer())

def category_choice2_func():
    global cm_choice
    cm_choice = "sports"
    category_win.destroy()
    category_win.after(1000,open_singleplayer())

def category_choice3_func():
    global cm_choice
    cm_choice = "countries_states"
    category_win.destroy()
    category_win.after(1000,open_singleplayer())

def category_choice4_func():
    global cm_choice
    cm_choice = "animals"
    category_win.destroy()
    category_win.after(1000,open_singleplayer())
def category_choice5_func():
    global cm_choice
    cm_choice="Random"
    category_win.withdraw()
    category_win.after(1000,open_singleplayer())

#starting windows

win = CTk(fg_color=("#0A0A1A"))
win.title("Hangman")
win.attributes("-fullscreen",True)
win.geometry("1000x800")
win.resizable(True,True)
lbl_textseen = None
# function
def open_singleplayer():
    global var2
    global lbl_textseen   
    global cp_finalchoice
    global design
    global stage_label
    global wrong_wrd
    if cm_choice=="sports":
        cp_finalchoice = random.choice(sports)
    elif cm_choice=="countries_states":
        cp_finalchoice = random.choice(countries_states)
    elif cm_choice=="games":
        cp_finalchoice = random.choice(games)
    elif cm_choice=="animals":
        cp_finalchoice = random.choice(animals)
    elif cm_choice=="Random":
        random_cat = random.choice(["sports","games","countries_states","animals"])
        if random_cat=="sports":
            cp_finalchoice = random.choice(sports)
        elif random_cat=="games":
            cp_finalchoice = random.choice(games)
        elif random_cat=="countries_states":
            cp_finalchoice = random.choice(countries_states)
        elif random_cat=="animals":
            cp_finalchoice = random.choice(animals)
        else:
            messagebox.showerror("Error","An Internal Error Ocurred")
    else:
        messagebox.showerror("Error","An Internal Error Ocurred")
    design = []
    for i in range(0,len(cp_finalchoice)):
        if cp_finalchoice[i] == " ":
            design.append(" ")
        else:
            design.append("_")
    sp_win = CTkToplevel(win)
    sp_win.configure(fg_color=("#0A0A1A"))
    stage_img = CTkImage(dark_image=Image.open(resource_path("stage1.png")), size=(450,370))
    stage_label = CTkLabel(sp_win, image=stage_img, text="",fg_color="#0A0A1A",bg_color="#0A0A1A",height=100,width=100)
    stage_label.image = stage_img
    stage_label.place(x=1000, y=80)
    var2= StringVar(master=sp_win)
    sp_win.title("Hangman")
    sp_win.resizable(True,True)
    sp_win.attributes("-fullscreen",True)
    logo3_my_img = CTkImage(dark_image=Image.open("hgman1.png"),
                            size=(700,450))
    lbl2 = CTkLabel(sp_win,image=logo3_my_img,text="",
                            bg_color="#0A0A1A")
    lbl2.image = logo3_my_img
    lbl2.place(x=300,y=-80)
    lbl_category = CTkLabel(sp_win,
                            text=f"Category = {cm_choice}",
                            fg_color="#FF3333",
                            text_color="white",
                            font=("consolas",35,"bold"),
                            corner_radius=10,
                            width=40,height=15)
    
    lbl_category.place(x=150,y=440)
    lbl_textseen = CTkLabel(sp_win,
                            text=" ".join(design),
                            text_color="white",
                            fg_color="#0A0A1A",
                            font=("consolas",50,"bold"))
    lbl_textseen.place(x=150,y=500)

    taken_entvalue = CTkEntry(sp_win,
                              textvariable=var2,
                              placeholder_text="Enter The Text",
                              width=300,height=22,
                              corner_radius=10,
                              font=("Arial",40,"bold"),
                              fg_color="#8B0000",
                              text_color="white") 
    taken_entvalue.place(x=900,y=520)

    wrong_wrd_lbl = CTkLabel(sp_win,
                    text="Typed Words : ",
                    fg_color="#0A0A1A",
                    text_color="white",
                    font=("consolas",35,"bold"),
                    corner_radius=10,
                    width=10,height=15)
    wrong_wrd_lbl.place(x=280,y=700)

    wrong_wrd = CTkLabel(sp_win,text="",
                    width=300,
                    height=60,
                    text_color="white",
                    font=("consolas",40,"bold"),
                    corner_radius=15,
                    fg_color="#8B0000",
                    )
    wrong_wrd.place(x=280,y=750)

    smt_btn = CTkButton(sp_win,
                    text="Submit",
                    width=200,
                    height=60,
                    text_color="white",
                    font=("consolas",30,"bold"),
                    cursor="hand2",
                    corner_radius=15,
                    fg_color="#8B0000",
                    hover_color="#FF3333",
                    command=main
                    )
    smt_btn.place(x=750,y=650)
    
# functions
def main():
    global lbl_textseen
    global attempts
    global stage_label
    global wrong_wrd
    userword = var2.get().lower()
    var2.set("")
    # main body
    if len(userword) == 1:
        if userword in cp_finalchoice.lower():
            wrong_wrd.configure(text=f"""{userword}""")
            for i in range(0,len(cp_finalchoice)):
                if cp_finalchoice[i].lower() == userword:
                    design[i] = userword
                    lbl_textseen.configure(text=" ".join(design), text_color="green")
        else:
            messagebox.showerror("Error","You Guess The Wrong Word")
            attempts= attempts+1
            current = wrong_wrd.cget("text")

            # string ko list me convert
            letters = current.replace(" ", "").split(",")

            if userword not in letters:
                if current == "":
                    wrong_wrd.configure(text=userword)
                else:
                    wrong_wrd.configure(text=current + "," + userword)
            if attempts == 2:
                stage_no = 2
                img_path = f"stage{stage_no}.png"
                new_img = CTkImage(
                    dark_image=Image.open(resource_path(img_path)),
                    size=(350,250)
                )
                stage_label.configure(image=new_img)
                stage_label.image = new_img

            elif attempts == 3:
                stage_no = 3
                img_path = f"stage{stage_no}.png"
                new_img = CTkImage(
                    dark_image=Image.open(resource_path(img_path)),
                    size=(350,250)
                )
                stage_label.configure(image=new_img)
                stage_label.image = new_img

            elif attempts == 4:
                stage_no = 4
                img_path = f"stage{stage_no}.png"
                new_img = CTkImage(
                    dark_image=Image.open(resource_path(img_path)),
                    size=(350,250)
                )
                stage_label.configure(image=new_img)
                stage_label.image = new_img

            elif attempts == 5:
                stage_no = 5
                img_path = f"stage{stage_no}.png"
                new_img = CTkImage(
                        dark_image=Image.open(resource_path(img_path)),
                        size=(350,250)
                )
                stage_label.configure(image=new_img)
                stage_label.image = new_img

            elif attempts == 6:
                stage_no = 6
                img_path = f"stage{stage_no}.png"
                new_img = CTkImage(
                        dark_image=Image.open(resource_path(img_path)),
                        size=(350,250)
                )
                stage_label.configure(image=new_img)
                stage_label.image = new_img

            elif attempts == 7:
                stage_no = 7
                img_path = f"stage{stage_no}.png"
                new_img = CTkImage(
                        dark_image=Image.open(resource_path(img_path)),
                        size=(350,250)
                )
                stage_label.configure(image=new_img)
                stage_label.image = new_img

            elif attempts == 8:
                stage_no = 8
                img_path = f"stage{stage_no}.png"
                new_img = CTkImage(
                        dark_image=Image.open(resource_path(img_path)),
                        size=(350,250)
                )
                stage_label.configure(image=new_img)
                stage_label.image = new_img
                messagebox.showerror("Lose",f"You Will Lose The coorect word is {cp_finalchoice} ")

            
            # 💀 GAME OVER
            if attempts <= 0:
                messagebox.showerror("Game Over", f"Word was: {cp_finalchoice}")
            
    else:
        messagebox.showerror("Error","Pls Type Only One Word")
# category choosen function
def category():
    global category_win
    win.withdraw()
    category_win = CTkToplevel(win)
    category_win.configure(fg_color="#0A0A1A")
    category_win.title("Hangman")
    category_win.geometry("1000x800")
    category_win.attributes("-fullscreen",True)
    category_win.resizable(True,True)
    logo2_my_img = CTkImage(dark_image=Image.open(resource_path("hgman1.png")),size=(900,520))
    lbl1 = CTkLabel(category_win,image=logo2_my_img,text="",bg_color="#0A0A1A")
    lbl1.image = logo2_my_img
    lbl1.place(x=300,y=-100)

    category_label = CTkLabel(category_win,text="Choose The One Category : ",corner_radius=10,width=30,height=10,font=("consolas",45,"bold"),fg_color="white")
    category_label.place(x=210,y=250)

    category_choice1 = CTkButton(category_win,
    text="Games",
    width=200,
    height=60,
    text_color="white",
    font=("consolas",35,"bold"),
    cursor="hand2",
    corner_radius=15,
    fg_color="#8B0000",
    hover_color="#FF3333",
    command=category_choice1_func
    )
    category_choice1.place(x=100,y=350)
    category_choice2 = CTkButton(category_win,
    text="Sports",
    width=200,
    height=60,
    text_color="white",
    font=("consolas",35,"bold"),
    cursor="hand2",
    corner_radius=15,
    fg_color="#8B0000",
    hover_color="#FF3333",
    command=category_choice2_func
    )
    category_choice2.place(x=400,y=350)
    category_choice3 = CTkButton(category_win,
    text="Countries_States",
    width=200,
    height=60,
    text_color="white",
    font=("consolas",35,"bold"),
    cursor="hand2",
    corner_radius=15,
    fg_color="#8B0000",
    hover_color="#FF3333",
    command=category_choice3_func
    )
    category_choice3.place(x=700,y=350)
    category_choice4 = CTkButton(category_win,
    text="Animals",
    width=200,
    height=60,
    text_color="white",
    font=("consolas",35,"bold"),
    cursor="hand2",
    corner_radius=15,
    fg_color="#8B0000",
    hover_color="#FF3333",
    command=category_choice4_func
    )
    category_choice4.place(x=1150,y=350)
    category_choice5 = CTkButton(category_win,
    text="Random",
    width=200,
    height=60,
    text_color="white",
    font=("consolas",35,"bold"),
    cursor="hand2",
    corner_radius=15,
    fg_color="#8B0000",
    hover_color="#FF3333",
    command=category_choice5_func
    )
    category_choice5.place(x=560,y=470)
    
def play():
    select = my_segments.get()
    if select=="":
       messagebox.showerror("Error","Pls First Select The Option")
       return
    if select == "Singleplayer":
        win.withdraw()
        win.after(1000,category())
        return
# starting windows coontinue
logo_my_img = CTkImage(dark_image=Image.open(resource_path("hgman1.png")),size=(900,520))
lbl = CTkLabel(win,image=logo_my_img,text="",bg_color="#0A0A1A")
lbl.place(x=300,y=-100)

my_segments_values = ["Singleplayer","Multiplayer"]
my_segments = CTkSegmentedButton(
    win,
    values=my_segments_values,
    selected_color="#8B0000",
    unselected_color="#1a1a3e",
    text_color="white",
    corner_radius=10,
    selected_hover_color="#FF3333",
    font=("Arial Black",30,"bold"))
my_segments.place(x=530,y=300)
btn = CTkButton(
    win,
    text="Play",
    width=200,
    height=60,
    text_color="white",
    font=("consolas",50,"bold"),
    cursor="hand2",
    corner_radius=15,
    fg_color="#8B0000",
    hover_color="#FF3333",
    command=play)
btn.place(x=650,y=420)
win.mainloop()