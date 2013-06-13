#!/usr/bin/php
<?php

//sample array
$my_array = array("Dog", "Cat", "Horse");
$v = "";

//it seems to be easier to concatenate the array into a string to pass it to the command
foreach($my_array as $value)
  $v = $v . " " . $value;
	echo $v;

# the path of the python file and the string
$command = "python /Users/etaiklein/Documents/workspace/plugins/metadatagames/www/protected/modules/plugins/modules/dictionary/components/DictCheck.py $v 2>&1";

#standard fare for popopen	
$pid = popen( $command,"r");

while( !feof( $pid ) )
{
	echo fread($pid, 256);
	flush();
	ob_flush();
	usleep(100000);
}
pclose($pid);
?>
