file { '/tmp/school':
path => '/tmp/school',
mode => '0744',
owner => 'www-data',
group => 'www-data',
contents => 'I love Puppet'
}
