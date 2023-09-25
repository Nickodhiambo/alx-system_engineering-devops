#Modifies ssh config file

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}

file_line {' Turn off password auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
