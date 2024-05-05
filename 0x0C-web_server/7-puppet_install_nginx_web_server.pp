# install and configure Ngix
class nginx {

  include puppet::nginx

  package { 'nginx': ensure => present }

  nginx::vhost { 'default':
    ensure => present,
    port => 80,
    server_name => ['localhost'],
    www_root => '/var/www/html',
    content => <<EOF
    server {
        listen 80;
        server_name localhost;

        location / {
          root /var/www/html;
          index index.html index.htm;
          try_files $uri $uri/ /index.html;
        }

        location /redirect_me {
          return 301 $scheme://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
    }
EOF
  }

  service { 'nginx':
    ensure => running,
    enabled => true,
  }
}
