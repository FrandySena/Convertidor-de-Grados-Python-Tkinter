import tkinter as tk

ventana = tk.Tk()
ventana.title("Agenda Frandy")
ventana.geometry("410x350")
ventana.configure(bg="#C7EBFF")

#===============================================================================

frame_izq = tk.Frame(ventana, bg="#C7EBFF")
frame_izq.grid(row=0, column=0, padx=10, pady=3, sticky="n")

frame_der = tk.Frame(ventana, bg="#C7EBFF")
frame_der.grid(row=0, column=1, padx=10, pady=3, sticky="n")

frame_botones = tk.Frame(ventana, bg="#C7EBFF")
frame_botones.grid(row=1, column=0, padx=3, pady=3, sticky="n")

#===============================================================================

tk.Label(frame_izq, text="Nombre:", bg="#C7EBFF").grid(row=0, column=0, sticky="w")
entrada_nombre = tk.Entry(frame_izq)
entrada_nombre.grid(row=1, column=0, sticky="w")

tk.Label(frame_izq, text="Apellido:", bg="#C7EBFF").grid(row=2, column=0, sticky="w")
entrada_apellido = tk.Entry(frame_izq)
entrada_apellido.grid(row=3, column=0, sticky="w")

tk.Label(frame_izq, text="Email:", bg="#C7EBFF").grid(row=4, column=0, sticky="w")
entrada_email = tk.Entry(frame_izq)
entrada_email.grid(row=5, column=0, sticky="w")

tk.Label(frame_izq, text="Telefono:", bg="#C7EBFF").grid(row=6, column=0, sticky="w")
entrada_telefono = tk.Entry(frame_izq)
entrada_telefono.grid(row=7, column=0, sticky="w")

tk.Label(frame_izq, text="Direccion:", bg="#C7EBFF").grid(row=8, column=0, sticky="w")
entrada_direccion = tk.Entry(frame_izq)
entrada_direccion.grid(row=9, column=0, sticky="w")

#===============================================================================

lista_personas = {}

#===============================================================================

def guardar_contacto():
    nombre = entrada_nombre.get().strip()
    apellido = entrada_apellido.get().strip()
    email = entrada_email.get().strip()
    telefono = entrada_telefono.get().strip()
    direccion = entrada_direccion.get().strip()

    nombre_completo = f"{nombre} {apellido}".strip()

    if not nombre or not apellido:
        return

    lista_personas[nombre_completo] = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "telefono": telefono,
        "direccion": direccion
    }

    contactos.insert(tk.END, nombre + " " +  apellido)



def eliminar_contacto():
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("eliminar contacto")
    ventana_emergente.geometry("325x180")
    ventana_emergente.configure(bg="#C7EBFF")

    tk.Label(ventana_emergente, text="Ingrese el nombre y apellido del contacto a eliminar", bg="#C7EBFF").pack(pady=5)
    entrada_nombre = tk.Entry(ventana_emergente)
    entrada_nombre.pack(pady=5)

    mensaje = tk.Label(ventana_emergente, text="", bg="#C7EBFF")
    mensaje.pack(pady=5)

    def confirmar():
        nombre_buscado = entrada_nombre.get().strip()

        if not nombre_buscado:
            mensaje.config(text="ingrese un nombre")
            return

        if nombre_buscado in lista_personas:
            del lista_personas[nombre_buscado]

            for k, p in lista_personas.items():
                contactos.insert(tk.END, k)

            mensaje.config(text="Contacto eliminado.")

        else:
            mensaje.config(text="No se encontró el contacto.")

        contactos.delete(0, tk.END)
        for clave in lista_personas:
            contactos.insert(tk.END, clave)

    tk.Button(ventana_emergente, text="Eliminar", command=confirmar, bg="#75BCE2").pack(pady=10)
    tk.Button(ventana_emergente, text="Cancelar", command=ventana_emergente.destroy, bg="#75BCE2").pack()



def editar_contacto():
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("editar contacto")
    ventana_emergente.geometry("325x180")
    ventana_emergente.configure(bg="#C7EBFF")

    tk.Label(ventana_emergente, text="Ingrese el nombre y apellido del contacto a editar", bg="#C7EBFF").pack(pady=5)
    entrada_nombre = tk.Entry(ventana_emergente)
    entrada_nombre.pack(pady=5)

    mensaje = tk.Label(ventana_emergente, text="", bg="#C7EBFF")
    mensaje.pack(pady=5)

    def confirmar():
        nombre_completo = entrada_nombre.get().strip()

        if nombre_completo not in lista_personas:
            mensaje.config(text="No se encontró el contacto.")
            return

        ventana_sub_emergente = tk.Toplevel()
        ventana_sub_emergente.title("editar contacto")
        ventana_sub_emergente.geometry("400x345")
        ventana_sub_emergente.configure(bg="#C7EBFF")

        tk.Label(ventana_sub_emergente, text="Nombre", bg="#C7EBFF").pack(pady=5)
        entrada_nuevo_nombre = tk.Entry(ventana_sub_emergente)
        entrada_nuevo_nombre.pack(pady=5)

        tk.Label(ventana_sub_emergente, text="Apellido", bg="#C7EBFF").pack(pady=5)
        entrada_nuevo_apellido = tk.Entry(ventana_sub_emergente)
        entrada_nuevo_apellido.pack(pady=5)

        tk.Label(ventana_sub_emergente, text="Email", bg="#C7EBFF").pack(pady=5)
        entrada_nuevo_email = tk.Entry(ventana_sub_emergente)
        entrada_nuevo_email.pack(pady=5)

        tk.Label(ventana_sub_emergente, text="Teléfono", bg="#C7EBFF").pack(pady=5)
        entrada_nuevo_telefono = tk.Entry(ventana_sub_emergente)
        entrada_nuevo_telefono.pack(pady=5)

        tk.Label(ventana_sub_emergente, text="Dirección", bg="#C7EBFF").pack(pady=5)
        entrada_nuevo_direccion = tk.Entry(ventana_sub_emergente)
        entrada_nuevo_direccion.pack(pady=5)

        def confirmar_edicion():
            nuevo_nombre = entrada_nuevo_nombre.get().strip()
            nuevo_apellido = entrada_nuevo_apellido.get().strip()
            nuevo_nombre_completo = f"{nuevo_nombre} {nuevo_apellido}"

            if nuevo_nombre_completo != nombre_completo:
                lista_personas[nuevo_nombre_completo] = lista_personas.pop(nombre_completo)

            lista_personas[nuevo_nombre_completo]["nombre"] = nuevo_nombre
            lista_personas[nuevo_nombre_completo]["apellido"] = nuevo_apellido
            lista_personas[nuevo_nombre_completo]["email"] = entrada_nuevo_email.get().strip()
            lista_personas[nuevo_nombre_completo]["telefono"] = entrada_nuevo_telefono.get().strip()
            lista_personas[nuevo_nombre_completo]["direccion"] = entrada_nuevo_direccion.get().strip()

            contactos.delete(0, tk.END)
            for clave in lista_personas:
                contactos.insert(tk.END, clave)

            ventana_sub_emergente.destroy()
            ventana_emergente.destroy()

        tk.Button(ventana_sub_emergente, text="confirmar", command=confirmar_edicion, bg="#75BCE2").pack()

        mensaje.config(text="Contacto editado.")

    tk.Button(ventana_emergente, text="Editar", command=confirmar, bg="#75BCE2").pack(pady=10)
    tk.Button(ventana_emergente, text="Cancelar", command=ventana_emergente.destroy, bg="#75BCE2").pack()



def buscar_contacto():
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("buscar contacto")
    ventana_emergente.geometry("300x180")
    ventana_emergente.configure(bg="#C7EBFF")

    tk.Label(ventana_emergente, text="Ingrese el nombre del contacto a buscar", bg="#C7EBFF").pack(pady=5)
    entrada_nombre = tk.Entry(ventana_emergente)
    entrada_nombre.pack(pady=5)

    mensaje = tk.Label(ventana_emergente, text="", bg="#C7EBFF")
    mensaje.pack(pady=5)

    def filtrar_nombre():
        nombre_buscado = entrada_nombre.get().strip().lower()
        contactos.delete(0, tk.END)

        encontrados = 0
        for clave, datos in lista_personas.items():
            if nombre_buscado in datos["nombre"].lower():
                contactos.insert(tk.END, clave)
                encontrados += 1

        if encontrados == 0:
            mensaje.config(text="No se encontraron contactos")
        else:
            mensaje.config(text=f"{encontrados} contacto(s) encontrado(s)")

    tk.Button(ventana_emergente, text="Filtrar", command=filtrar_nombre, bg="#75BCE2").pack(pady=10)
    tk.Button(ventana_emergente, text="Cancelar", command=ventana_emergente.destroy, bg="#75BCE2").pack()



def restablecer_lista():
    contactos.delete(0, tk.END)
    for clave in lista_personas:
        contactos.insert(tk.END, clave)


def detallar_contacto():
    seleccion = contactos.curselection()
    if not seleccion:

        ventana_error = tk.Toplevel()
        ventana_error.title("Error")
        ventana_error.configure(bg="#C7EBFF")
        tk.Label(ventana_error, text="Seleccione un contacto primero", bg="#C7EBFF").pack(padx=20, pady=20)
        return

    indice = seleccion[0]

    nombre_completo = contactos.get(indice)

    if nombre_completo not in lista_personas:
        ventana_error = tk.Toplevel()
        ventana_error.title("Error")
        ventana_error.configure(bg="#C7EBFF")
        tk.Label(ventana_error, text="El contacto no existe", bg="#C7EBFF").pack(padx=20, pady=20)
        return

    datos = lista_personas[nombre_completo]

    ventana_sub_emergente = tk.Toplevel()
    ventana_sub_emergente.title("Detalles del contacto")
    ventana_sub_emergente.geometry("300x250")
    ventana_sub_emergente.configure(bg="#C7EBFF")

    tk.Label(ventana_sub_emergente, text=f"Nombre: {datos['nombre']}", bg="#C7EBFF").pack(pady=5)
    tk.Label(ventana_sub_emergente, text=f"Apellido: {datos['apellido']}", bg="#C7EBFF").pack(pady=5)
    tk.Label(ventana_sub_emergente, text=f"Email: {datos['email']}", bg="#C7EBFF").pack(pady=5)
    tk.Label(ventana_sub_emergente, text=f"Teléfono: {datos['telefono']}", bg="#C7EBFF").pack(pady=5)
    tk.Label(ventana_sub_emergente, text=f"Dirección: {datos['direccion']}", bg="#C7EBFF").pack(pady=5)

#===============================================================================

boton_agregar = tk.Button(frame_botones, text="agregar", command=guardar_contacto, bg="#75BCE2")
boton_agregar.grid(row=0, column=0, sticky="ew")

boton_eliminar = tk.Button(frame_botones, text="eliminar", command=eliminar_contacto, bg="#75BCE2")
boton_eliminar.grid(row=0, column=1, sticky="ew")

boton_editar = tk.Button(frame_botones, text="editar", command=editar_contacto, bg="#75BCE2")
boton_editar.grid(row=1, column=0, sticky="ew")

boton_filtrar = tk.Button(frame_botones, text="buscar", command=buscar_contacto, bg="#75BCE2")
boton_filtrar.grid(row=1, column=1, sticky="ew")

boton_restablecer = tk.Button(frame_botones, text="restablecer", command=restablecer_lista, bg="#75BCE2")
boton_restablecer.grid(row=2, column=0, sticky="ew")

boton_ver = tk.Button(frame_botones, text="ver detalles", command=detallar_contacto, bg="#75BCE2")
boton_ver.grid(row=2, column=1, sticky="ew")

#===============================================================================

despl = tk.Scrollbar(frame_der, bg="#75BCE2")
despl.grid(row=0, column=1, sticky="ns")

contactos = tk.Listbox(frame_der, width=23, height=14, yscrollcommand=despl.set)
contactos.grid(row=0, column=0, padx=0, pady=10, sticky="nsew")

despl.config(command=contactos.yview)

#===============================================================================

ventana.mainloop()