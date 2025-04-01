import math
import tkinter

root = tkinter.Tk()
root.title("Unit Conversion Tool 2.0")
root.geometry("600x400")

units = ['milimeters', 'centimeters', 'meters', 'kilometers', 'inches', 'feet', 'yards', 'miles']

currentUnit = tkinter.StringVar()
currentUnit.set(units[1])

dropdownCurrent = tkinter.OptionMenu(root, currentUnit, *units)
dropdownCurrent.pack()

inputValue = tkinter.Text(root, height = 1, width = 10)
inputValue.pack()

outputUnit = tkinter.StringVar()
outputUnit.set(units[4])

def button_clicked():
    val = float(inputValue.get("1.0", "end-1c"))
    print (val)
    inUnit = currentUnit.get()
    print (inUnit)
    outUnit = outputUnit.get()
    print (outUnit)
    if inUnit == 'milimeters' or inUnit == 'centimeters' or inUnit == 'meters' or inUnit == 'kilometers': # milimeter conversion
        cVal = [val, val/10, val/1000, val/1000000, val/25.4, val/304.8, val/914.4, val/1609344]

        if inUnit == 'centimeters' or inUnit == 'meters' or inUnit == 'kilometers': # centimeter conversion
            cVal = [element * 10 for element in cVal]

            if inUnit == 'meters' or inUnit == 'kilometers': # meter conversion
                cVal = [element * 100 for element in cVal]

                if inUnit == 'kilometers':
                    cVal = [element * 1000 for element in cVal] # kilometer conversion

    # converting from imperial units
    if inUnit == 'inches' or inUnit ==  'feet' or inUnit ==  'yards' or inUnit ==  'miles':
        cVal = [val*25.4, val * 2.54, val*0.0254, val * 0.0000254,  val, val/12, val/36, val/63360]

        if inUnit ==  'feet' or inUnit ==  'yards' or inUnit ==  'miles': # feet conversion
            cVal = [element * 12 for element in cVal]
        
            if inUnit ==  'yards' or inUnit ==  'miles': # yards conversion
                cVal = [element * 3 for element in cVal]

                if inUnit ==  'miles':
                    cVal = [element * 1760 for element in cVal]
    rounding = len(str(val))
    output.delete("1.0", tkinter.END)
    for u in range(len(units)): # outputs a list of converted measurements
        output.insert(tkinter.END,units[u] + ": " + str(round(cVal[u], rounding - int(math.floor(math.log10(abs(cVal[u]))))))+"\n")

button = tkinter.Button(root, text="Convert", command=button_clicked)
button.pack()

output = tkinter.Text(root, height = 8, width = 40)
output.pack()

root.mainloop()