# change the limit of requests

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/5000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
