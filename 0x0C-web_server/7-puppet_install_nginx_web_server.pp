# Install Nginx web server (w/ Puppet)
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update'],
}

file { 'index-html':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
