<?php
include "../db_config.php";
session_start();
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $user = $_POST["email"];
    $pass = $_POST["pwd"];
    $sqlusuario = "SELECT * FROM usuario WHERE correo = $1 ";
    $resultusuario = pg_query_params($dbconn, $sqlusuario, array($user));
    $row = pg_fetch_row($resultusuario);
    if($row) { 
        $contrahash = $row[4];
        //revisar si la contraseña corresponde con la de la base de datos
        if (password_verify ($pass, $contrahash)){
            //guardas los datos relevantes del usuario
            $_SESSION["nombre"] = $row[1];
            $_SESSION["apellido"] = $row[2];
            $_SESSION["correo"] = $row[3];
            $_SESSION["pais"] = $row[5];
            $_SESSION["tipo"] = $row[7];
            $_SESSION["fecha"] = $row[6];
            $_SESSION["id_usuario"] = $row[0];
            header('Location: ../index.php');
        }
        pg_close($dbconn);

    }
    else {
        echo "Hubo un error al solicitar los datos";
        pg_close($dbconn);
    }
}
header('log-in.php'); //No está registrado, por lo que se redirecciona al mainpage.php 
?>