# change setting

exec {'change os configuration':
  command => 'sed -i "/holberton hard/s/5/1000/" /etc/security/limits.conf && \
  sed -i "/holberton soft/s/4/1000/" /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
