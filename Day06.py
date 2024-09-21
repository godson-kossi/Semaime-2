def f(x):
    return 2 * x + 1

def g():
    return 7

y = f(2)
print(y)

y = f(5) + g()
print(y)



# def f ( x ) : # defines a function f that takes one argument x and returns 2 * x + 1.
# return 2 * x + 1
# def g () : # efines a function g that takes no arguments and returns the constant 7. Calling the Functions:
# return 7
# y = f (2) # calls function f with x = 2. This calculates 2 * 2 + 1, which is 5, and assigns this value to y.
# #print(y) prints the value of y, which is 5.
# print( y )
# y = f (5) + g () # calls function f with x = 5, calculates 2 * 5 + 1, which is 11, and adds the result of calling g(), which is 7. So, y becomes 11 + 7, which is 18.
# # print(y) prints the new value of y, which is 18
# print( y )


# Task 1.2

def bread():   # bread() function who can be colling at the top and bottom to represent the bread slices.
    print(" <////////// > ")

def lettuce(): # lettuce() and tomato() functions, can be called to add layers of lettuce and tomato.
    print(" ~~~~~~~~~~~~ ")

def tomato():
    print(" O O O O O O ")

def ham(): #   ham() function can be call to twice for the double ham.
    print(" ============ ")

# Display the sandwich in the terminal
bread()
lettuce()
tomato()
ham()
ham()  # Double ham 
bread()



# Task 1.3

def bread():   # bread() function who can be colling at the top and bottom to represent the bread slices.
    print(" <////////// > ")

def lettuce(): # lettuce() and tomato() functions, can be called to add layers of lettuce and tomato.
    print(" ~~~~~~~~~~~~ ")

def tomato():
    print(" O O O O O O ")

def ham(): #   ham() function can be call to twice for the double ham.
    print(" ============ ")

# Display the sandwich in the terminal

for _ in range(42): # Make 42 of those lettuce-tomato-double ham sandwiches.
      bread()
      lettuce()
      tomato()
      ham()
      ham()  # Double ham 
      bread()
      print()
    
   
   # Task 1.4

def bread():
    print(" <////////// > ")

def lettuce():
    print(" ~~~~~~~~~~~~ ")

def tomato():
    print(" O O O O O O ")

def ham():
    print(" ============ ")

def make_sandwiches(count): # make_sandwiches(count) function takes count as a parameter, which represents the number of sandwiches to be prepared.
    if count <= 0 :
        print(" I can't do this. Please enter a positive integer.")
    else:
        for _ in range(count):  # count times, displaying one sandwich per loop iteration.
              bread()
              lettuce()
              tomato()
              ham()
              ham()  # Double ham
              bread()
              print()  # Blank line between sandwiches

# Example: Make 5 sandwiches
count = int(input("How many sandwiches you like to prepare?"))
make_sandwiches(count)


# Task 1.5

def bread():
    print(" <////////// > ")

def lettuce():
    print(" ~~~~~~~~~~~~ ")

def tomato():
    print(" O O O O O O ")

def ham():
    print(" ============ ")


def make_sandwiches(count, vegetarian=False):
    if count <= 0:
        print("I can't do this. Please enter a positive integer")
    else:
        for _ in range(count):
            bread()
            lettuce()
            tomato()
            if vegetarian:
                lettuce()  # Double lettuce for vegetarian
                tomato()  # Double tomato for vegetarian
            else:
                ham()  # Double ham for non-vegetarian
                ham()
            bread()
            print()  # Blank line between sandwiches


# Example: Make 5 sandwiches
count = int(input("How many sandwiches you like to prepare?"))
is_vegetarian = input("Do you want a vegetarian sandwich? (yes/no): ").strip().lower() == 'yes' #if vegetarian is True, the sandwich will have double layers of lettuce and tomato instead of ham.
make_sandwiches(count,vegetarian=is_vegetarian)

                    
# Task  Challenge

import time

# Function to compute x^n using simple exponentiation by squaring
def fast_power(x, n):
    result = 1
    while n > 0:
        if n % 2 == 1:  # If n is odd
            result *= x
        x *= x  # Square the base
        n //= 2  # Divide the exponent by 2
    return result

# Compute 42^84
start_time = time.time()
result = fast_power(42, 84)
end_time = time.time()
print(f"42^84 = {result}")
print(f"Time to compute 42^84: {end_time - start_time} seconds")

# Compute 42^168
start_time = time.time()
result = fast_power(42, 168)
end_time = time.time()
print(f"42^168 = {result}")
print(f"Time to compute 42^168: {end_time - start_time} seconds")


# Challenge 2

import time

# Function to compute x^n using simple exponentiation by squaring
def fast_power(x, n):
    result = 1
    while n > 0:
        if n % 2 == 1:  # If n is odd
            result *= x
        x *= x  # Square the base
        n //= 2  # Divide the exponent by 2
    return result

# Get user input for the base and the exponent
try:
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))

    # Measure time and compute result
    start_time = time.time()
    result = fast_power(base, exponent)
    end_time = time.time()

    print(f"{base}^{exponent} = {result}")
    print(f"Time to compute {base}^{exponent}: {end_time - start_time} seconds")

except ValueError:
    print("Invalid input. Please enter integers for the base and exponent.")



# Task 3.1


import string

def is_palindrome(s):
    # Normalize the string by removing punctuation and spaces, and converting to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Base case: if the string is empty or a single character, it's a palindrome
    if len(s) <= 1:
        return True
    
    # Recursive case: compare the first and last characters
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Example usage
print(is_palindrome("kayak"))  
print(is_palindrome("never odd or even"))  
print(is_palindrome("Was it a car or a cat I saw?")) 
print(is_palindrome("hello"))  


# Task 2.1'

import string

def is_palindrome(s):
    # Normalize the string by removing punctuation and spaces, and converting to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Base case: if the string is empty or a single character, it's a palindrome
    if len(s) <= 1:
        return True
    
    # Recursive case: compare the first and last characters
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

def main():
    user = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(user):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

# Run the main function to get user input and check for palindrome
if __name__ == "__main__":
    main()


# Task 2.2
import os

def list_files_and_directories(start_dir='.'):
    for root, dirs, files in os.walk(start_dir):              # os.walk generates the file names in a directory tree.
        print(f"In directory: {root}")                        # Print all files
        for dir_name in dirs:                                # Print all subdirectories
            print(f"Dir: {dir_name}")
        for file_name in files:                              # Print all files
            print(f"File: {file_name}")
        print("-" * 40)

list_files_and_directories()                                # the function with the current directory as starting point


# task 3.1

import string

# Function A: checks if the string contains at least n lowercase letters
def funA(s, n):
    lowercase_count = sum(1 for char in s if char.islower())
    return lowercase_count >= n

# Function B: checks if the string contains at least n uppercase letters
def funB(s, n):
    uppercase_count = sum(1 for char in s if char.isupper())
    return uppercase_count >= n

# Function C: checks if the string contains at least n characters
def funC(s, n):
    return len(s) >= n

# Function D: checks if the string contains at least n special characters
def funD(s, n):
    special_characters = string.punctuation
    special_count = sum(1 for char in s if char in special_characters)
    return special_count >= n

# Function E: checks if the string contains at least n numbers
def funE(s, n):
    number_count = sum(1 for char in s if char.isdigit())
    return number_count >= n


# Task 3.2


# Reused functions from the previous task
def funA(s, n):
    return sum(1 for char in s if char.islower()) >= n

def funB(s, n):
    return sum(1 for char in s if char.isupper()) >= n

def funC(s, n):
    return len(s) >= n

def funD(s, n):
    import string
    return sum(1 for char in s if char in string.punctuation) >= n

def funE(s, n):
    return sum(1 for char in s if char.isdigit()) >= n

# Generic password check function
def check_password(validation_func, n, password):
    return validation_func(password, n)

# Example usage
password = "mySecretPassword!123"

# Check if the password has at least 4 lowercase letters
print(check_password(funA, 4, password))  # True

# Check if the password has at least 2 special characters
print(check_password(funD, 2, password))  # False


# Task 3.3


# Error Management System
def check_password(validation_func, n, password):
    # Ensure the provided validation function is callable
    if not callable(validation_func):
        raise TypeError("The first argument must be a valid function.")
    
    # Ensure n is a positive integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("The second argument must be a non-negative integer.")
    
    # Ensure the password is a string
    if not isinstance(password, str):
        raise TypeError("The third argument must be a string.")
    
    # Call the validation function with parameters and return the result
    return validation_func(password, n)

# Reused validation functions from before
def funA(s, n):
    return sum(1 for char in s if char.islower()) >= n

def funB(s, n):
    return sum(1 for char in s if char.isupper()) >= n

def funC(s, n):
    return len(s) >= n

def funD(s, n):
    import string
    return sum(1 for char in s if char in string.punctuation) >= n

def funE(s, n):
    return sum(1 for char in s if char.isdigit()) >= n

# Example usage with error handling
try:
    password = "mySecretPassword!123"
    
    # Validating the password for lowercase letters and special characters
    print(check_password(funA, 4, password))  # True, 4 lowercase letters
    print(check_password(funD, 2, password))  # False, only 1 special character

except (TypeError, ValueError) as e:
    print(f"Error: {e}")


# Task 3.3 explain




# #  Fonction améliorée `check_password` avec gestion des erreurs

# # Objectif du code :
# # Ce code vérifie si un mot de passe satisfait certaines conditions, telles que :
# # - La présence d'un nombre minimum de lettres minuscules.
# # - La présence de caractères spéciaux, etc.
# # En plus, il intègre un 'système de gestion des erreurs' pour s'assurer que les arguments passés à la fonction sont corrects.

# # Explication détaillée :

# # 1. **Fonction `check_password`** :
# def check_password(validation_func, n, password):
#     if not callable(validation_func):
#         raise TypeError("The first argument must be a valid function.")
    
#     if not isinstance(n, int) or n < 0:
#         raise ValueError("The second argument must be a non-negative integer.")
    
#     if not isinstance(password, str):
#         raise TypeError("The third argument must be a string.")
    
#     return validation_func(password, n)


# # - **Paramètres** :
# validation_func :# Il s'agit de la fonction de validation qu'on va  passer, comme par exemple la fonction qui vérifie si le mot de passe contient des lettres minuscules (`funA`).
# #   - `n` : Le nombre minimum d'éléments requis (comme le nombre minimum de lettres minuscules, de chiffres, etc.).
# #   - `password` : Le mot de passe à valider.

# # - **Gestion des erreurs** :
# #   - Le programme vérifie d'abord si la fonction de validation passée est 'appelable' (grâce à `callable(validation_func)`). Si ce n'est pas le cas, il lève une exception de type `TypeError`.
# #   - Ensuite, il vérifie si `n` est bien un entier positif (grâce à `isinstance(n, int)` et `n >= 0`). Si ce n'est pas le cas, il lève une exception de type `ValueError`.
# #   - Enfin, il s'assure que le mot de passe est une chaîne de caractères (grâce à `isinstance(password, str)`). Si ce n'est pas une chaîne, une autre exception `TypeError` est levée.

# # - **Retour** :
# #   Si tous les paramètres sont valides, la fonction appelle la fonction de validation passée en premier argument et retourne `True` ou `False` selon si la condition est respectée.

# #  2. **Fonctions de validation (exemples)** :
# # Ces fonctions servent à valider différentes conditions pour le mot de passe.

# # - **funA** : Vérifie s'il y a au moins `n` lettres minuscules.

#  def funA(s, n):
#      return sum(1 for char in s if char.islower()) >= n


# # - **funB** : Vérifie s'il y a au moins `n` lettres majuscules.

#  def funB(s, n):
#      return sum(1 for char in s if char.isupper()) >= n


# # - **funC** : Vérifie si la longueur de la chaîne est d'au moins `n` caractères.

#  def funC(s, n):
#      return len(s) >= n


# # - **funD** : Vérifie s'il y a au moins `n` caractères spéciaux.
#  def funD(s, n):
#     import string
#      return sum(1 for char in s if char in string.punctuation) >= n


# # - **funE** : Vérifie s'il y a au moins `n` chiffres.
#  def funE(s, n):
#    return sum(1 for char in s if char.isdigit()) >= n

# # 3. **Exemple d'utilisation** :
# try:
#   password = "mySecretPassword!123"
    
# #     # Vérifie si le mot de passe contient au moins 4 lettres minuscules
#  print(check_password(funA, 4, password))  # True (le mot de passe contient 4 lettres minuscules)

#  # Vérifie si le mot de passe contient au moins 2 caractères spéciaux
#   print(check_password(funD, 2, password))  # False (le mot de passe ne contient qu'un seul caractère spécial)

# except (TypeError, ValueError) as e:
#     print(f"Erreur : {e}")


# # - **Explication** :
# #   - Ici, on essaye d'abord de vérifier si le mot de passe contient au moins 4 lettres minuscules en appelant `check_password(funA, 4, password)`. La fonction retourne `True` car le mot de passe a bien 4 lettres minuscules.
# #   - Ensuite, on vérifie s'il y a au moins 2 caractères spéciaux avec `check_password(funD, 2, password)`. La fonction retourne `False` car il n'y a qu'un seul caractère spécial (`!`).
# #   - Si une erreur est détectée (par exemple si un des paramètres est invalide), l'exception sera capturée par le `try-except` et un message d'erreur sera affiché.

# #  Gestion des erreurs :
# # - Si vous essayez de passer une fonction invalide, un nombre négatif pour `n`, ou un mot de passe qui n'est pas une chaîne de caractères, une **erreur sera levée** et gérée proprement avec un message explicatif.

# #  Conclusion :
# # Ce code rend la vérification des mots de passe plus robuste, car il valide non seulement les règles de sécurité du mot de passe, mais il s'assure aussi que les entrées fournies à la fonction sont correctes. Cela évite les plantages inattendus du programme en cas d'entrée incorrecte.

# # ---

# # N'hésite pas à me dire si quelque chose n'est pas clair ou si tu as d'autres questions !



# Task 3.3'

# Error Management System
def check_password(validation_func, n, password):
    if not callable(validation_func):
        raise TypeError("The first argument must be a valid function.")
    
    if not isinstance(n, int) or n < 0:
        raise ValueError("The second argument must be a non-negative integer.")
    
    if not isinstance(password, str):
        raise TypeError("The third argument must be a string.")
    
    return validation_func(password, n)

# Reused validation functions
def funA(s, n):
    return sum(1 for char in s if char.islower()) >= n

def funB(s, n):
    return sum(1 for char in s if char.isupper()) >= n

def funC(s, n):
    return len(s) >= n

def funD(s, n):
    import string
    return sum(1 for char in s if char in string.punctuation) >= n

def funE(s, n):
    return sum(1 for char in s if char.isdigit()) >= n

# Demander à l'utilisateur d'entrer son mot de passe
password = input("Veuillez entrer votre mot de passe : ")

# Exemple d'utilisation : Validation du mot de passe en utilisant les fonctions de validation
try:
    # Vérifier si le mot de passe contient au moins 4 lettres minuscules
    if check_password(funA, 4, password):
        print("Le mot de passe contient au moins 4 lettres minuscules.")
    else:
        print("Le mot de passe ne contient pas suffisamment de lettres minuscules.")
    
    # Vérifier si le mot de passe contient au moins 2 lettres majuscules
    if check_password(funB, 2, password):
        print("Le mot de passe contient au moins 2 lettres majuscules.")
    else:
        print("Le mot de passe ne contient pas suffisamment de lettres majuscules.")
    
    # Vérifier si le mot de passe contient au moins 1 caractère spécial
    if check_password(funD, 1, password):
        print("Le mot de passe contient au moins 1 caractère spécial.")
    else:
        print("Le mot de passe ne contient pas suffisamment de caractères spéciaux.")
    
    # Vérifier si le mot de passe contient au moins 3 chiffres
    if check_password(funE, 3, password):
        print("Le mot de passe contient au moins 3 chiffres.")
    else:
        print("Le mot de passe ne contient pas suffisamment de chiffres.")
    
except (TypeError, ValueError) as e:
    print(f"Erreur : {e}")
