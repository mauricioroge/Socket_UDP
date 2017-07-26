from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
# Criar servidor
with SimpleXMLRPCServer(("localhost", 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()



    # Todas os metodos da classe serao criados a partir do server register abaixo
    class MyFuncs:
        
        def mul(self, x, y):
            return x * y
    
        # Potenciacao
        def pot(self,x,y):
            return pow(x,y)
    
        # Soma
        def soma(self,x,y):
            return x + y
    
    server.register_instance(MyFuncs())

    # Server loop
    server.serve_forever()