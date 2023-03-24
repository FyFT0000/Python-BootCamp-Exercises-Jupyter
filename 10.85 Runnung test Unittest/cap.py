import string

def cap_text(text):
    """
    Input a string
    Output the paitalized string
    """
    #return text.capitalize()
    #return text.title()
    return string.capwords(text)

#print(cap_text("monty python's program"))