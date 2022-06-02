from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

app = Tk()
app.title("GraphApp")
X = []
Y = []

wrapper = ttk.Frame(app, padding="125 125 125 125")
wrapper.grid(column=0, row=0)

ttk.Label(app, text="Linear Regression Scatter Graph",font=('Arial',12,'bold')).grid(column=2, row=0, columnspan=5, ipadx=3)
ttk.Label(app, text="github.com/SaeedAbdulrahman",font=('Arial',9,'underline')).grid(column=2, row=1, columnspan=5, ipadx=3)

ttk.Label(app, text="X:").grid(column=1, row=2)
x_value = StringVar()
x_entry = ttk.Entry(app, width=4, textvariable=x_value)
x_entry.grid(column=2, row=2)

ttk.Label(app, text="Y:").grid(column=3, row=2)
y_value = StringVar()
y_entry = ttk.Entry(app, width=4, textvariable=y_value)
y_entry.grid(column=4, row=2)

ttk.Label(app, text="Slope: ").grid(column=1, row=4, columnspan=2)
slope_value = StringVar()
intercept_label = ttk.Label(app, textvariable=slope_value).grid(column=2, row=4, columnspan=5)

ttk.Label(app, text="Intercept: ").grid(column=1, row=5, columnspan=2)
intercept_value = StringVar()
intercept_label = ttk.Label(app, textvariable=intercept_value).grid(column=2, row=5, columnspan=5)

ttk.Label(app, text="Equation: ").grid(column=1, row=6, columnspan=2)
le_value = StringVar()
le_label = ttk.Label(app, textvariable=le_value).grid(column=2, row=6, columnspan=5)

def update_stats():
    global X, Y, slope_value, intercept_value, le_value
    slope, intercept = np.polyfit(X,Y,1)
    slope_value.set(str(round(slope, 3)))
    intercept_value.set(str(round(intercept, 3)))
    equation = f"{str(round(slope, 3))}x + ({str(round(intercept, 3))})"
    le_value.set(equation)
    
def add_value():
    global X, Y
    x_value = x_entry.get()
    y_value = y_entry.get()
    if x_value.isnumeric() and y_value.isnumeric():
        X.append(float(x_value))
        Y.append(float(y_value))
        xy_table.insert(parent='', index='end', iid=len(X), text='', values=(x_value,y_value))
        x_entry.delete(0, 'end')
        y_entry.delete(0, 'end')
        update_stats()

ttk.Button(app, text=">", command=add_value, width=8, padding=1).grid(column=6, row=2)

table_columns = ('X','Y')
xy_table = ttk.Treeview(app, columns=table_columns, show='headings', height=5)
xy_table.grid(column=1, row=3, columnspan=6)
xy_table.heading("X", text="X")
xy_table.heading("Y", text="Y")
xy_table.column("X",width=95)
xy_table.column("Y",width=95)

table_scrollbar = ttk.Scrollbar(app, orient=tk.VERTICAL, command=xy_table.yview)
xy_table.configure(yscroll=table_scrollbar.set)
table_scrollbar.grid(column=6, row=3, sticky="ns")

def show_graph():
    global X, Y
    graphWindow = Toplevel(app)
    graphWindow.title("Graph")
    graphWindow.geometry('500x300')
    figure = Figure(figsize=(6,6))
    graph = figure.add_subplot(111)
    graph.plot(X,Y, c="green", alpha=0.7)
    graph_canvas = FigureCanvasTkAgg(figure, master=graphWindow)
    graph_canvas.draw()
    graph_canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    toolbar = NavigationToolbar2Tk(graph_canvas, graphWindow)
    toolbar.update()
    graph_canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  

ttk.Button(app, text="Show Graph", command=show_graph, width=10, padding=2).grid(column=1, row=7, columnspan=6)

app.mainloop()