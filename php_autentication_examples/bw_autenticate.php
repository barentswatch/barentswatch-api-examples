$client_id = '';
$client_secret = '';
$redirect_uri= "http://localhost:8080/callback.php";
$url = 'https://www.barentswatch.no/api/token';
$data = array(
    'grant_type' => 'client_credentials'
    'client_id' => $client_id,
    'client_secret' => $client_secret,
    'redirect_uri' => $redirect_uri,
    
 );
$options = array(
    'http' => array(
        'header'  => "Content-type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data)
    )
);
$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);
var_dump($result);