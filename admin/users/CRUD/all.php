
<?php
    include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';
    $sql = "SELECT * FROM usuario";
    $result = pg_query_params($dbconn, $sql, array( ));
    $otro=pg_query($dbconn, $sql);
    
    function id($result,$dbconn){
    
        if( pg_num_rows($result) > 0 ) {
            while($row = pg_fetch_assoc($result)) {
                echo '<br>' .$row["id"]. '<br>';
            
            }
            
        }else {
            echo "Hubo un error al solicitar los datos";
            pg_close($dbconn);
            }
    }
    function name($result,$dbconn){
    
        if( pg_num_rows($result) > 0 ) {
            while($row = pg_fetch_assoc($result)) {
                echo '<br>' .$row["nombre"]. '<br>';
            
            }
            
        }else {
            echo "Hubo un error al solicitar los datos";
            pg_close($dbconn);
            }
    }
    function apellido($result,$dbconn){
    
        if( pg_num_rows($result) > 0 ) {
            while($row = pg_fetch_assoc($result)) {
                echo '<br>' .$row["apellido"]. '<br>';
            
            }
            
        }else {
            echo "Hubo un error al solicitar los datos";
            pg_close($dbconn);
            }
    }
    function correo($result,$dbconn){
    
        if( pg_num_rows($result) > 0 ) {
            while($row = pg_fetch_assoc($result)) {
                echo '<br>' .$row["correo"]. '<br>';
            
            }
            
        }else {
            echo "Hubo un error al solicitar los datos";
            pg_close($dbconn);
            }
    }
    


        

?>