import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import javax.net.ssl.HttpsURLConnection;

public class Test02 {
    public static void main(String[] args) {
        // URL para probar HTTP
        String httpUrl = "http://grado.pol.una.py";
        // URL para probar HTTPS
        String httpsUrl = "https://grado.pol.una.py";

        System.out.println("Haciendo solicitud HTTP:");
        realizarPeticion(httpUrl, false);

        System.out.println("\nHaciendo solicitud HTTPS:");
        realizarPeticion(httpsUrl, true);
    }

    public static void realizarPeticion(String urlString, boolean esHttps) {
        try {
            URL url = new URL(urlString);
            HttpURLConnection connection;

            // Usar HttpsURLConnection si es HTTPS
            if (esHttps) {
                connection = (HttpsURLConnection) url.openConnection();
            } else {
                connection = (HttpURLConnection) url.openConnection();
            }

            // Configuración de la solicitud
            connection.setRequestMethod("GET");
            connection.setConnectTimeout(5000); // Tiempo máximo de conexión (5s)
            connection.setReadTimeout(5000); // Tiempo máximo de lectura (5s)
            connection.setRequestProperty("User-Agent", "Mozilla/5.0"); // Evita bloqueos por ciertos servidores

            int status = connection.getResponseCode();
            if (status != HttpURLConnection.HTTP_OK) {
                System.out.println("Error: Código HTTP " + status);
                connection.disconnect();
                return;
            }

            // Leer respuesta
            try (BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String inputLine;
                StringBuilder response = new StringBuilder();
                while ((inputLine = in.readLine()) != null) {
                    response.append(inputLine).append("\n");
                }
                System.out.println("Respuesta del servidor:\n" + response);
            }

            connection.disconnect();
        } catch (IOException e) {
            System.err.println("Error en la petición: " + e.getMessage());
        }
    }
}
    