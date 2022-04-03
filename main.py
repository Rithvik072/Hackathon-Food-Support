import time
import math
from tkinter import *
from tkinter import messagebox
from database import food
import json

COLOR = "#f9d3a3"
BLACK = "#000000"
window = Tk()
window.title("Food Support")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg=COLOR)

for food_item in range(len(food)):
    food_name = food[food_item]["Name"]
    calories = food[food_item]["Calor"]
    serving_size = food[food_item]["SS"]
    fat = food[food_item]["Total"]
    cholestrol = food[food_item]["Chol"]
    sodium = food[food_item]["Sod"]
    carbohydrates = food[food_item]["Carb"]
    fiber = food[food_item]["Fiber"]
    sugar = food[food_item]["Sugar"]
    protein = food[food_item]["Protein"]
    iron = food[food_item]["Iron"]
    potassium = food[food_item]["Pot"]
    calcium = food[food_item]["Calc"]


###################FUNCTIONS###########################
def about_page():
    window.destroy()
    ab = Tk()
    ab.title("About Us")
    ab.minsize(width=500, height=500)
    ab.config(padx=90, pady=50, bg=COLOR)

    ab_label = Label(text="About Us", font=("Times New Roman", 38, "italic"), fg=BLACK, bg=COLOR)
    ab_label.place(x=0, y=0)

    t_label = Label(text='''
        Welcome to our page! 
This is a program 
that allows users to monitor
their daily calorie intake 
and see the nutrition 
facts of the food you
may choose to eat in a day!  ''',
                    font=("Times New Roman", 20, "bold"), fg=BLACK, bg=COLOR)
    t_label.place(x=0, y=60)


# m_label=Label(text=''' Today we are in a society where
#     watching your calorie intake and
#     types of foods you eat is difficult
#     to do, it's crucial to maintain a
#     proper diet as well as excerise to
#     stay healthy. We hope this is helpful
#     with monitering your diet. ''',
#     font=("Times New Roman", 10, "bold"), fg=BLACK, bg=COLOR)
# m_label.place(x=0, y=200)

def help_page():
    window.destroy()
    help = Tk()
    help.title("Help")
    help.minsize(width=500, height=500)
    help.config(padx=90, pady=50, bg=COLOR)

    help_label = Label(text="Help", font=("Times New Roman", 38), fg=BLACK, bg=COLOR)
    help_label.place(x=0, y=0)
    c_label = Label(text='''
  Welcome to the help page! To navigate through this application you first need to login with a username and password. And then choose between breakfast, lunch and dinner, snacks, or drinks. Then you choose the food and you'll get the nutrition facts about the chosen food.''',
                    font=("Times New Roman", 10, "bold"), fg=BLACK, bg=COLOR)
    c_label.place(x=0, y=60)


###########

def login_page():
    window.destroy()
    login_window = Tk()
    login_window.title("Login Page")
    login_window.minsize(width=500, height=500)
    login_window.config(padx=50, pady=50, bg=COLOR)

    login_label = Label(text="Login", font=("Times New Roman", 45), fg=BLACK, bg=COLOR)
    login_label.place(x=150, y=0)

    username_label = Label(text="Username", font=("Times New Roman", 18, "bold"), fg=BLACK, bg=COLOR)
    username_label.place(x=75, y=100)

    username_entry = Entry(width=30, bg=COLOR, fg=BLACK)
    username_entry.place(x=75, y=130)
    username_entry.insert(0, "name123@gmail.com")

    password_label = Label(text="Password", font=("Times New Roman", 18, "bold"), fg=BLACK, bg=COLOR)
    password_label.place(x=75, y=180)

    password_entry = Entry(width=30, bg=COLOR, fg=BLACK)
    password_entry.place(x=75, y=210)
    password_entry.insert(0, "123456789")

    def nutrition():
        login_window.destroy()
        nutrition_window = Tk()
        nutrition_window.title("Nutrition")
        nutrition_window.minsize(width=500, height=500)
        nutrition_window.config(padx=50, pady=50, bg=COLOR)

        ################CATEGORIES##########################
        def breakfast_page():
            nutrition_window.destroy()
            breakfast = Tk()
            breakfast.title("Breakfast")
            breakfast.minsize(width=500, height=500)
            breakfast.config(padx=50, pady=50, bg=COLOR)

            breakfast_label = Label(text="Breakfast", font=("Times New Roman", 50), fg=BLACK, bg=COLOR)
            breakfast_label.place(x=0, y=0)

            options_label = Label(text="Options", font=("Times New Roman", 40, "underline"), bg=COLOR)
            options_label.place(x=0, y=75)

            foods = Label(text='''
                        Cereal
                        Pancakes
                        Bagels
                        Eggs
                        French Toast
                        Toast
                        Waffles
                        Plain Oatmeal
                        Yogurt
                        Bacon
                        ''', font=("Times New Roman", 20), bg=COLOR)
            foods.place(x=-50, y=180)

            breakfast_insert = Entry(width=20, bg=COLOR, fg=BLACK)
            breakfast_insert.place(x=180, y=160)
            breakfast_item = breakfast_insert.get()

            def submit():
                if len(breakfast_item) == 0:
                    messagebox.showinfo(title="No food?!", message="Please don't leave any fields empty!")
                elif (breakfast_item == food_name):
                    breakfast_things = Label(text=f'''
                                          name = {food_name}
  calories = {calories}
  serving size = {serving_size}
  fat = {fat}
  cholestrol = {cholestrol}
  sodium = {sodium}
  carbohydrates = {carbohydrates}
  fiber ={fiber}
  sugar = {sugar}
  protein = {protein}
  iron = {iron}
  potassium = {potassium}
  calcium = {calcium}
                                         ''', font=("Times New Roman", 10), fg=COLOR)
                    breakfast_things.place(x=200, y=100)
                else:
                    messagebox.showinfo(title="Food not found",
                                        message="Please enter a valid food (with proper capitalization and spacing)")

            submit_button = Button(text="Submit", font=("Times New Roman", 10), fg=BLACK, height=4, command=submit)
            submit_button.place(x=0, y=150)

        def lunch_dinner_page():
            nutrition_window.destroy()
            lunch = Tk()
            lunch.title("Lunch & Dinner page")
            lunch.minsize(width=500, height=500)
            lunch.config(padx=0, pady=50, bg=COLOR)

            dinner_label = Label(text="Lunch & Dinner", font=("Times New Roman", 50), fg=BLACK, bg=COLOR)
            dinner_label.place(x=0, y=0)

            options2_label = Label(text="Options", font=("Times New Roman", 30, "underline"), bg=COLOR)
            options2_label.place(x=0, y=75)

            foods2 = Label(text='''
          Ham sandwich
          Veggie salad 
          Chicken salad
          Hamburger
          Beef burrito
          Cheese pizza
          Peanut butter and jelly sandwich  
          Grilled Cheese Sandwich
          Hot Dog
          Burrito 
          Sushi
          Beef Taco
          Garlic Bread 
                        ''', font=("Times New Roman", 15), bg=COLOR)
            foods2.place(x=0, y=150)
            foods2_part2 = Label(text='''
          Tomato soup
          Veggie fried rice
          White rice
          Whole Grain Rice
          Pesto Pasta
          Baked Salmon
          Pork Burrito Bowl
          Veg Burrito Bowl
          Minestrone Soup
          Black Bean Soup
          Butter Noodles
          Chicken Alfredo Pasta
          Mac n’ cheese
                        ''', font=("Times New Roman", 15), bg=COLOR)
            foods2_part2.place(x=250, y=150)
            dinner_insert = Entry(width=20, bg=COLOR, fg=BLACK)
            dinner_insert.place(x=0, y=120)
            dinner_item = snack_insert.get()

            def submit():
                if len(dinner_item) == 0:
                    messagebox.showinfo(title="No food?!", message="Please don't leave any fields empty!")
                elif (dinner_item == food_name):
                    dinner_things = Label(text=f'''
                                              name = {food_name}
      calories = {calories}
      serving size = {serving_size}
      fat = {fat}
      cholestrol = {cholestrol}
      sodium = {sodium}
      carbohydrates = {carbohydrates}
      fiber ={fiber}
      sugar = {sugar}
      protein = {protein}
      iron = {iron}
      potassium = {potassium}
      calcium = {calcium}
                                             ''', font=("Times New Roman", 10), fg=COLOR)
                    dinner_things.place(x=200, y=100)
                else:
                    messagebox.showinfo(title="Food not found",
                                        message="Please enter a valid food (with proper capitalization and spacing)")

            submit_button2 = Button(text="Submit", font=("Times New Roman", 10), fg=BLACK, command=submit)
            submit_button2.place(x=60, y=180)

        def snack_page():
            nutrition_window.destroy()
            snack_page = Tk()
            snack_page.title("Snacks")
            snack_page.minsize(width=500, height=500)
            snack_page.config(padx=50, pady=50, bg=COLOR)

            snack_label = Label(text="Snacks", font=("Times New Roman", 50), fg=BLACK, bg=COLOR)
            snack_label.place(x=0, y=0)

            options3_label = Label(text="Options", font=("Times New Roman", 30, "underline"), bg=COLOR)
            options3_label.place(x=0, y=75)

            foods3 = Label(text='''
          Potato Chips
          French Fries
          Cheez its 
          Goldfish 
          Oreos
          Tortilla Chips
          Strawberries
          Blueberries 
          Grapes
          Vanilla Ice cream
          Chocolate Ice cream
                            ''', font=("Times New Roman", 20), bg=COLOR)
            foods3.place(x=0, y=130)

            snack_insert = Entry(width=20, bg=COLOR, fg=BLACK)
            snack_insert.place(x=150, y=130)
            snack_item = snack_insert.get()

            def submit():
                if len(dinner_item) == 0:
                    messagebox.showinfo(title="No food?!", message="Please don't leave any fields empty!")
                elif (snack_item == food_name):
                    snack_things = Label(text=f'''
                                              name = {food_name}
      calories = {calories}
      serving size = {serving_size}
      fat = {fat}
      cholestrol = {cholestrol}
      sodium = {sodium}
      carbohydrates = {carbohydrates}
      fiber ={fiber}
      sugar = {sugar}
      protein = {protein}
      iron = {iron}
      potassium = {potassium}
      calcium = {calcium}
                                             ''', font=("Times New Roman", 10), fg=COLOR)
                    snack_things.place(x=200, y=100)
                else:
                    messagebox.showinfo(title="Food not found",
                                        message="Please enter a valid food (with proper capitalization and spacing)")

            submit_button3 = Button(text="Submit", font=("Times New Roman", 10), fg=BLACK, height=3, command=submit)
            submit_button3.place(x=0, y=120)

        def drink_page():
            nutrition_window.destroy()
            drink_page = Tk()
            drink_page.title("Drinks")
            drink_page.minsize(width=500, height=500)
            drink_page.config(padx=50, pady=50, bg=COLOR)

            drink_label = Label(text="Drinks", font=("Times New Roman", 50), fg=BLACK, bg=COLOR)
            drink_label.place(x=0, y=0)

            options4_label = Label(text="Options", font=("Times New Roman", 30, "underline"), bg=COLOR)
            options4_label.place(x=0, y=75)

            foods4 = Label(text='''
            Lemonade 
            Cranberry juice
            Apple juice
            Orange juice
                              ''', font=("Times New Roman", 15), bg=COLOR)
            foods4.place(x=0, y=180)

            drinks_insert = Entry(width=20, bg=COLOR, fg=BLACK)
            drinks_insert.place(x=100, y=140)
            drinks_item = drinks_insert.get()

            def submit():
                if len(drinks_item) == 0:
                    messagebox.showinfo(title="No food?!", message="Please don't leave any fields empty!")
                elif (drinks_item == food_name):
                    drinks_things = Label(text=f'''
                                                    name = {food_name}
            calories = {calories}
            serving size = {serving_size}
            fat = {fat}
            cholestrol = {cholestrol}
            sodium = {sodium}
            carbohydrates = {carbohydrates}
            fiber ={fiber}
            sugar = {sugar}
            protein = {protein}
            iron = {iron}
            potassium = {potassium}
            calcium = {calcium}
                                                   ''', font=("Times New Roman", 10), fg=COLOR)
                    drinks_things.place(x=200, y=100)
                else:
                    messagebox.showinfo(title="Food not found",
                                        message="Please enter a valid food (with proper capitalization and spacing)")

            submit_button4 = Button(text="Submit", font=("Times New Roman", 10), fg=BLACK, height=4, command=submit)
            submit_button4.place(x=0, y=120)

        lunch_dinner_button = Button(text='''Lunch
  &
  Dinner''', font=("Times New Roman", 10, "bold"), width=5, height=10, command=lunch_dinner_page)
        lunch_dinner_button.place(x=110, y=100)

        breakfast_button = Button(text="Breakfast", font=("Times New Roman", 10, "bold"), width=5, height=10,
                                  command=breakfast_page)
        breakfast_button.place(x=5, y=100)

        snack_button = Button(text="Snack", font=("Times New Roman", 10, "bold"), width=5, height=10, command=snack_page)
        snack_button.place(x=215, y=100)

        drink_button = Button(text="Drinks", font=("Times New Roman", 10, "bold"), width=5, height=10, command=drink_page)
        drink_button.place(x=320, y=100)

        category = Label(text="Select Category", font=("Times New Roman", 50, "bold", "underline"), bg=COLOR)
        category.place(x=0, y=0)

    login_button = Button(text="Login", font=("Times New Roman", 10, "bold"), command=nutrition, height=2)
    login_button.place(x=175, y=270)


my_label = Label(text="Food Support", font=("Times New Roman", 50, "bold"), fg=BLACK, bg=COLOR)
my_label.place(x=-45, y=20)

frame = Frame(highlightbackground="black", highlightthickness=2)

###########

login = Button(text="Login", font=("Times New Roman", 15), fg=BLACK, width=10, height=3, highlightthickness=0,
               command=login_page)
login.place(x=150, y=150)

about_us = Button(text="About Us", font=("Times New Roman", 15), width=10, height=3, fg=BLACK, highlightthickness=0,
                  command=about_page)
about_us.place(x=150, y=250)

window.mainloop()
