import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()


#region
# Creating the mysql server
node1 = request.XenVM("mysql-server")
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node1.routable_control_ip = "true"

# # Installs mysql
node1.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))
node1.addService(rspec.Execute(shell="/bin/sh", command="sudo apt install -y sudo apt install -y software-properties-common gnupg apt-transport-https ca-certificates mongodb"))
node1.addService(rspec.Execute(shell="/bin/sh", command='wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -'))
node1.addService(rspec.Execute(shell="/bin/sh", command='echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list'))
node1.addService(rspec.Execute(shell="/bin/sh", command='sudo apt update'))
node1.addService(rspec.Execute(shell="/bin/sh", command='sudo apt install -y mongodb-org'))
node1.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl start mongod'))
node1.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl status mongod'))


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
#endregion