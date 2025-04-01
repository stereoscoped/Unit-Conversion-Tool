import math
import tkinter

root = tkinter.Tk(className="Unit Conversion Tool 2.0")
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

dropdownOutput = tkinter.OptionMenu(root, outputUnit, *units)
dropdownOutput.pack()

def button_clicked():
    val = float(inputValue.get("1.0", "end-1c"))
    print (val)
    inUnit = currentUnit.get()
    print (inUnit)
    outUnit = outputUnit.get()
    print (outUnit)
    if outUnit == 'milimeters' or outUnit == 'centimeters' or outUnit == 'meters' or outUnit == 'kilometers': # milimeter conversion
        cVal = [val, val/10, val/1000, val/1000000, val/25.4, val/304.8, val/914.4, val/1609344]

        if outUnit == 'centimeters' or outUnit == 'meters' or outUnit == 'kilometers': # centimeter conversion
            cVal = [element * 10 for element in cVal]

            if outUnit == 'meters' or outUnit == 'kilometers': # meter conversion
                cVal = [element * 100 for element in cVal]

                if outUnit == 'kilometers':
                    cVal = [element * 1000 for element in cVal] # kilometer conversion

    # converting from imperial units
    if outUnit == 'inches' or outUnit ==  'feet' or outUnit ==  'yards' or outUnit ==  'miles':
        cVal = [val*25.4, val * 2.54, val*0.0254, val * 0.0000254,  val, val/12, val/36, val/63360]

        if outUnit ==  'feet' or outUnit ==  'yards' or outUnit ==  'miles': # feet conversion
            cVal = [element * 12 for element in cVal]
        
            if outUnit ==  'yards' or outUnit ==  'miles': # yards conversion
                cVal = [element * 3 for element in cVal]

                if outUnit ==  'miles':
                    cVal = [element * 1760 for element in cVal]
    rounding = len(str(val))
    for u in range(len(units)): # outputs a list of converted measurements
        OutOut = str(round(cVal[u], rounding - int(math.floor(math.log10(abs(cVal[u]))))))
    output.insert(tkinter.END, cVal)

button = tkinter.Button(root, text="Convert", command=button_clicked)
button.pack()

output = tkinter.Text(root, height = 1, width = 10)
output.pack()

root.mainloop()