<?php 
include '../Curl.php';

$get_data = callAPI('GET', 'http://127.0.0.1:5000/api/v1/cuenta_bancaria', false);
$response = json_decode($get_data,true);
print_r ($response);

foreach ($response as $clave=>$product) {
    
    
    foreach($product as $matriz){
        
        print_r($matriz["id_usuario"] );
        print_r($matriz["balance"] );
        
    }
    
}
#$errors = $response['response']['errors'];
#$data = $response['response']['data'][0];

?>