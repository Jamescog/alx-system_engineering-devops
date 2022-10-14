# create a file in /tmp

file {'school':
    content  => 'I love Puppet',
    mode     => '0744',
    group    => 'www-data',
    owner    => 'www-data',
    path     => '/tmp/school',
    }
