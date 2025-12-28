# Porra para la Eurocopa 2016

**Date:** 2015-10-06
**Categories:** dev, django

Página de la porra → [Porra Eurocopa 2016](http://porra.zeneke.com)

Después de haber hecho varios intentos con distintas tecnologías entre otras:

- NodeJS
- AngularJS → Mencionar la single-web-app que realicé con AngularJS (pero sin backend) [Porra Mundial 2014](http://porrangular.zeneke.com)

Para realizar una aplicación web que permita gestionar una porra de la próxima Eurocopa 2016.
Al final me decanté por mi Framework preferido de siempre [Django](http://www.djangoproject.com).

La arquitectura de la aplicación es la siguiente:

* Nginx como servidor web
* uwsgi para la intercomunicación entre la aplicación en Django y Nginx
* Postgres como BBDD en el backend
* Django es el Framework sobre el que está montada la aplicación
* jQuery el API REST básico está basado en jQuery
