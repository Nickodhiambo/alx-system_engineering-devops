# Enables NGINX to handle more incoming traffic

# Increase user limit in the default file
exec { 'add-user-limit':
  command => 'sed -i "s/15/6000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

#Restart Nginx

exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
