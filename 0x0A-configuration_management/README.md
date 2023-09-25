# Puppet is a popular open-source configuration management and automation tool used for managing the configuration of computer systems and automating tasks within an IT infrastructure. Puppet is designed to simplify the process of configuring and maintaining servers, making it easier to manage large-scale and complex environments.

# Declarative language is a programming or configuration language that focuses on describing what should be accomplished, rather than specifying how to achieve it. In a declarative language, you express the desired outcome or state, and the system or program is responsible for determining the steps needed to reach that state. This is in contrast to imperative languages, where you explicitly specify the sequence of actions to achieve a result.

* An example:
file { '/tmp/school':
path => '/tmp/school',
mode => '0744',
owner => 'www-data',
group => 'www-data',
contents => 'I love Puppet'
}
