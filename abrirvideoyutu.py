#Importamos la librería webbrowser
import webbrowser

#Pedimos al usuario que ingrese el nombre de la canción
cancion = input("Ingrese el nombre de una canción: ")

#Abrimos el navegador y buscamos la canción
webbrowser.open("https://www.youtube.com/results?search_query=" + cancion)