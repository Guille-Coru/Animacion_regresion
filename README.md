# Animación ventanas críticas
## Manim
Con la libreria ``manim`` de Python se pueden hacer algunas animaciones de forma programática. Un pequeño ejemplo introductorio es la animación ``ejemplo_peque(2).gif`` generado con el programa ``ejemplo2grad`` donde se ilustra que las raices de un polinomio no cambian al multiplicar dicho polinomio por una constante. Hay una comunidad, pequeña pero muy activa, manteniendo esta libreria y cada cierto tiempo aparecen nuevas funcionalidades.  Esta es la librería que usa el divulgador **3Blue1Brown** para crear sus animaciones en youtube. Para conocer más es recomendable visitar https://www.manim.community/.
## El programa principal
Tanto el programa ``vtrack1.py`` como ``muestranim28ab.R`` surgieron para visualizar ciertos resultados acerca de la ventana crítica del estimador de Parzen-Rosenblatt:
 $$\hat{f}\left(x\right)=\displaystyle\frac{1}{n}\displaystyle\sum_{i=1}^{n}K_h\left(X_i-x\right)$$
Donde $K_h$ es un núcleo reescalado. Si bien puede cambiarse el tipo de núcleo a utilizar, uno de los resultados más importantes es de monotonía del número de modas respecto al parámetro $h$ y este resultado solo es válido para núcleos gaussianos. Es por ello que en el programa este sea el núcleo implementado.
El ejemplo implementado ahora es de una muestra generada en ``R``, tiene distintas muestras que se pueden comentar y descomentar por bloques con el shortcut que tengas establecido para ello.
El programa de ``R`` es genera mixturas de distintas distribuciones clásicas y luego genera un archivo .txt con el que se hace fácil pasarle la muestra al archivo python. Sin embargo si el usuario tiene una muestra propia con la que quiere probar el programa solo tiene que incluirla en el código, comentando la muestra que el código usa previamente. 
Como ejemplo el gif ``dicotomia_ventana_critica.gif`` ilustra el método de dicotomía para encontrar la ventan crítica de $4$ modas. 
### Recomendación
Se recomienda descargar el código entero del programa ``vtrack1.py`` para visualización en un editor de Python. Pues las muestras comentadas con las que se hicieron pruebas antes de generar las animaciones usadas en la exposición del trabajo se pueden comprimir para no ocupar tantas líneas y poder centrarse en aquellas que realmente son código.   
