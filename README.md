# Magic-recipee


## Recipe Manager

### A Python command-line app that lets you store, search, and manage recipes using a CSV file. Built as a group project.

## Team

AJ — foundation, CSV handling, adding recipes, main menu
MI— viewing recipes, category filter, shopping list
AH — search, random recipe, cooking history


## How to Run
Open the main notebook (RecipeManager.ipynb) and run all cells from top to bottom. The last cell runs main() which starts the app.
Make sure you run the shared setup cell first or nothing will work.

## Features

Add a new recipe
Search for recipes by ingredient
View all recipes
Get a random recipe suggestion
Sort recipes by rating
Generate a shopping list
Filter by category
Suggest a recipe based on cooking history


## Files

RecipeManager.ipynb — main notebook with all the code
recipes.csv — created automatically when you add your first recipe


## How the data is stored
Everything is saved in recipes.csv. Each row is one recipe with these fields:
name, ingredients, prep_time, instructions, difficulty, category, servings, rating, times_cooked, last_cooked
The file is created on the first run and persists between sessions so your recipes are never lost.

Requirements
No external libraries needed. Only built-in Python modules are used:

csv
random
datetime
