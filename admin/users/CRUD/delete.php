<?php
/* Este archivo debe manejar la lógica de borrar un usuario (y los registros relacionados) como admin */
include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

$id=$_REQUEST["id"];
$sql = "DELETE FROM  usuario WHERE usuarios.id=$id";
    

?>