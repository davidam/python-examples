try:
     import xmlrpclib
except ImportError:
     import xmlrpc.client as xmlrpclib

client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
# get a list of package names
packages = client.list_packages()
print(packages)
