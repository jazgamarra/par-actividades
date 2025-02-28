# Actividad 1. Cliente HTTP

Se debe implementar un cliente http utilizable desde la línea de comandos utilizando java
como lenguaje base. Este cliente debe permitir realizar peticiones a cualquier URL pasada
como parámetro.

## Compilacion 
```javac HttpClientApp.java```
```jar cfe unHttpClient.jar HttpClientApp HttpClientApp.class```

## Para probar, se puede usar: 
```java -jar unHttpClient.jar -u https://pokeapi.co/api/v2/pokemon -m GET -p "limit=10&offset=0" ```
```java -jar unHttpClient.jar -u https://postman-echo.com/post -m POST -p "name=John&age=30"```

Jazmin Gamarra. 27/02/2025
