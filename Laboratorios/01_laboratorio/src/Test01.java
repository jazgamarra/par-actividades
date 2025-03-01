import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

class Test01 {
    public static void main(String[] args) {
        String url = "https://www.datos.gov.py/dataset/proyectos-adjudicados-hackathon";
        try {
            String respuesta = peticionHttpGet(url);
            System.out.println("La respuesta es:\n" + respuesta);
        } catch (Exception e) {
            System.err.println("Error al hacer la petición: " + e.getMessage());
        }
    }

    public static String peticionHttpGet(String urlParaVisitar) throws Exception {
        StringBuilder resultado = new StringBuilder();
        URL url = new URL(urlParaVisitar);
        HttpURLConnection conexion = (HttpURLConnection) url.openConnection();
        conexion.setRequestMethod("GET");

        // Manejar código de respuesta HTTP
        int status = conexion.getResponseCode();
        if (status != HttpURLConnection.HTTP_OK) {
            throw new RuntimeException("Error en la petición: " + status);
        }

        BufferedReader rd = new BufferedReader(new InputStreamReader(conexion.getInputStream()));
        String linea;
        while ((linea = rd.readLine()) != null) {
            resultado.append(linea).append("\n");
        }
        rd.close();
        conexion.disconnect();  // Cerrar la conexión

        return resultado.toString();
    }
}
