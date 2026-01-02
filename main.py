import tkinter as tk

ventana = tk.Tk()
ventana.title("Convetor de grados Frandy")
ventana.geometry("410x350")
ventana.configure(bg="#C7EBFF")
ventana.grid_columnconfigure(0, weight=1)

#===============================================================================

frame_izq = tk.Frame(ventana, bg="#C7EBFF")
frame_izq.grid(row=0, column=0, padx=10, pady=3, sticky="n")

frame_botones = tk.Frame(ventana, bg="#C7EBFF")
frame_botones.grid(row=1, column=0, padx=3, pady=3, sticky="n")

#===============================================================================

tk.Label(frame_izq, text="Ingrese los grados a convertir:", bg="#C7EBFF").grid(row=0, column=0, sticky="ew")
entrada_grados = tk.Entry(frame_izq)
entrada_grados.grid(row=1, column=0, sticky="ew")

opcion_seleccion = tk.StringVar()
opcion_seleccion.set("Seleccione grados a calcular")
opciones_seleccion = ["Celsius", "Fahrenheit", "Kelvin"]

opcion_conversion = tk.StringVar()
opcion_conversion.set("Seleccione a convertir")
opciones_conversion = ["Celsius", "Fahrenheit", "Kelvin"]

menu_seleccion = tk.OptionMenu(frame_izq, opcion_seleccion, *opciones_seleccion)
menu_seleccion.grid(row=2, column=0, sticky="ew", pady= 5)
menu_seleccion.config( bg="#75BCE2")
menu_seleccion["menu"].config(bg="#75BCE2")

menu_conversion = tk.OptionMenu(frame_izq, opcion_conversion, *opciones_conversion)
menu_conversion.grid(row=3, column=0, sticky="ew", pady= 5)
menu_conversion.config( bg="#75BCE2")
menu_conversion["menu"].config(bg="#75BCE2")

resultado = tk.Label(frame_izq, text="", bg="#C7EBFF")
resultado.grid(row=4, column=0, sticky="ew")

#===============================================================================

unidades = ("Celsius", "Fahrenheit", "Kelvin")

conversiones = {
    ("Celsius", "Fahrenheit"): lambda c: (c * 9/5) + 32,
    ("Celsius", "Kelvin"):     lambda c: c + 273.15,

    ("Fahrenheit", "Celsius"): lambda f: (f - 32) * 5/9,
    ("Fahrenheit", "Kelvin"):  lambda f: (f - 32) * 5/9 + 273.15,

    ("Kelvin", "Celsius"):     lambda k: k - 273.15,
    ("Kelvin", "Fahrenheit"):  lambda k: (k - 273.15) * 9/5 + 32,
}

def convertir():
    try:
        valor = float(entrada_grados.get())
    except ValueError:
        resultado.config(text="Ingrese un número válido")
        return

    escala_seleccion = opcion_seleccion.get()
    escala_conversion = opcion_conversion.get()

    if escala_seleccion == escala_conversion:
        resultado.config(text="Seleccione escalas distintas")
        return

    clave = (escala_seleccion, escala_conversion)

    if clave in conversiones:
        conversion = conversiones[clave](valor)
        resultado.config(text=f"{valor}° {escala_seleccion} en {escala_conversion} = {conversion:.2f}° ")
    else:
        resultado.config(text="Conversión no válida")


#===============================================================================

boton_convertir = tk.Button(frame_botones, text="convertir", command=convertir, bg="#75BCE2")
boton_convertir.grid(row=0, column=0, sticky="ew")

#===============================================================================

ventana.mainloop()
