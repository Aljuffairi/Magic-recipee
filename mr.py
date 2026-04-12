import csv      # Lets Python read and write .csv files
import random   # Lets Python make random choices
import datetime  # Lets Python work with today's date

# The name of the file that stores all recipes
CSV_FILE = "recipes.csv"

# The column names used in the CSV file — every recipe has these fields
CSV_COLUMNS = [
    "name",          # Recipe title           e.g.  "Pancakes"
    "ingredients",   # Comma-separated list   e.g.  "flour, egg, milk"
    "prep_time",     # Minutes to prepare     e.g.  "15"
    "instructions",  # How to cook it         e.g.  "Mix and fry..."
    "difficulty",    # Easy, Medium, or Hard
    "category",      # Breakfast, Lunch, Dinner, or Dessert
    "servings",      # Number of servings     e.g.  "4"
    "rating",        # Score from 1 to 5      e.g.  "4"  (can be empty)
    "times_cooked",  # How many times cooked  e.g.  "3"
    "last_cooked",   # Date last cooked       e.g.  "2024-11-15" (can be empty)
]

# The only allowed values for difficulty and category
DIFFICULTY_OPTIONS = ["Easy", "Medium", "Hard"]
CATEGORY_OPTIONS   = ["Breakfast", "Lunch", "Dinner", "Dessert"]

print("Shared setup loaded.")
print("CSV file:", CSV_FILE)


def load_recipes(): 

    """ Open recipes.csv and return a list of dictionary
    If the file does not exist yet, returns an empty list instead of crashing.
    """

    recipes = [] #empty list 

    try: 
        with open(CSV_FILE,'r', newline='') as file:
            reader = csv.DictReader(file) #Convert each row into dict
            for row in reader: 
                recipes.append(dict(row)) #each csv row added to our above list in a dictionary format.

    except FileNotFoundError: #returns empty list if no file found
        pass

    return recipes 


def save_recipes(recipes):

    """Writes the full recipes list to recipes.csv """

    with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=CSV_COLUMNS)
            writer.writeheader() #Column nam first row
            writer.writerows(recipes) #every recipe as a row based on dict keys fieldnames 'CSV Column'
def add_recipe(recipes): 
    """Ask user input for Creating new recipees and appending recipe list"""
    print('--- Add a New Recipe ---')

    name = input('Recipe name: ').strip()
    ingredients = input('ingredients (seperated by comma): ').strip()
    instructions = input('Cooking instructions: ').strip()


    while True: 
        prep_time = input("Prep time (minutes): ").strip()
        if prep_time.isdigit():
            break
        print("Please enter digit only")


    while True:
        print("Dificulty options:", DIFFICULTY_OPTIONS)
        difficulty = input("Difficulty: ").strip().capitalize()
        if difficulty in DIFFICULTY_OPTIONS: 
            break
        print('Please choose Easy, Medium or Hard')


    while True:
        print("Category: ", CATEGORY_OPTIONS)
        category = input("Category: ").strip().capitalize()
        if category in CATEGORY_OPTIONS: 
            break
        print('Please choose Breakfast, Lunch, Dinner, or Dessert.')


    while True:
        servings = input("Number of servings: ").strip()
        if servings.isdigit():
            break
        print("Please enter digit only")

    while True: 
        rating = input("1 to 5 (Enter to skip): ").strip()
        if rating == "" :
            break
        if rating.isdigit() and 1 <= int(rating) <= 5:
            break
        print("Please rnter a number 1 to 5 or ENTER to skip")


    new_recipe = {
    "name":  name,
    "ingredients":  ingredients,
    "prep_time":    prep_time,
    "instructions": instructions,
    "difficulty":   difficulty,
    "category":     category,
    "servings":     servings,
    "rating":       rating,    
    "times_cooked": "0",       
    "last_cooked":  "",        
    }

    recipes.append(new_recipe)  # Add the new recipe to the list
    save_recipes(recipes)      # Write the updated list to the CSV file
    print("'" + name + "' has been added!")

    return recipes


def display_menu():
    """
    Prints menu so the user can see all available options.
    """
    print("\n=== Recipe Manager ===")
    print("1. Add a new recipe")
    print("2. Search for recipes by ingredient")
    print("3. View all recipes")
    print("4. Get a random recipe")
    print("5. Generate a shopping list")
    print("6. Filter by category")
    print("7. Suggest a recipe (cooking history)")
    print("0. Exit")


def main():
    """
    Runs the whole application.
    Loads saved recipes, shows the menu, and calls the right function
    based on what the user chooses. Keeps looping until the user exits.
    """
    print("Welcome to the Recipe Manager!")

    recipes = load_recipes()  # Load any saved recipes from the CSV file
    print("Loaded", len(recipes), "recipe(s).")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            recipes = add_recipe(recipes)           # Ammar's function 

        elif choice == "2":
            search_by_ingredient(recipes)           # Aqeela's function

        elif choice == "3":
            view_all_recipes(recipes)               # Maryam's function

        elif choice == "4":
            random_recipe(recipes)                  # Aqeela's function

        elif choice == "5":
            generate_shopping_list(recipes)         # Maryam's stretch function

        elif choice == "6":
            filter_by_category(recipes)             # Maryam's stretch function

        elif choice == "7":
            suggest_uncooked_recipe(recipes)        # Aqeela's stretch function

        elif choice == "0":
            print("Goodbye! Happy cooking!")
            break  # Stop the loop and end the program

        else:
            print("Invalid choice. Please enter a number from the menu.")
    

def view_all_recipes(recipes): #defining the function

   if not recipes:
        print("No recipes available!") # Checking if the list is empty, if it is it will return that there is no recepis avaialable
        return
       
   print("\n--- All Recipes ---")

   count = 1

   for recipe in recipes:
       
   # to handle missing rating
        if recipe["rating"] == "": #check if there is no rating
            rating_handling = "-" #if there is no rating it will return -
        else:
            rating_handling = recipe["rating"] #otherwise it will return the actual rating 
            
        print(f"\n{count}. {recipe['name']}")
        print(f"   Preperation Time : {recipe['prep_time']} minutes")
        print(f"   Difficulty level : {recipe['difficulty']}")
        print(f"   Rating    : {rating_handling}")

        count = count + 1
       

def filter_by_category(recipes):

    if not recipes: #if the list is empty
        print("No recipes available.") # it will print this message 
        return # message will be returned and the function will stop at here

        
    print("\nAvailable categories:")
    print(CATEGORY_OPTIONS) #displaying the exsisting catogeries to the user 

    category = input("Enter a category: ").lower() #here the user will Enter one the category options displayed to him 
    
    filtered_recipes = [] #an empty list where we sill store the recipes within the sepecific category the user chosed

    for recipe in recipes:

        if recipe["category"].lower() == category: #will check if the recipe category matches the category entered by the user 
            filtered_recipes.append(recipe)  # if it does match the recipe will be added to the empty list created 
        
    if not filtered_recipes: #check if the list is empty which mean no matches results founded for the specific category within recipes
        print("No results found.") 
        return
        
    print(f"\n--- {category} recipes  ---")

    for recipe in filtered_recipes:
        print(f"- {recipe['name']} , preperaion time is  {recipe['prep_time']} minutes")


def generate_shopping_list(recipes):

    if not recipes:
        print("No recipes available.") #if the list is empty it will return no recipes availables
        return

    view_all_recipes(recipes) #displaying all the recips for the user so he can choose

    recipes_selections = input("Enter the recipe numbers to generate a shopping list, separated by commas (e.g., 1, 3, 5)").strip()

    shopping_list = []

    for n in recipes_selections.split(","): #looping through users selection
        n = n.strip()

        if not n.isdigit(): #to check if the user input is a valid numbers , if its not number it will skip it 
            continue 

        index = int(n) - 1 #since user see list starts with 1 , for python index strats with 0

        if 0 <= index < len(recipes):

            recipe = recipes[index]

            ingredients = recipe["ingredients"].split(",")

            for item in ingredients:
                item = item.strip()

                is_duplicate = False 

                for existing in shopping_list:
                    
                    if existing.lower() == item.lower():
                        is_duplicate = True 
                        break  

                
                if not is_duplicate:
                    shopping_list.append(item)

    if not shopping_list:
        print("No ingredients found.")
        return

    
    print("\n--- Shopping List ---")
    for item in shopping_list:
        print(f"☐ {item}")



def search_by_ingredient(recipes):
    search_ingredient = (input("Enter the ingredient to search for: ").lower())
    found = False
    print(f"\nSearch results for: {search_ingredient} ")

    for i in recipes:
        if search_ingredient in i['ingredients'].lower():
            print(f"{i['name']} : (Category: {i['category']})")
            found = True
            
        if not found:
            print("Sorry, there are no recipes found with that ingredient :( .")



def random_recipe(recipes):
    if len(recipes) == 0:
        print("Sorry,there are no recipes available yet.")
        return
        
    r = random.choice(recipes)
    print("\nRandom Suggestion: ")
    print(f"Name of the recipe is: {r['name']}")
    print(f"Ingredients of the recipe is: {r['ingredients']}")
    print(f"Instructions of the recipe is: {r['instructions']}")



def suggest_uncooked_recipe(recipes):
    if len(recipes) == 0:
        print("Your recipe book is empty!")
        return
    
    suggested = recipes[0]
    for i in recipes:
        if int(i['times_cooked']) < int(suggested['times_cooked']):
            suggested = i
            
    print(f"How about cooking '{suggested['name']}'? You haven't made it very often (Cooked {suggested['times_cooked']} times).")



main()