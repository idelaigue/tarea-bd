<?php
include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

/* Este archivo debe manejar la lógica de obtener los datos de un determinado usuario */
$id=$_REQUEST["id"];
$sql= "SELECT * FROM usuario WHERE usuario.id =$id" ;
$resultado= pg_query_params($dbconn, $sql, array( ));
$row = pg_fetch_assoc($result);
function idos($row){
    echo $row["id"];
}
function nombre($row){
    echo $row["nombre"];
}
function ap($row){
    echo $row["apellido"];
}
function corr($row){
    echo $row["correo"];
}
function cntr($row){
    echo $row["contraseña"];
}
function pais($row){
    echo $row["pais"];
}


?>