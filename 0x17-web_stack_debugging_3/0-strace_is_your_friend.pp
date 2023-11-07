# Finds why Apache is returning a  500 error. 

exec { 'find-issue':
  command => 'cp /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  path    => ['/bin/:/usr/bin/:/usr/local/bin/:/usr/sbin/']
}
