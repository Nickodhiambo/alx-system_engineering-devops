# Adds custom header to web server response

# update package manager
exec { 'apt-update':
  command ==> '/usr/bin/apt-get -y update',
  path    ==> ['/usr/bin/', '/bin'],
}

# Check and install nginx
package { 'nginx':
  ensure ==> installed,
}

# Create a basic html file
file { '/var/www/html/index.html':
  content ==> 'Hello world!',
}

# Configure nginx with custom http response header
file_line { 'add custom header':
  ensure ==> present,
  path   ==> '/etc/nginx/sites-available/default',
  line   ==> "\tadd_header X-Served-By ${hostname};",
  after  ==> 'server_name _;',
}

# Restart web server
service { 'nginx':
  ensure ==> running,
}
