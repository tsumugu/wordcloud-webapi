<?php
$words = urldecode($_GET["words"]);
$uid_get = basename(urldecode($_GET["uid"]));
$uid = empty($uid_get)?"?uid?":$uid_get;
$command = "sudo /usr/bin/python3.6 /var/www/html/wordcloud/simple.py '".$words."' '".$uid."' 2>&1";
$exec_res = exec($command, $error);
if (strpos($exec_res, "/var/www/html/wordcloud/imgs/") === false) {
  header("HTTP", true, 400);
  echo "400 Bad Request";
} else {
  header("Content-Type: image/jpg");
  echo file_get_contents($exec_res);
}
