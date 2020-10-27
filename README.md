# CregevalBI

<b>Nota: Este instructivo únicamente tiene las indicaciones de ejecución y arranquel del proyecto en su fase de desarrollo.</b> 

Este proyecto está escrito bajo el framework Django para el back-end, el front está diseñado a base de Bootstrap y HTML.
Para su uso correcto se recomienda usar el IDE <a href="https://www.jetbrains.com/es-es/pycharm/download/">PyCharm</a> y
tener <a href="https://www.anaconda.com/products/individual">Anaconda</a> previamente instalado.

### 1. Previo a la ejecución del proyecto
Para ejecutar el proyecto se recomienda seguir los siguientes pasos:

* Instalar el IDE Pycharm (preferiblemente en su versión professional aunque la comunity tambien sirve).
* Posterior a la instalación, ejecutar Pycharm. En la ventana de inico se encontrarán listadas tres opciones a escoger:

    1.  <i>Create New Project</i>
    2. <i>Open</i>
    3. <i>Get from Version Control</i>
    
    Seleccionar la opción de <b>Get from Version Control</b> para clonar el repositorio del proyecto.

* Dentro del panel de Pycharm se puede clonar el repositorio por meido del .git del mismo o dimplemente ingresando con 
el usuario que tenga acceso a este. Lugo de esto el repositorio será clonado y se abrirá el proyecto.

* Con el proyecto abierto dentro del Pycharm nos dirigimos a la esquina inferior derecha del IDE para configurar el 
interprete. Dentro del panel configuramos un interprete Conda con Python versión 3.8 o superior.

### 2. Instalación de parametros para el proyecto

Para ejecutar el proyecto sin inconvenientes es requerido instalar los requerimientos del proyecto, los cuales 
inclujen el propio framework de Django. Para ello ejecutamos el siguiente comando en la terminal, la cual se accede desde
el propio IDE:

```pip install -r requirements.txt```

Con dicho comando se instalarán todos los paquetes pip requeridos para la ejecución correcta del proyecto.

### 3. Ejecución

Con todo preparado, para la administración y manipulación del proyecto se requieren usar los comandos Django, concretamente
para la ejecución se requiere utilizar el siguiente comando:

``python manage.py runserver``

Si todo está en orden, el proyecto inicializará de forma correcta. Para conocer otros comandos Django de utilidad para el proyecto
ejecutar el siguiente:

```python manage.py help```

<b>NOTA: Para temas de producción, despliegue y alojamiento consultar al equipo desarrollador.</b>