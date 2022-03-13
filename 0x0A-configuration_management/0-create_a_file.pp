# Creates a file in /tmp

file { 'school':
  ensure => present,
  content => 'I love puppet',
  group => 'www-data',
  mode => '0744',
  owner => 'www-data',
  path => '/tmp/school',
}
