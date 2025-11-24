#Profesor melquisedec, aqui hago entrega de la tarea 2 de tkinter
#El cual trata de un calendario con dias de trabajo y descanso
#El cual se puede ajustar el dia de inicio y el modal de trabajo/descanso
#Nombre del profesor: Melquisedec Sierra
#Alumno: Said Riquelme
#Ramo: Lenguaje de Programacion
#Fecha: 18-10-2025

#Al correr este programa, usted podra ingresar el dia de inicio del turno
#Y será capaz de seleccionar el modal de trabajo a gusto 
# Días rojos son días de descanso
# Días verdes son días de trabajo
#Saludos :D

import tkinter as tk

def gen_cal():
    for w in f.winfo_children(): w.destroy()
    inicio = int(e1.get())
    w, r = map(int, e2.get().split('x')) 
    
    dia = 1
    for i in range(5): # 5 semanas
        for j in range(7): # 7 dias
            if dia > 31: break
                
            color = "green" if (dia - inicio) % (w + r) < w else "red"
            
            # Hice los días un poco más grandes para llenar el espacio, aqui se puede
            #ver los colores de los días y el tamaño de las etiquetas
            tk.Label(f, text=dia, bg=color, fg="white", width=5, height=2
                    ).grid(row=i, column=j, padx=2, pady=2)
            dia += 1
v = tk.Tk()
v.title("msierra_t2.py")
v.geometry("350x350") #Profesor, aqui se encuentra el ajuste de tamaño de la ventana

tk.Label(v, text="Inicio:").grid(row=0, column=0, pady=5)
e1 = tk.Entry(v, width=7)
e1.grid(row=0, column=1, pady=5)

tk.Label(v, text="Modal (ej: 4x4):").grid(row=1, column=0, pady=5)
e2 = tk.Entry(v, width=7)
e2.grid(row=1, column=1, pady=5)

#El codigo de abajo es para el boton de generar el calendario profe
tk.Button(v, text="Generar", command=gen_cal
          ).grid(row=2, column=0, columnspan=2, pady=10)

#la funcion de este condigo es para crear el frame donde se va a generar el calendario
f = tk.Frame(v) #f = frame
f.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

v.mainloop()