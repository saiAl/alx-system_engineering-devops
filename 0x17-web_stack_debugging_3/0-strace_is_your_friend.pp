# fix internal error

file {'create missing file':
  ensure => 'present',
  path   => '/var/www/html/index.html',
}
