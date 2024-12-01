import tkinter as tk
import webbrowser

def abrir_pestañas():
    # Palabra clave ingresada por el usuario
    palabraClave = entrada.get()

    # Categorías seleccionadas
    urls = []

    if var_archivos.get():
        urls.extend([
            f"https://www.google.com/search?q={palabraClave}+filetype:pdf",
            f"https://www.google.com/search?q={palabraClave}+filetype:doc",
            f"https://www.google.com/search?q={palabraClave}+ext:json",
        ])

    if var_sitios.get():
        urls.extend([
            f"https://www.google.com/search?q={palabraClave}+site:drive.google.com",
            f"https://www.google.com/search?q={palabraClave}+site:docs.google.com",
            f"https://www.google.com/search?q={palabraClave}+site:github.com",
            f"https://www.google.com/search?q={palabraClave}+site:reddit.com",
            f"https://www.google.com/search?q={palabraClave}+site:youtube.com",
            f"https://www.google.com/search?q={palabraClave}+site:x.com",
            f"https://www.google.com/search?q={palabraClave}+site:studocu.com",
        ])

    if var_filtros.get():
        urls.extend([
            f"https://www.google.com/search?q=allintext:{palabraClave}",
            f"https://www.google.com/search?q=intext:{palabraClave}",
            f"https://www.google.com/search?q=intitle:{palabraClave}",
            f"https://www.google.com/search?q=inurl:{palabraClave}",
            f"https://www.google.com/search?q=allintitle:{palabraClave}",
            f"https://www.google.com/search?q=link:{palabraClave}",
            f"https://www.google.com/search?q=inanchor:{palabraClave}",
        ])

    # Abre cada URL en una pestaña nueva del navegador
    for url in urls:
        webbrowser.open_new_tab(url)

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("KeywordSearch")

# Entrada para palabra clave
tk.Label(ventana, text="Palabra clave (opcional):").pack()
entrada = tk.Entry(ventana, width=40)
entrada.pack()

# Checkboxes para seleccionar tipos de búsqueda
var_archivos = tk.BooleanVar()
var_sitios = tk.BooleanVar()
var_filtros = tk.BooleanVar()

tk.Checkbutton(ventana, text="Búsquedas de archivos", variable=var_archivos).pack()
tk.Checkbutton(ventana, text="Búsquedas por sitios", variable=var_sitios).pack()
tk.Checkbutton(ventana, text="Búsquedas con filtros avanzados", variable=var_filtros).pack()

# Botón para realizar la búsqueda
tk.Button(ventana, text="Buscar", command=abrir_pestañas).pack()

ventana.mainloop()
