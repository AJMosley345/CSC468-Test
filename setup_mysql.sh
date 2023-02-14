MYSQL_ROOT_PASSWORD="test@123"
set timeout 10
spawn mysql_secure_installation

expect "Change the password for root ?\(Press y\|Y for Yes, any other key for No\) :"
send "y/r"

expect "New password:"
send "$MYSQL_ROOT_PASSWORD"

expect "Re-enter new password:"
send "$MYSQL_ROOT_PASSWORD"

expect "Do you wish to continue with the password provided?\(Press y\|Y for Yes, any other key for No\) :"
send "y/r"

expect "Remove anonymous users?\(Press y\|Y for Yes, any other key for No\) :"
send "y/r"

expect "Disallow root login remotely?\(Press y\|Y for Yes, any other key for No\) :"
send "y/r"

expect "Remove test database and access to it?\(Press y\|Y for Yes, any other key for No\) :"
send "y/r"

expect "Reload privilege tables now?\(Press y\|Y for Yes, any other key for No\) :"
send "y/r"
