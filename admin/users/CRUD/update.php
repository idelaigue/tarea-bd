<?php
/* Este archivo debe manejar la lógica de borrar un usuario (y los registros relacionados) como admin */
include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';
    /* Este archivo debe manejar la lÃ³gica de obtener los datos de todos los usuarios */
    $sql = "SELECT * FROM usuario ";
    $result= pg_query($dbconn,$sql);
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $id=$_POST["id"];
        $nombre = $_POST["name"];
        $apellido = $_POST["surname"];
        $email = $_POST["email"];
        $contraseña = $_POST["pwd"];
        $contraseña_hasheada = password_hash($contraseña, PASSWORD_BCRYPT, $opciones);
        $pais = $_POST["country"];
        $sql1= "UPDATE usuarios SET nombre = $nombre ,apellido = $apellido, correo= $email, constraseña = $contraseña_hasheada , pais = $pais";
        
    }
?>