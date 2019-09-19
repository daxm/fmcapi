from fmcapi.api_objects.classtemplates import APIClassTemplate
import logging


class ExtendedAccessList(APIClassTemplate):
    """
    The ExtendedAccessList Object in the FMC.
    """

    url_suffix = '/object/extendedaccesslist'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ExtendedAccessList class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for ExtendedAccessList class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ExtendedAccessList class.")

    def post(self):
        logging.info('POST method for API for ExtendedAccessList not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for ExtendedAccessList not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for ExtendedAccessList not supported.')
        pass