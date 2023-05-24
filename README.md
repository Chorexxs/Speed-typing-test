# Speed Typing Test

Este programa te permite poner a prueba tu velocidad de escritura mediante un test de mecanografía. Genera una lista de palabras aleatorias y mide el tiempo que te toma escribir cada una de ellas. Al final del test, se calcula tu puntuación en palabras por minuto (wpm).

## Requisitos

- Python 3.x
- Biblioteca `time`

## Uso

1. Ejecuta el programa desde tu entorno de Python.
2. Al iniciarse, te dará la bienvenida y esperará a que presiones Enter para empezar el test.
3. Aparecerán las palabras aleatorias en la pantalla. Escribe cada palabra y presiona Enter para pasar a la siguiente.
4. Una vez que hayas terminado de escribir todas las palabras, se calculará tu puntuación en palabras por minuto y se mostrará en pantalla.

## Funcionamiento

El programa consta de las siguientes funciones:

- `get_words()`: Genera una lista de palabras aleatorias a partir de una lista predefinida.
- `start_typing(words)`: Muestra las palabras en pantalla y registra las palabras escritas por el usuario, calculando el tiempo transcurrido.
- `calculate_wpm(typed_words, time_elapsed)`: Calcula la puntuación en palabras por minuto a partir de las palabras escritas y el tiempo transcurrido.
- Programa principal: Muestra un mensaje de bienvenida, espera la entrada del usuario para comenzar el test, ejecuta las funciones anteriores y muestra la puntuación final.

## Ejemplo

```
Bienvenido al Speed Typing Test!
Presione Enter para empezar...

apple
banana
cat
dog
elephant
fox
grape
horse
island
jungle

Su puntuación es de 50.00 palabras por minuto.
```

En este ejemplo, se muestra la ejecución del programa donde el usuario escribe las palabras proporcionadas y se calcula su puntuación en palabras por minuto.

¡Ponte a prueba y mejora tu velocidad de escritura con este Speed Typing Test!
