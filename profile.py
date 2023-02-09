import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

# Creating the mysql server
node1 = request.XenVM("mysql-server")
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node1.routable_control_ip = "true"

# Installs mysql
node1.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))
node1.addService(rspec.Execute(shell="/bin/sh", command="sudo apt install -y mysql-server "))
node1.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl enable mysql-server'))
node1.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl status mysql-server'))

# Configuring mysql-server
node1.addService(rspec.Execute(shell="/bin/sh", command='sudo mysql_secure_installation'))
node1.addService(rspec.Execute(shell="/bin/sh", command='2'))
node1.addService(rspec.Execute(shell="/bin/sh", command='dfA2%Vf!Z&U12mz3FlW!'))
node1.addService(rspec.Execute(shell="/bin/sh", command='dfA2%Vf!Z&U12mz3FlW!'))
node1.addService(rspec.Execute(shell="/bin/sh", command='y'))
node1.addService(rspec.Execute(shell="/bin/sh", command='y'))
node1.addService(rspec.Execute(shell="/bin/sh", command='y'))
node1.addService(rspec.Execute(shell="/bin/sh", command='y'))

# Changing root user password
node1.addService(rspec.Execute(shell="/bin/sh", command='sudo mysql'))
node1.addService(rspec.Execute(shell="/bin/sh", command="ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '&cFpmgffmF16jt!nhmQj';"))
node1.addService(rspec.Execute(shell="/bin/sh", command='FLUSH PRIVILEGES;'))
node1.addService(rspec.Execute(shell="/bin/sh", command='exit'))

# Creating a default user
node1.addService(rspec.Execute(shell="/bin/sh", command='sudo mysql -u root -p'))
node1.addService(rspec.Execute(shell="/bin/sh", command='&cFpmgffmF16jt!nhmQj'))
node1.addService(rspec.Execute(shell="/bin/sh", command="CREATE USER 'amosley'@'localhost' IDENTIFIED BY 'OQsl*Jcn^MLntHVFn3i2';"))
node1.addService(rspec.Execute(shell="/bin/sh", command="GRANT ALL PRIVILEGES ON *.* TO 'amosley'@'localhost' WITH GRANT OPTION;"))
node1.addService(rspec.Execute(shell="/bin/sh", command='exit'))

# Creating the nginx server
node2 = request.XenVM("nginx-server")
node2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node2.routable_control_ip = "true"

node2.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))
node2.addService(rspec.Execute(shell="/bin/sh", command="sudo apt install -y nginx"))
node2.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl status nginx'))

# Creating the dev server for frontend
node3 = request.XenVM("frontend-dev-server")
node3.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node3.routable_control_ip = "true"

node3.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))

# Creating links between the servers
link1 = request.Link(members = [node1,node2])
link2 = request.Link(members = [node1,node3])
link3 = request.Link(members = [node2,node3])


# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()

