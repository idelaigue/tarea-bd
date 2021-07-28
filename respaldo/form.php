<?php include 'db_config.php';


if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $pais = $_POST["pais"];
    $nro_cont = $_POST["nro_cont"];
    $sql = 'INSERT INTO Informe (pais, nro_cont) VALUES ($1, $2)';
    if( pg_query_params($dbconn, $sql, array($pais,$nro_cont)) !== FALSE ) {
        echo "Dato ingresado correctamente <br>";
        echo '<a href="lista.php"> lista de datos </a> <br>';
        echo '<a href="index.php"> Ingresar más datos </a> <br>';
        pg_close($dbconn);
    } else {
        echo "Hubo un error al ingresar el dato";
        pg_close($dbconn);
    }
}
?>