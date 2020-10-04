#### for loop with if inside ####

def translate(phrase):
   
    translation = ""

    for letter in phrase:          ### For loop - loop until end of phrase length.
        
        if letter in "AEIOUaeiou":              ### If condition (if loop)
            translation = translation + "g"
        
        else:
            translation = translation + letter      
            ## when there is no g, the translation is current translation + letter

    return translation  




print(translate(input("enter a phrase: ")))
# call function with user's input
