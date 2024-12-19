import tkinter as tk

def cajadeNumero():
    textPrimo = int(entradaNum.get())
    print(textPrimo)
    entradaNum.delete(0, 'end')
    return textPrimo
    
def verificacion():
    bandera = False
    numeroAVerificar = cajadeNumero()
    if numeroAVerificar>1:
        for num in range(2,numeroAVerificar):
            if numeroAVerificar % num == 0:
                bandera = True
                break
        if bandera is True:
            resultado.config(text=f"El {numeroAVerificar} no es primo.",fg="blue")
            
        if bandera is False:
            resultado.config(text=f" El {numeroAVerificar} es primo.", fg="green")
        
    

    else:
        resultado.config(text="Numero no valido",fg="red")

    
ventana= tk.Tk()
ventana.title("EsPrimo?")
ventana.geometry("400x300")
titulo = tk.Label(ventana, text="Verificador de numeros primos",font=("Arial", 16))
titulo.pack(pady=20)
texto = tk.Label(ventana, text="Ingrese un Numéro para verificar si es Primo",font=("Arial", 10))
texto.pack(pady=5)
entradaNum = tk.Entry(ventana, font=("Arial", 14), width=8)
entradaNum.pack()
boton = tk.Button(ventana,text=" verificar",command=verificacion)
boton.pack(pady=10)
resultado = tk.Label(ventana, text="",font=("Arial", 15),)
resultado.pack()

ventana.mainloop()
