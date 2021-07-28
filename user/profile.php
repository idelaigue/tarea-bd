<?php
include "../db_config.php";
include "../sesion/valida_sesion.php";
$pais = "SELECT nombre FROM pais WHERE cod_pais = $1";  
$resultpais = pg_query_params($dbconn, $pais, array($_SESSION["pais"]));
$paiss = pg_fetch_row($resultpais);
?>