# Creates a file in the temp directory with 744 permissions

file {'/tmp/school':
ensure  => 'present',
mode    => '0744',
content => 'I love Puppet',
owner   => 'www-data',
group   => 'www-data',
}
