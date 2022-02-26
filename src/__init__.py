from .MacroPush import MacroPush


def create_instance(c_instance):
    ''' Creates and returns Remote Script instance '''
    return MacroPush(c_instance)
