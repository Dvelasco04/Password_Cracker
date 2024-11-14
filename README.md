# Password Cracker Project

Este proyecto es un script de Python que intenta adivinar una contraseña ingresada por el usuario. Utiliza un enfoque de fuerza bruta generando combinaciones aleatorias de caracteres hasta encontrar la coincidencia con la contraseña proporcionada.

## Descripción

El script utiliza la biblioteca `random` y el módulo `string` de Python para crear combinaciones aleatorias de letras (mayúsculas y minúsculas), números y caracteres especiales. El proceso continúa hasta que la combinación generada coincida con la contraseña introducida por el usuario.

### Cómo funciona

1. El usuario ingresa una contraseña.
2. El script genera un intento aleatorio de contraseña con la misma longitud que la contraseña proporcionada.
3. El script repite el proceso hasta que el intento aleatorio coincide con la contraseña del usuario.
4. Una vez que el script adivina correctamente la contraseña, se imprime el resultado.

**Nota**: Este script es solo un ejemplo educativo y no debe ser utilizado para actividades de fuerza bruta en sistemas reales.

## Requisitos

- Python 3.x

## Ejecución del script

1. Asegúrate de tener Python 3 instalado en tu máquina.
2. Descarga el archivo `password_cracker.py` o copia el siguiente código en un archivo `.py`:

```python
import random
import string

character_list = string.ascii_letters + string.digits + string.punctuation
password = input("Enter your password: ")
guess = ""

while guess != password:
    guess = random.choices(character_list, k=len(password))
    guess = "".join(guess)

print("Your password is " + guess)
```
Ejecuta el script con el siguiente comando:
```bash
python password_cracker.py
```
>[!warning]
>Este proyecto es solo para fines educativos y para demostrar cómo funciona un ataque de fuerza bruta en teoría. No debe usarse en aplicaciones del mundo real ni para comprometer la seguridad de otros.

Contribuciones
Las contribuciones son bienvenidas. Siéntete libre de hacer un fork de este repositorio y enviar un pull request con mejoras o sugerencias.
