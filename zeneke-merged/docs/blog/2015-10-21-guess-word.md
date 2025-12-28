# Guess Word en Django

**Date:** 2015-10-21
**Categories:** dev, django

Ya está la aplicación de Adivinar las Palabras funcionando → [GuessWord](http://guessword.zeneke.com/), la arquitectura es la misma que la aplicación de la porra:

* Nginx como servidor web
* uwsgi para la intercomunicación entre la aplicación en Django y Nginx
* Postgres como BBDD en el backend
* Django es el Framework sobre el que está montada la aplicación
* jQuery el API REST básico está basado en jQuery

Se graban estadísticas de cuánto se tarda en adivinar las palabras y cuántas personas se han rendido.
