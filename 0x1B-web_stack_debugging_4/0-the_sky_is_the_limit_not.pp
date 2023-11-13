# Testing our web server setup ft Nginx performance under pressure
exec { 'ulimit':
  command => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 500\"/' /etc/default/nginx",
  path    => '/usr/bin:/usr/sbin:/bin',
  notify  => Service['nginx']
}

# Ensures Nginx is runnign and set to start at boot
service { 'nginx':
  ensure => running,
  enable => true,
}
