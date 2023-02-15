import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

# Creating the mongodb docker container
mongo_db = request.DockerContainer("mongo_db")
mongo_db.docker_dockerfile = "https://github.com/AJMosley345/CSC468-Test/mongo_db/Dockerfile"

# Creating the nginx docker container
web_server = request.DockerContainer("web_server")
web_server.docker_dockerfile = "https://github.com/AJMosley345/CSC468-Test/nginx/Dockerfile"

# Creating a LAN to put the containers into
lan = request.LAN("docker_lan")
mongodb_iface = mongo_db.addInterface("if1")
nginx_iface = web_server.addInterface("if1")
lan.addInterface(mongodb_iface)
lan.addInterface(nginx_iface)

portal.context.printRequestRSpec()