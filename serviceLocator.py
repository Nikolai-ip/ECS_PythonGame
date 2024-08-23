
class ServiceLocator:

    servicesMap = {}
       
    @staticmethod
    def register(service, name):
        ServiceLocator.servicesMap[name] = service
        
    @staticmethod
    def get(serviceName):
        return ServiceLocator.servicesMap[serviceName] 