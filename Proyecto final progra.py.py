import tkinter as tk
import random
import numpy as np

#PROYECTO Final PROGRAMACION 1
#Version 1.265
#Programadores: 
#    Elder Geovany Yac Mul - 202007018
#    Andres Fernando Gonzalez Alcantara - 202308061
#    Denis Alexander Lucas Ramirez - 202207036

def f_clic_boton(fila, columna):
    # Obtenemos el valor del boton que fue pulsado
    boton_clic = ventana_matriz.grid_slaves(row=fila, column=columna)[0]
    valor_boton = boton_clic.cget("text")
    boton_clic.configure(bg="red",state="disable")
    print("Valor del botón clickeado:", valor_boton)

    global ventana_cronometro
    ventana_cronometro = tk.Toplevel(ventana_matriz)
    
    etiqueta = tk.Label(ventana_cronometro, font=("Helvetica", 48))
    etiqueta.pack(pady=20)

    # Inicializar el valor de los segundos en 25
    segundos = 25

    # Función para actualizar la etiqueta con el valor actual de segundos
    def actualizar_etiqueta():
        nonlocal segundos
        etiqueta.config(text=str(segundos))
        if segundos > 0:
            segundos -= 1
            etiqueta.after(1000, actualizar_etiqueta)

        if (segundos==0):
            bt_der_abj.configure(bg="black")
            bt_der_arr.configure(bg="black")
            bt_izq_arr.configure(bg="black")
            bt_izq_abj.configure(bg="black")
            bt_abajo.configure(bg="black")
            bt_arriba.configure(bg="black")
            bt_der.configure(bg="black")
            bt_izq.configure(bg="black")
            ventana_cronometro.destroy()
            ventana_opciones.destroy()

    # Llamar a la función para iniciar la cuenta regresiva
    actualizar_etiqueta()

    # Obtenemos los valores de los botones que rodean al boton pulsado y los guardamos en un vector
    valores_adyacentes = []

    # Verificamos si hay botón encima del boton pulsado
    if fila > 0:
        bt_arriba = ventana_matriz.grid_slaves(row=fila-1, column=columna)[0]
        valor_arriba = bt_arriba.cget("text")
        bt_arriba.configure(bg="yellow")
        valores_adyacentes.append(valor_arriba)

    # Verificamos si hay botón abajo del boton pulsado
    if fila < tamanio_matriz_ingresado - 1:
        bt_abajo = ventana_matriz.grid_slaves(row=fila+1, column=columna)[0]
        valor_abajo = bt_abajo.cget("text")
        bt_abajo.configure(bg="yellow")
        valores_adyacentes.append(valor_abajo)

    # Verificamos si hay botón a la izquierda del boton pulsado
    if columna > 0:
        bt_izq = ventana_matriz.grid_slaves(row=fila, column=columna-1)[0]
        valor_izq = bt_izq.cget("text")
        bt_izq.configure(bg="yellow")
        valores_adyacentes.append(valor_izq)

    # Verificamos si hay botón a la derecha del boton pulsado
    if columna < tamanio_matriz_ingresado - 1:
        bt_der = ventana_matriz.grid_slaves(row=fila, column=columna+1)[0]
        valor_derecha = bt_der.cget("text")
        bt_der.configure(bg="yellow")
        valores_adyacentes.append(valor_derecha)

    # Verificamos esquina superior izquierda
    if fila > 0 and columna > 0:
        bt_izq_arr = ventana_matriz.grid_slaves(row=fila-1, column=columna-1)[0]
        valor_izq_arr = bt_izq_arr.cget("text")
        bt_izq_arr.configure(bg="yellow")
        valores_adyacentes.append(valor_izq_arr)

    # Verificamos esquina superior derecha
    if fila > 0 and columna < tamanio_matriz_ingresado - 1:
        bt_der_arr = ventana_matriz.grid_slaves(row=fila-1, column=columna+1)[0]
        valor_der_arr = bt_der_arr.cget("text")
        bt_der_arr.configure(bg="yellow")
        valores_adyacentes.append(valor_der_arr)

    # Verificamos esquina inferior izquierda
    if fila < tamanio_matriz_ingresado - 1 and columna > 0:
        bt_izq_abj = ventana_matriz.grid_slaves(row=fila+1, column=columna-1)[0]
        valor_izq_abj = bt_izq_abj.cget("text")
        bt_izq_abj.configure(bg="yellow")
        valores_adyacentes.append(valor_izq_abj)

    # Verificamos esquina inferior derecha
    if fila < tamanio_matriz_ingresado - 1 and columna < tamanio_matriz_ingresado - 1:
        bt_der_abj = ventana_matriz.grid_slaves(row=fila+1, column=columna+1)[0]
        valor_der_abj = bt_der_abj.cget("text")
        bt_der_abj.configure(bg="yellow")
        valores_adyacentes.append(valor_der_abj)

    print("Valores de los botones adyacentes:", valores_adyacentes)
    np_valoresAdyacentes = np.array(valores_adyacentes)
    global resultado
    resultado = np_valoresAdyacentes.sum() * valor_boton
    print("El resultado de la operacion es: ", resultado)
    opciones_respuesta()

def crear_matriz(tamanio):
    global ventana_matriz
    ventana_matriz = tk.Toplevel(ventanaPrincipal)
    ventana_matriz.title("Matriz de Botones")

    jugador1 = jugador1_entry.get()
    jugador2 = jugador2_entry.get()
    jugador1_label = tk.Label(ventanaPrincipal, text=jugador1)
    jugador1_label.pack()
    jugador2_label = tk.Label(ventanaPrincipal, text=jugador2)
    jugador2_label.pack()

    global tamanio_matriz_ingresado
    tamanio_matriz_ingresado = tamanio
    for i in range(tamanio):
        for j in range(tamanio):
            valor = random.randint(0,11)
            button = tk.Button(ventana_matriz, text=valor, width=10, height=5, command=lambda fila=i, columna=j: f_clic_boton(fila, columna),bg="black")
            button.grid(row=i, column=j)
    
def iniciarJuego():
    tamanio_matriz = int(tamanio_entry.get())
    crear_matriz(tamanio_matriz)

def opciones_respuesta():
    global ventana_opciones
    ventana_opciones = tk.Toplevel(ventana_matriz)
    for i in range(0,2,1):
        for j in range(0,2,1):
            valor = random.randint(0,1000)
            if (i == 1 and j == 1):
                button = tk.Button(ventana_opciones, text=resultado, width=10, height=5, command=lambda fila=i, columna=j, bg="red": f_clic_botones_opciones(fila, columna))
                button.grid(row=i, column=j)
            else:
                button = tk.Button(ventana_opciones, text=valor, width=10, height=5, command=lambda fila=i, columna=j, bg="red": f_clic_botones_opciones(fila, columna))
                button.grid(row=i, column=j)

def f_clic_botones_opciones(fila, columna):

    boton_clic_op = ventana_opciones.grid_slaves(row=fila, column=columna)[0]
    valor_boton_op = boton_clic_op.cget("text")
    print("Valor del botón clickeado:", valor_boton_op)
    global contador_puntos
    global turnos
    if(turnos == 2):
        global ventana_ganador
        jugador1 = jugador1_entry.get()
        jugador2 = jugador2_entry.get()
        ventana_ganador = tk.Toplevel(ventana_matriz)
        ventana_ganador.title("Finalizar juego")
        ventana_ganador.geometry("450x450")

        jugador1_label = tk.Label(ventana_ganador, text=jugador1)
        jugador1_label.pack()
        jugador2_label = tk.Label(ventana_ganador, text=jugador2)
        jugador2_label.pack()

        ventana_cronometro.destroy()
        ventana_matriz.destroy()
        ventana_opciones.destroy()
    else:
        if(resultado == int(valor_boton_op)):
            print("Respuesta Correcta UwU")
            ventana_opciones.destroy()
            contador_puntos+=3
            turnos+=1
        else:
            print("Error. Respuesta Incorrecta UwU")
            ventana_opciones.destroy()
            turnos+=1

    print("El contador de puntos es:", contador_puntos)

contador_puntos = 0
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Ventana Principal")
ventanaPrincipal.geometry("450x450")
ventanaPrincipal.resizable(1,1)
ventanaPrincipal.iconbitmap("Logo-Meso-Color.ico")

# Etiqueta y entrada para el jugador 1
jugador1_label = tk.Label(ventanaPrincipal, text="Jugador 1:")
jugador1_label.pack()
jugador1_entry = tk.Entry(ventanaPrincipal)
jugador1_entry.pack()

# Etiqueta y entrada para el jugador 2
jugador2_label = tk.Label(ventanaPrincipal, text="Jugador 2:")
jugador2_label.pack()
jugador2_entry = tk.Entry(ventanaPrincipal)
jugador2_entry.pack()

# Etiqueta y entrada para el tamaño de la matriz
tamanio_label = tk.Label(ventanaPrincipal, text="Tamaño de la matriz:")
tamanio_label.pack()
tamanio_entry = tk.Entry(ventanaPrincipal)
tamanio_entry.pack()

# Cantidad de turnos por jugador
turnos_label = tk.Label(ventanaPrincipal, text="Ingrese la cantidad de Turnos por Jugador:")
turnos_label.pack()
turnos_entry = tk.Entry(ventanaPrincipal)
turnos_entry.pack()
turnos = 0

# Botón para iniciar el juego
boton_inicio = tk.Button(ventanaPrincipal, text="Iniciar Juego", command=iniciarJuego)
boton_inicio.pack()

ventanaPrincipal.mainloop()