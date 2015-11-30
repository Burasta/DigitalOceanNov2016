 <?php
$dbHost = 'localhost'; // usually localhost
$dbUsername = 'root';
$dbPassword = 'root';
$dbDatabase = 'egglabs';
$db = mysql_connect($dbHost, $dbUsername, $dbPassword) or die ("Unable to connect to Database Server.");
mysql_select_db ($dbDatabase, $db) or die ("Could not select database.");

$sql_check = mysql_query("SELECT * FROM messages order by msg_id desc");


if(isSet($_POST['content']))

{
$content=$_POST['content'];

mysql_query("insert into messages(msg) values ('$content')");

$sql_in= mysql_query("SELECT msg,msg_id FROM messages order by msg_id desc");
$r=mysql_fetch_array($sql_in);


}


?>

<table cellpadding="0" cellspacing="0" width="500px">

<tr class="comment">
<td style="padding:14px;" class="comment_box" align="left"><b><?php echo $r['msg']; ?></b></td>
</tr>

</table>