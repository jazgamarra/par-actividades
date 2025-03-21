import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

public class EjemploURL {
    public static void main(String[] args) {
        try {
            String test_url = "http://www.pol.una.py";
            URL pagina1 = new URL(test_url);
            URL pagina2 = new URL("http", "grado.pol.una.py", 80, "index.html");

            imprimirDetallesURL("Primera Página", pagina1);
            imprimirDetallesURL("Segunda Página", pagina2);

        } catch (MalformedURLException e) {
            System.err.println("Error: La URL está mal formada - " + e.getMessage());
        } catch (IOException e) {
            System.err.println("Error de conexión - " + e.getMessage());
        }
    }

    private static void imprimirDetallesURL(String titulo, URL url) {
        System.out.println("***** " + titulo);
        System.out.println("Protocolo: " + url.getProtocol());
        System.out.println("Puerto: " + (url.getPort() != -1 ? url.getPort() : url.getDefaultPort()));
        System.out.println("Host: " + url.getHost());
        System.out.println("Archivo: " + url.getFile());
        System.out.println("External form: " + url.toExternalForm());
        System.out.println();
    }
}
