from fmcapi.api_objects.classtemplates import APIClassTemplate
import logging


class IKEv2IpsecProposals(APIClassTemplate):
    """
    The IKEv2IpsecProposals Object in the FMC.
    """

    url_suffix = '/object/ikev2ipsecproposals'
    required_for_post = ['name', 'encryptionAlgorithms', 'integrityAlgorithms']
    VALID_FOR_ENCRYPTION = ['DES', '3DES', 'AES', 'AES-192', 'AES-256', 'NULL', 'AES-GCM', 'AES-GCM-192',
                            'AES-GCM-256', 'AES-GMAC', 'AES-GMAC-192', 'AES-GMAC-256']
    VALID_FOR_HASH = ['NULL', 'MD5', 'SHA-1', 'SHA-256', 'SHA-384', 'SHA-512']
    valid_characters_for_name = """[.\w\d_\- ]"""
    first_supported_fmc_version = '6.3'


    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IKEv2IpsecProposals class.")
        self.parse_kwargs(**kwargs)
        self.type = 'IKEv2IPsecProposal'

    def format_data(self):
        logging.debug("In format_data() for IKEv2IpsecProposals class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'encryptionAlgorithms' in self.__dict__:
            json_data['encryptionAlgorithms'] = self.encryptionAlgorithms
        if 'integrityAlgorithms' in self.__dict__:
            json_data['integrityAlgorithms'] = self.integrityAlgorithms
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for IKEv2IpsecProposals class.")
        if 'encryptionAlgorithms' in kwargs:
            self.encryptionAlgorithms = kwargs['encryptionAlgorithms']
        if 'integrityAlgorithms' in kwargs:
            self.integrityAlgorithms = kwargs['integrityAlgorithms']

    def encryption(self, action, algorithms=[]):
        logging.debug("In encryption() for IKEv2IpsecProposals class.")
        if action == 'add':
            for algorithm in algorithms:
                if 'encryptionAlgorithms' in self.__dict__:
                    if algorithm in self.encryptionAlgorithms:
                        logging.warning(f'encryptionAlgorithms "{algorithm}" already exists.')
                    elif algorithm in self.VALID_FOR_ENCRYPTION:
                        self.encryptionAlgorithms.append(algorithm)
                    else:
                        logging.warning(f'encryptionAlgorithms "{algorithm}" not a valid type.')
                else:
                    self.encryptionAlgorithms = [algorithm]
        elif action == 'remove':
            if 'encryptionAlgorithms' in self.__dict__:
                for algorithm in algorithms:
                    self.encryptionAlgorithms = list(filter(lambda i: i != algorithm, self.encryptionAlgorithms))
            else:
                logging.warning('IKEv2IpsecProposals has no members.  Cannot remove encryptionAlgorithms.')
        elif action == 'clear':
            if 'encryptionAlgorithms' in self.__dict__:
                del self.encryptionAlgorithms
                logging.info('All encryptionAlgorithms removed from this IKEv2IpsecProposals object.')

    def hash(self, action, algorithms=[]):
        logging.debug("In hash() for IKEv2IpsecProposals class.")
        if action == 'add':
            for algorithm in algorithms:
                if 'integrityAlgorithms' in self.__dict__:
                    if algorithm in self.integrityAlgorithms:
                        logging.warning(f'integrityAlgorithms "{algorithm}" already exists.')
                    elif algorithm in self.VALID_FOR_HASH:
                        self.integrityAlgorithms.append(algorithm)
                    else:
                        logging.warning(f'integrityAlgorithms "{algorithm}" not a valid type.')
                else:
                    self.integrityAlgorithms = [algorithm]
        elif action == 'remove':
            if 'integrityAlgorithms' in self.__dict__:
                for algorithm in algorithms:
                    self.integrityAlgorithms = list(filter(lambda i: i != algorithm, self.integrityAlgorithms))
            else:
                logging.warning('IKEv2IpsecProposals has no members.  Cannot remove integrityAlgorithms.')
        elif action == 'clear':
            if 'integrityAlgorithms' in self.__dict__:
                del self.integrityAlgorithms
                logging.info('All integrityAlgorithms removed from this IKEv2IpsecProposals object.')