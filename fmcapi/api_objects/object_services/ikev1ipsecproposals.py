from fmcapi.api_objects.classtemplates import APIClassTemplate
import logging


class IKEv1IpsecProposals(APIClassTemplate):
    """
    The IKEv1IpsecProposals Object in the FMC.
    """

    url_suffix = '/object/ikev1ipsecproposals'
    required_for_post = ['name', 'espEncryption', 'espHash']
    VALID_FOR_ENCRYPTION = ['DES', '3DES', 'AES-128', 'AES-192', 'AES-256', 'ESP-NULL']
    VALID_FOR_HASH = ['NONE', 'MD5', 'SHA']
    valid_characters_for_name = """[.\w\d_\- ]"""
    first_supported_fmc_version = '6.3'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IKEv1IpsecProposals class.")
        self.parse_kwargs(**kwargs)
        self.type = 'IKEv1IPsecProposal'

    def format_data(self):
        logging.debug("In format_data() for IKEv1IpsecProposals class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'espEncryption' in self.__dict__:
            json_data['espEncryption'] = self.espEncryption
        if 'espHash' in self.__dict__:
            json_data['espHash'] = self.espHash
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for IKEv1IpsecProposals class.")
        if 'espEncryption' in kwargs:
            self.espEncryption = kwargs['espEncryption']
        if 'espHash' in kwargs:
            self.espHash = kwargs['espHash']
