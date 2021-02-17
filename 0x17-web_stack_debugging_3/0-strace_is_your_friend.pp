# Modify a line with extension phpp in a file
exec { 'eldanie':
    command => 'sudo sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
    path    => ['/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin'],
}
