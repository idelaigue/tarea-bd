<?php 
include '../Curl.php';

$get_data = callAPI('GET', 'http://127.0.0.1:5000/api/v1/moneda', false);
$response = json_decode($get_data,true);
print_r ($response);

foreach ($response as $clave=>$product) {
    
    
    foreach($product as $matriz){
        
        print_r($matriz["nombre"] );
        print_r($matriz["sigla"] );
        
    }
    
}
#$errors = $response['response']['errors'];
#$data = $response['response']['data'][0];

?>