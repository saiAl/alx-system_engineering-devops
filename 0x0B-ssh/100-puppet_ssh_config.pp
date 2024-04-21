# configuration of ssh

$content = "
PasswordAuthentication no
IdentityFile ~/.ssh/school
"

file { 'modify conf file':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  content => $content
}
