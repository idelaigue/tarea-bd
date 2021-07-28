<?php
include "../db_config.php";
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $name = $_POST["name"];
    $lastname = $_POST["surname"];
    $email = $_POST["email"];
    $pass = $_POST["pwd"];
    $pass2 = $_POST["pwd2"];
    $country = $_POST["country"];
    if ($pass == $pass2){
        $sqlemail = "SELECT * FROM usuario WHERE correo = $1 ";
        $resultemail = pg_query_params($dbconn, $sqlemail, array($email));
        $row = pg_fetch_row($resultemail);
        if(!$row) { 
            $sqlregistro =  "INSERT INTO usuario (nombre, apellido, correo, contraseña, pais, fecha_registro, tipo) VALUES ($1, $2, $3, $4, $5, $6, $7)";
            $opciones = array("cost" => 12);
            $hashpass = password_hash($pass, PASSWORD_BCRYPT, $opciones);
            $fecha = date("Y-m-d");
            $resultusuario = pg_query_params($dbconn, $sqlregistro, array($name, $lastname, $email, $hashpass, $country, $fecha, "usuario" ));
             }
            pg_close($dbconn);
            header('log-in.php');
        }
    else {
        echo "Hubo un error al solicitar los datos";
        pg_close($dbconn);
    }
}
header('log-in.php');
?>
