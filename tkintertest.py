import tkinter as tk
from tkinter import ttk

"""def button_func():
    print("A button was pressed")

#create a window
window = tk.Tk()
window.title("Hello World")
window.geometry("900x700")

#create widgets
textbox = tk.Text(master = window)
textbox.pack()

#ttk widgets
label = ttk.Label(master = window, text = "Hello world")
label.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()

#ttk button
button = ttk.Button(master = window, text = "login", command = button_func )
button.pack()

#run
window.mainloop()"""

"""def button_func():
    # get the content of  the entry
    entry_text = entry.get()

    # update the label
    label["text"] = entry_text
    

# window
window = tk.Tk()
window.title("Test")
window.geometry("900x700")

# widgets
label = tk.Label(master = window, text = "Login")
label.pack()

entry = tk.Entry(master = window)
entry.pack()

button = tk.Button(master = window, text = "Login", command = button_func)
button.pack()


# run
window.mainloop()"""

"""def button_func():
    print(string_var.get())
    string_var.set("Button pressed")

#create window
window = tk.Tk()
window.title("rlghdg")
window.geometry("900x700")

#tkinter variables
string_var = tk.StringVar(value = "test")

#widgets
label = ttk.Label(master = window, text = "label", textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var,)
entry.pack()

button = ttk.Button(master = window, text = "Button", command= button_func)
button.pack()




#run
window.mainloop()"""

"""def button_func():
    print("basic button works")
    print(radio_var.get())

# create window
window = tk.Tk()
window.title("can you stop distracting him dude")
window.geometry("900x700")


#button
button = ttk.Button(master = window, text = "Button", command = button_func)
button.pack()

#checkbutton
check_var = tk.IntVar(value = 10)
check_button = ttk.Checkbutton(window, 
                               text = "check button 1", 
                               command = lambda: print(check_var.get()), 
                               variable = check_var, 
                               onvalue = 10,
                               offvalue = 5)
check_button.pack()

#radio button
radio_var = tk.StringVar()
radio_button1 = ttk.Radiobutton(window, text = "radio button 1", value = "radio button 1", command = lambda: print(radio_var.get()), variable = radio_var)
radio_button1.pack()
radio_button2 = ttk.Radiobutton(window, text = "radio button 2", value = "radio button 2", variable = radio_var)
radio_button2.pack()
#run
window.mainloop()"""

# create window
window = tk.Tk()
window.title("rgioe riu ghnrd ghber")
window.geometry("900x700")


#widgets
text = tk.Text(window)
text.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text = "A button")
button.pack()
#run
window.mainloop()