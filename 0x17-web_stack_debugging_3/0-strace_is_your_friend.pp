# Using strace for find out why Apache is returning a 500 error

exec { 'Edit':
   command => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
