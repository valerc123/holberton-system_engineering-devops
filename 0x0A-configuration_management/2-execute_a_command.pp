# Kill process named killmenow

exec { 'kill_process':
command  => 'pkill -f killmenow',
provider => 'shell',
}

