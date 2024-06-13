# decrease the pressure on the nginx server.

exec {'fix nginx':
  command => 'sed -i "s/15/4000/" /etc/default/nginx && service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
