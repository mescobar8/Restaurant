import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk

root  = Tk()

root.title("Pizza restaurant")

# ------------------------------------FUNCTIONS--------------------------------------------- #


# ---------------------------------- STYLING AND IMAGES ------------------------------------ #

#region Style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#2B2B28")
s.configure('MenuFrame.TFrame', background = "#4A4A48")
s.configure('DisplayFrame.TFrame', background = "#0F1110")
s.configure('OrderFrame.TFrame', background = "#B7C4CF")
s.configure('DishFrame.TFrame', background = "#4A4A48", relief = "raised")
s.configure('MenuLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 13, "italic"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 21
            )
s.configure('orderTotalLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )

# Top Banner images
LogoImageObject = Image.open("Images/Logo.png").resize((130, 130))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("Images/TopBanner.jpg").resize((800, 130))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

# Menu images
displayDefaultImageObject = Image.open("Images/display - Default.png").resize((350,360))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

CheesePizzaImageObject = Image.open("Images/menu/cheese pizza.png").resize((350,334))
cheesepizzaiImage = ImageTk.PhotoImage(CheesePizzaImageObject)

PepperoniPizaaImageObject = Image.open("Images/menu/pepperoni pizza.png").resize((350,334))
pepperonipizzaImage = ImageTk.PhotoImage(PepperoniPizaaImageObject)

ChickenPizzaImageObject = Image.open("Images/menu/chicken pizza.png").resize((350,334))
chickenpizzaImage = ImageTk.PhotoImage(ChickenPizzaImageObject)

SupremePizzaImageObject = Image.open("Images/menu/supreme pizza.png").resize((350,334))
supremeImage = ImageTk.PhotoImage(SupremePizzaImageObject)

CheeseSticksImageObject = Image.open("Images/menu/cheese sticks.png").resize((350,334))
cheesesticksImage = ImageTk.PhotoImage(CheeseSticksImageObject)

SodaImageObject = Image.open("Images/menu/Soda.png").resize((350,334))
sodaImage = ImageTk.PhotoImage(SodaImageObject)


#endregion

#----------------------------------- WIDGETS ----------------------------------------------- #


# Section Frames
mainFrame = ttk.Frame(root, width = 800, height = 580, style = 'MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame')
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

# Dish Frames
cheesepizzaFrame = ttk.Frame(menuFrame, style = "DishFrame.TFrame")
cheesepizzaFrame.grid(row = 1, column = 0, sticky = "NSEW")

peperonipizzaFrame = ttk.Frame(menuFrame,style ="DishFrame.TFrame")
peperonipizzaFrame.grid(row = 2, column = 0, sticky ="NSEW")

chickenpizzaFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
chickenpizzaFrame.grid(row = 3, column = 0, sticky ="NSEW")

supremepizzaFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
supremepizzaFrame.grid(row = 4, column = 0, sticky ="NSEW")

cheesesticksFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
cheesesticksFrame.grid(row = 5, column = 0, sticky ="NSEW")

sodaFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
sodaFrame.grid(row = 6, column = 0, sticky ="NSEW")

#endregion

# region Top Banner Section

LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background = "#0F1110")
LogoLabel.grid(row = 0, column = 0, sticky = "W")

RestaurantBannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background = "#0F1110")
RestaurantBannerLabel.grid(row = 0, column = 1, sticky = "NSEW")

# endregion

#region Menu Section
MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

CheesePizzaLabel = ttk.Label(cheesepizzaFrame, text ="Cheese Pizza ..... 10$", style ="MenuLabel.TLabel")
CheesePizzaLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

PeperonniPizzaLabel = ttk.Label(peperonipizzaFrame, text ="Pepperoni Pizza ..... 12$", style ="MenuLabel.TLabel")
PeperonniPizzaLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

ChickenPizzaLabel = ttk.Label(chickenpizzaFrame, text ="chicken Pizza ..... 15$", style ="MenuLabel.TLabel")
ChickenPizzaLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

SupremePizzaLabel = ttk.Label(supremepizzaFrame, text ="Supreme Pizza ..... 18$", style ="MenuLabel.TLabel")
SupremePizzaLabel.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

CheeseSticksLabel = ttk.Label(cheesesticksFrame, text ="Cheese Sticks ..... 8$", style ="MenuLabel.TLabel")
CheeseSticksLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

SodaLabel = ttk.Label(sodaFrame, text ="Soda .... 3$", style ="MenuLabel.TLabel")
SodaLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

#Buttons
CheesePizzaButton = ttk.Button(cheesepizzaFrame, text ="Display")
CheesePizzaButton.grid(row = 0, column = 1, padx = 10)

PepperoniPizzaButton = ttk.Button(peperonipizzaFrame, text ="Display")
PepperoniPizzaButton.grid(row = 0, column = 1, padx = 10)

ChickenPizzaButton = ttk.Button(chickenpizzaFrame, text ="Display")
ChickenPizzaButton.grid(row = 0, column = 1, padx = 10)

SupremePizzaButton = ttk.Button(supremepizzaFrame, text ="Display")
SupremePizzaButton.grid(row = 0, column = 1, padx = 10)

CheeseSticksButton = ttk.Button(cheesesticksFrame, text ="Display")
CheeseSticksButton.grid(row = 0, column = 1, padx = 10)

SodaButton = ttk.Button(sodaFrame, text ="Display")
SodaButton.grid(row = 0, column = 1, padx = 10)

# endregion

#region Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : ")
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER")
orderButton.grid(row = 4, column = 0, sticky = "EW")


# endregion
# region Display Section
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER")
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE")
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

#endregion



#----------------------------- GRID CONFIGURATIONS -------------------------------------------#
mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)
orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)



root.mainloop()
