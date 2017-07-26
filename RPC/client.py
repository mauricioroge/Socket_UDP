import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.pot(2,3))  # Returns 2**3 = 8
print(s.soma(2,3))  # Returns 5
print(s.mul(5,2))  # Returns 5*2 = 10

# Print list of available methods
print(s.system.listMethods())