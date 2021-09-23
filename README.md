# Reto-QuantumRobotics
 Reto para el Area de Control

Objetivo: El objetivo de este reto es demostrar que tus conocimientos y habilidades corresponden con los “conocimientos indispensables”, mencionados en la vacante publicada en la página de Facebook de Quantum Robotics.

Descripción: Realizarás un programa escrito en python que lea un archivo de texto, el cual contendrá nombres de imágenes a analizar con OpenCV y creará un hilo de ejecución para el análisis de cada una de ellas.
Cada hilo hará un análisis muy sencillo de las imágenes, descrito como “conteo de objetos”.
El proceso principal del programa solo se encargará de extraer del archivo de texto el nombre de las imágenes (usando manipulación de cadenas), mientras que el hilo de ejecución realizará el conteo y lo imprimirá en pantalla con el siguiente mensaje “Yo soy el hilo que analizó la imagen bucks_and_cents_[IMAGEN_X].png y encontré x objetos”