'''Password Strength Checker (Moderate)
What to build
Check password length
Check digits, alphabets, symbols
Return strength: Weak / Medium / Strong
Concepts used
String methods
if-else conditions
Set for required characters
Loop to scan password
Function to evaluate strength'''
def pass_check(password):
    length=len(password)
    has_letter=False
    has_digit=False
    has_symbol=False
    for p in password:
        if p.isalpha():
            has_letter=True
        elif p.isdigit():
            has_digit=True
        else:
            has_symbol=True
    if has_letter==True and has_digit==True and has_symbol==True and len(password)>8:
        return "Strong password"
    elif has_letter==True and has_digit==True and len(password)>6:
        return "Moderate password"
    else:
        return "weak password"
print(pass_check("sachinss1@$"))
print(pass_check("sachi1$"))
print(pass_check("sachinss%$1"))