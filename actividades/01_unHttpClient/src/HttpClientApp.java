package unHttpClient.src;
import java.io.*;
import java.net.*;
import java.util.*;

public class HttpClientApp {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Sintaxis: java -jar unHttpClient.jar -u <URL> -m <GET/POST> [-p <parametros>]");
            return;
        }

        String url = "";
        String method = "GET"; // metodo por default 
        String params = "";

        for (int i = 0; i < args.length; i++) {
            switch (args[i]) {
                case "-u": // la siguiente cadena es la URL
                    url = args[++i];
                    break;
                case "-m": // la siguiente cadena es el metodo
                    method = args[++i].toUpperCase();
                    break;
                case "-p": // la siguiente cadena son los parametros (si hay)
                    params = args[++i];
                    break;
            }
        }

        try {
            sendHttpRequest(url, method, params);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    private static void sendHttpRequest(String urlString, String method, String params) throws IOException {
        if (!params.isEmpty() && method.equals("GET")) {
            urlString += "?" + params; // si se recibieron parametros, se agregan al query 
        }

        // Crear la conexion
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod(method);
        connection.setRequestProperty("User-Agent", "Java HTTP Client");

        if (method.equals("POST") && !params.isEmpty()) {
            connection.setDoOutput(true);
            OutputStream os = connection.getOutputStream();
            os.write(params.getBytes());
            os.flush();
            os.close();
        }

        System.out.println("HTTP Request:");
        System.out.println(method + " " + urlString);

        System.out.println("\nHTTP Response:");
        System.out.println("Status: " + connection.getResponseCode() + " " + connection.getResponseMessage());

        for (Map.Entry<String, List<String>> header : connection.getHeaderFields().entrySet()) {
            if (header.getKey() != null) {
                System.out.println("Header: " + header.getKey() + " Value: " + String.join(", ", header.getValue()));
            }
        }

        BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine).append("\n"); 
        }
        in.close();

        System.out.println("\nResponse Body:\n" + response);
    }
}
