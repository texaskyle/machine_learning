<?php
require 'vendor/autoload.php';

use AfricasTalking\SDK\AfricasTalking;

// Set your app credentials
$username   = "evans3345";
$apiKey     = "f1fb7660d9ffcee4ac4c12d34c5e615ad29d9b2eba911ac4e6ee42487273f32a";

// Initialize the SDK
$AT         = new AfricasTalking($username, $apiKey);

// Get the SMS service
$sms        = $AT->sms();

// Set the numbers you want to send to in international format
$recipients = "+254711XXXYYY,+254733YYYZZZ";

// Set your message
$message    = "I'm a lumberjack and its ok, I sleep all night and I work all day";

// Set your shortCode or senderId
$from       = "myShortCode or mySenderId";

try {
    // Thats it, hit send and we'll take care of the rest
    $result = $sms->send([
        'to'      => $recipients,
        'message' => $message,
        'from'    => $from
    ]);

    print_r($result);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
