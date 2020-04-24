<?php

$database = "users";
$user	  = "root";
$password = "secret";
$host	  = "mysql";

$db	 = mysql_connect("$host","$user","$password");

if(!$db){
	echo"Cannot  connect to the database server";
}else if($db && !(mysql_select_db($SQL_DBASE, $db))){
	echo "Sucessfully connected to the database server! Database Users Selected";
}

?>
