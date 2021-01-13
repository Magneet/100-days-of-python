def format_name(f_name, l_name):
    f_name_title = f_name.title()
    l_name_title = l_name.title()
    return(f_name_title,l_name_title)

f_name = input("First name?")
l_name = input("Last name?")
result = format_name(f_name, l_name)
print(f"Your first name is {result[0]} and your last name is {result[1]}")

def function():
    """bla bla docuentation
    also multiple lines"""

function()