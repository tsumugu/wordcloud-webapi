<?php
$words = urldecode($_GET["words"]);
$command = "sudo /usr/bin/python3.6 /var/www/html/wordcloud/simple.py '".$words."' 2>&1";
exec($command, $errors);
if (count($errors) > 0) {
  // Error occured: return HTTP Status Code 400(Bad Request)
  header('HTTP', true, 400);
  echo "400 Bad Request";
} else {
  // Succeed: return JPEG binary
  header('Content-Type: image/jpg');
  echo file_get_contents("./test.jpg");
}
