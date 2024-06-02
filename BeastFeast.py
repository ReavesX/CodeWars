# Check if the first char of string a = first char of string b
# Check if the last char of string a = last char of string b
# true: yes and yes
# false: no and (DO NOT CARE)

def feast(beast, dish):
    # your code here
    
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else: return False