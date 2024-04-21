# configuration of ssh

file { 'disable password':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no'
}

file { 'identity file':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school'
}
