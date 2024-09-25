import tkinter
import time

ventana = tkinter.Tk()
ventana.title("Mi primera ventana")

ventana.iconbitmap("icono.ico")

ventana.geometry("900x600")
ventana.resizable(False, False)

labelreloj = tkinter.LabelFrame(ventana, text="Contenedor del reloj", bg="green")
labelreloj.configure(width=800, height=500)

frame = tkinter.Frame(labelreloj)
frame.configure(bg="snow", bd=20, width=600, height=350)

etiqueta = tkinter.Label(frame, text="Aqui se mostrara la hora")
etiqueta.config(fg="black", bg="grey75", font=("Arial", 14, "bold"))

labelreloj.pack()
frame.pack()
etiqueta.pack()

def actualizarHora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000, actualizarHora)

actualizarHora()

ventana.mainloop()

