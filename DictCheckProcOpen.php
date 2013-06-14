#!/usr/bin/php
<?php

//sample array
$my_array = array("fights", "foot", "people", "notaword");

//it seems to be easier to concatenate the array into a string to pass it to the command
foreach($my_array as $value)
	$v = $v . " " . $value;
	
$descriptorspec = array(
		0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
		1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
		2 => array("pipe", "a") // appends errors to this pipe. Unused.
);
	

// the path of the python file and the string
// currently works for DictCheck.py and DictStem.py
$command = "python /Users/etaiklein/Documents/workspace/plugins/metadatagames/www/protected/modules/plugins/modules/dictionary/components/DictCheck.py $v 2>&1";

//opens the connection between the python and php files
$process = proc_open($command, $descriptorspec, $pipes);

//fwrite passes the array to python. It is null because we dont want to set a limit on the amount of information passed.
$p = null;
fwrite($pipes[0], $p);

//this reads all the lines in the file but returns only the last output.
do 	{$last_line = $line; 
	$line = fgets($pipes[1]);
}
while ($line != "" );

//Turns the string output into an array.
$new_array = explode(",",subStr($last_line, 0, -1));

//closing the pipes stops data leaks
fclose($pipes[1]);
fclose($pipes[0]);
fclose($pipes[2]);
proc_close($process);

//prints the arrays so they're visible
echo var_dump($my_array);
echo var_dump($new_array);

//DICTCHECK OUTPUT:
// array(4) {
//   [0]=>
//   string(6) "fights"
//   [1]=>
//   string(4) "feet"
//   [2]=>
//   string(6) "people"
//   [3]=>
//   string(8) "notaword"
// }
// array(4) {
//   [0]=>
//   string(4) "True"
//   [1]=>
//   string(4) "True"
//   [2]=>
//   string(4) "True"
//   [3]=>
//   string(5) "False"
// }

// DICTSTEM OUTPUT:
// array(4) {
// 	[0]=>
// 	string(6) "fights"
// 	[1]=>
// 	string(4) "feet"
// 	[2]=>
// 	string(6) "people"
// 	[3]=>
// 	string(8) "notaword"
// }
// array(4) {
// 	[0]=>
// 	string(5) "fight"
// 	[1]=>
// 	string(4) "foot"
// 	[2]=>
// 	string(6) "people"
// 	[3]=>
// 	string(8) "notaword"
// }


?>
