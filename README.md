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
