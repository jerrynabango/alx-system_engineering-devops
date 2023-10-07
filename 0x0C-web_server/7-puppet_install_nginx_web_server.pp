# Install Nginx web server (w/ Puppet)

exec { 'apt-get update':
  command => '/usr/bin/apt-get -y update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update'],
}

file_line { 'redirect':
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'rewrite ^/redirect_me https://www.google.com permanent;',
  notify  => Service['nginx'],
  require => Package['nginx'],
}

file { 'index-html':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

service { 'nginx':
  ensure => running,
  enable => true,
}
