<?php
/* Este archivo debe manejar la lógica para crear un usuario como admin */

    include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';
    /* Este archivo debe manejar la lógica de obtener los datos de todos los usuarios */
    $sql = "SELECT max(id) FROM usuario order by max(id)";
    $result= pg_query($dbconn,$sql);
    $opciones = array('cost'=>12);

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $id=$result+1;
        $nombre = $_POST["name"];
        $apellido = $_POST["surname"];
        $email = $_POST["email"];
        $contraseña = $_POST["pwd"];
        $contraseña_hasheada = password_hash($contraseña, PASSWORD_BCRYPT, $opciones);
        $pais = $_POST["country"];
        $sql = "INSERT INTO usuario (id,nombre, apellido, correo, contraseña, pais)VALUES (".$id.",'".$nombre."','".$apellido."','".$email."','".$contraseña."',".$pais.")";
        if( pg_query_params($dbconn, $sql, array($id,$nombre,$apellido,$email,$contraseña_hasheada,$pais)) !== FALSE ) {
            echo "Dato ingresado correctamente <br>";
            echo '<a href="usuarios.html"> lista de datos </a> <br>';
            echo '<a href="index.php"> Ingresar más datos </a> <br>';
            pg_close($dbconn);
        } else {
            echo "Hubo un error al ingresar el dato";
            pg_close($dbconn);
        }
    }
    

        
?>