# Proyecto ETL con Apache Nifi

### Objetivo del proyecto
El objetivo principal de este proyecto es demostrar un conocimiento práctico de los componentes y funcionalidades clave de Apache NiFi en el contexto de un pipeline de Extracción, Transformación y Carga (ETL). A través de esta implementación, se busca evidenciar la capacidad de diseñar, construir y operar flujos de datos utilizando esta potente herramienta.

### Requisitos previos del sistema
Java Development Kit (JDK): NiFi requiere Java para funcionar. Es crucial tener la variable de entorno JAVA_HOME configurada correctamente.
* Comprobación de Java para sistemas Unix:
```
java -version
echo $JAVA_HOME
```
* Instalación:
```
sudo apt update
sudo apt install openjdk-11-jdk
```
Para mayor información puedes recurrir a la [documentación oficial.](https://nifi.apache.org/components/)

### Descarga de Apache Nifi
Puedes verificar la versión que deseas descargar [aquí.](https://nifi.apache.org/download/)
* Descarga:
```
wget https://dlcdn.apache.org/nifi/2.4.0/nifi-2.4.0-source-release.zip
```
* Extraer Nifi
```
unzip nifi-2.4.0-source-release.zip
```
* Mover el directorio (recomendado)
```
mv nifi-2.4.0 /opt/
```
### Iniciar interfaz gráfica de Nifi
Se debe navegar al directorio *bin* dentro de la carpeta de NiFi y ejecutar el script de inicio
```
cd /opt/nifi/nifi-2.4.0/bin
```
Dentro de este directorio debes ejecutar:

```./nifi.sh start``` para iniciar nifi

```./nifi.sh stop``` para detener nifi

```./nifi.sh restart``` para reiniciar nifi

### Log in

Puedes acceder a la UI desde [https://localhost:8443/nifi/](https://localhost:8443/nifi/)

Deberías ver algo como esto:

![log in](./img/00_log-in.png)

Si encuentras algún problema en este paso debería verificar tu puerto por defecto:
```
nano /opt/nifi/nifi-2.4.0/conf/nifi.properties
```
![](./img/00_port.png)

### Genera tus credenciales
Si bien Nifi genera unas credenciales por defecto, es buena práctica generar un usuario y contraseñas de acceso unico.

Primero debes detener apache Nifi con el comando descrito mas arriba. Luego debes ejecutar lo siguiente dentro del directorio `opt/nifi/nifi-2.4.0/bin/`:
```
./nifi.sh set-single-user-credentials "nuevo_usuario" "nueva_contraseña"
```
La contraseña debe tener 12 caracteres como minimo.

Ahora podemos comenzar nuestro proyecto ETL.
