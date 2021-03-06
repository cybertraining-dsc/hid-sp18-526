from connexion.resolver import Resolver
import cmenv.constants as constants

class CMResolver(Resolver):
    """This resolver imports the original resolver and allows passing a dict of endpoints.
    
    *** taken from the original connexion resolver 
        @https://github.com/zalando/connexion/blob/master/connexion/resolver.py
    """

    def __init__(self, controller_dispatch = {}, collection_endpoint_name = 'search'):
        """
        Args:
            default_module_name
            collection_endpoint_name
        """
        
        Resolver.__init__(self)
        self.controller_dispatch = controller_dispatch
        self.collection_endpoint_name = collection_endpoint_name

    # unchanged
    def resolve_operation_id(self, operation):
        """
        Resolves the operationId using REST semantics unless explicitly configured in the spec
        :type operation: connexion.operation.Operation
        """
        if operation.operation.get('operationId'):
            return Resolver.resolve_operation_id(self, operation)

        return self.resolve_operation_with_dispatch(operation)

    def resolve_operation_with_dispatch(self, operation):
        """Returns endpoint based on parent/child dispatch
        
        <api root>.<api name>.controllers.<child name>.<method>
        ie. apis.services.controllers.list.get
        """
        
        path = operation.path.split('/')[1]
        endpoint = operation.method
        
        if endpoint == 'get' and '{' not in operation.path:
            endpoint = 'search'

        return '{}.{}.{}.{}.{}.{}'.format(
            'cmenv', 
            constants.API_ROOT,
            self.controller_dispatch[operation.path[1:]],
            'controllers',
            path,
            endpoint
        )
