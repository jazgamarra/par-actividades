import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class PeticionGET {

    public static void main(String[] args) {
        String var_url = "https://www.google.com/";
        realizarPeticion(var_url);
    }

    public static void realizarPeticion(String urlString) {
        try {
            URL url = new URL(urlString);
            HttpURLConnection conexion = (HttpURLConnection) url.openConnection();

            // Configurar la conexión
            conexion.setRequestMethod("GET");
            conexion.setConnectTimeout(5000); // Máximo 5s para conectar
            conexion.setReadTimeout(5000); // Máximo 5s para leer
            conexion.setRequestProperty("User-Agent", "Mozilla/5.0"); // Evita bloqueos

            int status = conexion.getResponseCode();
            if (status != HttpURLConnection.HTTP_OK) {
                System.out.println("Error: Código HTTP " + status);
                conexion.disconnect();
                return;
            }

            // Leer respuesta
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(conexion.getInputStream()))) {
                String linea;
                StringBuilder respuesta = new StringBuilder();
                while ((linea = reader.readLine()) != null) {
                    respuesta.append(linea).append("\n");
                }
                System.out.println("Respuesta del servidor:\n" + respuesta);
            }

            conexion.disconnect();

        } catch (MalformedURLException e) {
            System.err.println("URL mal formada: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("Error en la conexión: " + e.getMessage());
        }
    }
}
