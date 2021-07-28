<?php
include "../db_config.php";
include "../sesion/valida_sesion.php";
if ( $_SESSION["tipo"] == "usuario"){
    $coin = array();
    //query para obtener todas las monedas de un usuario con el precio y la fecha de hoy
    $monedas = "SELECT precio_moneda.id_moneda, balance, sigla, valor, nombre FROM usuario_tiene_moneda  LEFT JOIN moneda ON id_moneda = id LEFT JOIN precio_moneda ON usuario_tiene_moneda.id_moneda = precio_moneda.id_moneda WHERE id_usuario = $1 AND precio_moneda.fecha = $2";
    $resultmoneda = pg_query_params($dbconn, $monedas, array($_SESSION["id_usuario"], date("Y-m-d")));
    if(pg_num_rows($resultmoneda) > 0 ) { 
        while($row = pg_fetch_assoc($resultmoneda)) {
            $valor = $row[3];
            $nombremoneda = $row[4];
            $cantidad = $row[1];
            $codigo = $row[2];
            $valortotal = $cantidad * $valor;

            $coin->append(array($codigo, $nombremoneda, $cantidad, $valor, $valortotal));
        }
    }
}
?>