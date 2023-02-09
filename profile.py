import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
# Create a XenVM
node1 = request.XenVM("node")
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node1.routable_control_ip = "true"

node1.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))
node1.addService(rspec.Execute(shell="/bin/sh", command="sudo apt install -y mysql-server "))
node1.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl status mysql-server'))

# Creating another node
node2 = request.XenVM("node")
node2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node2.routable_control_ip = "true"

node2.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))
node2.addService(rspec.Execute(shell="/bin/sh", command="sudo apt install -y nginx"))
node2.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl status nginx'))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()

