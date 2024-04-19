# install package flask

package { 'install flask':
  ensure   => 'installed',
  name     => 'flask==2.1.0',
  provider => 'pip3',
}

package { 'install werkzeug':
  ensure   => 'installed',
  name     => 'Werkzeug==2.1.1',
  provider => 'pip3',
}
