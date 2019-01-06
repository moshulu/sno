<?php
echo '<a href = "first.php?rainbow">click here for rainbow</a>';
echo '<a href = "first.php?broadway">click here for broadway</a>';
echo '<a href = "first.php?poweroff">click here for power off</a>';

if(isset($_GET["rainbow"])){
	exec("sudo killall python3");
	shell_exec("cd /var/www/html/scripts && sudo python3 rainbow.py 2>&1");

}
if(isset($_GET["broadway"])){
	exec("sudo killall python3");
	shell_exec("cd /var/www/html/scripts && sudo python3 broadway.py 2>&1");

}
if(isset($_GET["poweroff"])){
	exec("sudo killall python3");
	shell_exec("cd /var/www/html/scripts && sudo python3 poweroff.py 2>&1");
}

?>
