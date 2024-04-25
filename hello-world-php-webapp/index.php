<?php

$serviceUrl = getenv('SVC_URL');
$consumerKey = getenv('CONSUMER_KEY');
$consumerSecret = getenv('CONSUMER_SECRET');
$tokenUrl = getenv('TOKEN_URL');

// Display the environment variable values
echo '<h2>Environment Variables</h2>';
echo '<p>Service URL: ' . htmlspecialchars($serviceUrl) . '</p>';
echo '<p>Consumer Key: ' . htmlspecialchars($consumerKey) . '</p>';
echo '<p>Consumer Secret: ' . htmlspecialchars($consumerSecret) . '</p>';
echo '<p>Token URL: ' . htmlspecialchars($tokenUrl) . '</p>';



echo 'hello world!';
?>
