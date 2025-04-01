import math # for rounding the output

units = ['milimeters', 'centimeters', 'meters', 'kilometers', 'inches', 'feet', 'yards', 'miles'] # unit list
abbr_units = ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi'] # unit list but abbreviation
print("\033[1;47;40m What unit are you converting from? \n")

for u in range(len(units)):
    print("\033[0;37;40m " + abbr_units[u] + ': ' + units[u]) # prints out a list of units
print()

def conversion(u_val, val, rounding): # converts input into different units
    # converting from Metric Units
    if u_val <= 3: # milimeter conversion
        c_units = [val, val/10, val/1000, val/1000000, val/25.4, val/304.8, val/914.4, val/1609344]

        if u_val == 1 or u_val == 2 or u_val == 3: # centimeter conversion
            c_units = [element * 10 for element in c_units]

            if u_val == 2 or u_val == 3: # meter conversion
                c_units = [element * 100 for element in c_units]

                if u_val == 3:
                    c_units = [element * 1000 for element in c_units] # kilometer conversion

    # converting from imperial units
    if u_val >= 4: # inches conversion
        c_units = [val*25.4, val * 2.54, val*0.0254, val * 0.0000254,  val, val/12, val/36, val/63360]

        if u_val == 5 or u_val == 6 or u_val == 7: # feet conversion
            c_units = [element * 12 for element in c_units]
        
            if u_val == 6 or u_val == 7: # yards conversion
                c_units = [element * 3 for element in c_units]

                if u_val == 7:
                    c_units = [element * 1760 for element in c_units] # miles conversion

    for u in range(len(units)): # outputs a list of converted measurements
        print("\033[0;37;40m " + units[u] + ': ' + str(round(c_units[u], rounding - int(math.floor(math.log10(abs(c_units[u]))))))) # rounds the answer

    print()
    user_input() # asks the question again
    
def user_input(): # asks the input variables
    unit = input('\033[1;37;40m Unit (use abbreviation or name): ')
    if unit in units: # checks if input is in the units list
        while True:
            try:
                val = float(input('\n\033[1;37;40m How many ' + unit + '?: ')) # asks the value
            except ValueError:
                print('\033[1;31;40m Incorrect variable type. Please enter a number.') # if value is not a number
                continue
            else:
                break
        conversion(units.index(unit), float(val), len(str(val)))
    elif unit in abbr_units: # checks if input is in the abbreviated units list
        while True:
            try:
                val = float(input('\n\033[1;37;40m How many ' + units[abbr_units.index(unit)] + '?: ')) # asks the value
            except ValueError:
                print('\033[1;31;40m Incorrect variable type. Please enter a number.') # if value is not a number
                continue
            else:
                break
        conversion(abbr_units.index(unit), float(val), len(str(val)))
    else: # if input is not in unit list
        print("\n\033[1;31;40m Use the unit abbreviation or name.\n")
        user_input()
user_input() # initial startup