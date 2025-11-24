#Listo profesor, presento mi trabajo equivalente para el certamen 2, en donde la calculadora es capaz de dividir, restar, multiplicar y sumar
#Ademas de que cada vez que presiona una tecla o el boton para resultado, la interfaz de la calculadora y los numeros, cambian de color
 #Aparte de esto, señalo que para que funcione correctamente, es necesario presionar los botones con el mouse, ya que no he logrado que funcione con el teclado

 # Nombre: Said Amaro Riquelme Ríos
 # Fecha: 12-10-2025
 # Asignatura: Programación
 # Carrera: Ingeniería Ejecución Mecánica


import tkinter as tk, random
#Señalo que se usara la libreria random para los colores
#Y que además, apartir de aquí comienza el codigo de la calculadora para cambiar de color
def click(v, b):
    e.insert(tk.END, v)
    colores = ["red","green","pink","purple","orange","yellow", "cyan", "magenta", "lightgrey"]
    b.config(bg=random.choice(colores))

def borrar(): e.delete(0, tk.END)

def calcular():
    try:
        r = eval(e.get())   
        #Este "r = eval" es la funcion que me ayuda a que se haga la operación correspondiente sin necesidad de crear
        #distintas líneas de código para cada operación #Protip muejeje
        e.delete(0, tk.END)
        e.insert(0, r)
        colores = ["red","green","pink","purple","orange","yellow", "cyan", "magenta", "lightgrey"]
        ventana.config(bg=random.choice(colores))
    except: e.delete(0, tk.END); e.insert(0,"Error")

ventana = tk.Tk(); ventana.title("Calculadora trabajo certamen 2")
e = tk.Entry(ventana, width=18, font=("Arial",18)); e.grid(row=0,column=0,columnspan=4)

#Profesor, en esta parte del codigo, se crean los botones y se les asigna su respectiva funcion
#para que al ser presionados, aparezca la suma solicitada en la pantalla de la calculadora
#Ademas de que cada vez que se presiona un boton, este cambia de color
bts = []
b = ["7","8","9","/","4","5","6","*","1","2","3","-","0",".","=","+"]
for i,x in enumerate(b):
    if x=="=":
        btn = tk.Button(ventana,text=x,width=15,height=3,command=calcular)
    else:
        btn = tk.Button(ventana,text=x,width=15,height=3,command=lambda v=x,b=None: None)
        
        btn.config(command=lambda v=x, b=btn: click(v,b))
    btn.grid(row=i//4+1,column=i%4)
    bts.append(btn)

tk.Button(ventana,text="C",width=22,height=2,bg="lightgreen",command=borrar).grid(row=5,column=0,columnspan=4)

for i in range(3):
    if i==2: print("Listo")

ventana.mainloop()
#Saludos profesor, espero que le guste mi trabajo y que pueda aprobar el certamen 2 xD