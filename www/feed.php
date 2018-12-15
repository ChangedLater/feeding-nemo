<?php
error_reporting(E_ALL);
$msg = $_POST['submitted'];

echo "<br/>";

/* Create a TCP/IP socket. */
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === false) {
    echo "unable to feed";
}


$result = socket_connect($socket, "127.0.0.1", 8888);

socket_write($socket,$msg,strlen($msg));

if ($result === false) {
    echo "Failure to feed";
}
$out = '';

echo "Request to feed submitted</br>";
$out = socket_read($socket, 2048);

socket_close($socket);
?>
