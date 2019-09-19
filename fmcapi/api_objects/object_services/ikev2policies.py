from fmcapi.api_objects.classtemplates import APIClassTemplate
import logging


class IKEv2Policies(APIClassTemplate):
    """
    The IKEv2Policies Object in the FMC.
    """

    url_suffix = '/object/ikev2policies'
    required_for_post = ['name', 'integrityAlgorithms', 'prfIntegrityAlgorithms', 'encryptionAlgorithms',
                         'diffieHellmanGroups']
    VALID_FOR_ENCRYPTION = ['DES', '3DES', 'AES', 'AES-192', 'AES-256', 'NULL', 'AES-GCM', 'AES-GCM-192',
                            'AES-GCM-256']
    VALID_FOR_INTEGRITY = ['NULL', 'MD5', 'SHA', 'SHA-256', 'SHA-384', 'SHA-512']
    VALID_FOR_PRF_INTEGRITY = ['MD5', 'SHA', 'SHA-256', 'SHA-384', 'SHA-512']
    valid_characters_for_name = """[.\w\d_\- ]"""
    first_supported_fmc_version = '6.3'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for IKEv2Policies class.")
        self.parse_kwargs(**kwargs)
        self.type = 'Ikev2PolicyObject'

    def format_data(self):
        logging.debug("In format_data() for IKEv2Policies class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'type' in self.__dict__:
            json_data['type'] = self.type
        if 'priority' in self.__dict__:
            json_data['priority'] = self.priority
        if 'diffieHellmanGroups' in self.__dict__:
            json_data['diffieHellmanGroups'] = self.diffieHellmanGroups
        if 'integrityAlgorithms' in self.__dict__:
            json_data['integrityAlgorithms'] = self.integrityAlgorithms
        if 'prfIntegrityAlgorithms' in self.__dict__:
            json_data['prfIntegrityAlgorithms'] = self.prfIntegrityAlgorithms
        if 'encryptionAlgorithms' in self.__dict__:
            json_data['encryptionAlgorithms'] = self.encryptionAlgorithms
        if 'lifetimeInSeconds' in self.__dict__:
            json_data['lifetimeInSeconds'] = self.lifetimeInSeconds
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for IKEv2Policies class.")
        if 'priority' in kwargs:
            self.priority = kwargs['priority']
        if 'diffieHellmanGroups' in kwargs:
            self.diffieHellmanGroups = kwargs['diffieHellmanGroups']
        if 'integrityAlgorithms' in kwargs:
            self.integrityAlgorithms = kwargs['integrityAlgorithms']
        if 'prfIntegrityAlgorithms' in kwargs:
            self.prfIntegrityAlgorithms = kwargs['prfIntegrityAlgorithms']
        if 'encryptionAlgorithms' in kwargs:
            self.encryptionAlgorithms = kwargs['encryptionAlgorithms']
        if 'lifetimeInSeconds' in kwargs:
            self.lifetimeInSeconds = kwargs['lifetimeInSeconds']

    def encryption(self, action, algorithms=[]):
        logging.debug("In encryption() for IKEv2Policies class.")
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
                logging.warning('IKEv2Policies has no members.  Cannot remove encryptionAlgorithms.')
        elif action == 'clear':
            if 'encryptionAlgorithms' in self.__dict__:
                del self.encryptionAlgorithms
                logging.info('All encryptionAlgorithms removed from this IKEv2Policies object.')

    def hash(self, action, algorithms=[]):
        logging.debug("In hash() for IKEv2Policies class.")
        if action == 'add':
            for algorithm in algorithms:
                if 'integrityAlgorithms' in self.__dict__:
                    if algorithm in self.integrityAlgorithms:
                        logging.warning(f'integrityAlgorithms "{algorithm}" already exists.')
                    elif algorithm in self.VALID_FOR_INTEGRITY:
                        self.integrityAlgorithms.append(algorithm)
                    else:
                        logging.warning(f'integrityAlgorithms "{algorithm}" not a valid type.')
                else:
                    if algorithm in self.VALID_FOR_INTEGRITY:
                        self.integrityAlgorithms = [algorithm]
                    else:
                        logging.warning(f'integrityAlgorithms "{algorithm}" not a valid type.')
        elif action == 'remove':
            if 'integrityAlgorithms' in self.__dict__:
                for algorithm in algorithms:
                    self.integrityAlgorithms = list(filter(lambda i: i != algorithm, self.integrityAlgorithms))
            else:
                logging.warning('IKEv2Policies has no members.  Cannot remove integrityAlgorithms.')
        elif action == 'clear':
            if 'integrityAlgorithms' in self.__dict__:
                del self.integrityAlgorithms
                logging.info('All integrityAlgorithms removed from this IKEv2Policies object.')

    def prf_hash(self, action, algorithms=[]):
        logging.debug("In prf_hash() for IKEv2Policies class.")
        if action == 'add':
            for algorithm in algorithms:
                if 'prfIntegrityAlgorithms' in self.__dict__:
                    if algorithm in self.prfIntegrityAlgorithms:
                        logging.warning(f'prfIntegrityAlgorithms "{algorithm}" already exists.')
                    elif algorithm in self.VALID_FOR_PRF_INTEGRITY:
                        self.prfIntegrityAlgorithms.append(algorithm)
                    else:
                        logging.warning(f'prfIntegrityAlgorithms "{algorithm}" not a valid type.')
                else:
                    if algorithm in self.VALID_FOR_PRF_INTEGRITY:
                        self.prfIntegrityAlgorithms = [algorithm]
                    else:
                        logging.warning(f'prfIntegrityAlgorithms "{algorithm}" not a valid type.')
        elif action == 'remove':
            if 'prfIntegrityAlgorithms' in self.__dict__:
                for algorithm in algorithms:
                    self.prfIntegrityAlgorithms = list(filter(lambda i: i != algorithm, self.prfIntegrityAlgorithms))
            else:
                logging.warning('IKEv2Policies has no members.  Cannot remove prfIntegrityAlgorithms.')
        elif action == 'clear':
            if 'prfIntegrityAlgorithms' in self.__dict__:
                del self.prfIntegrityAlgorithms
                logging.info('All prfIntegrityAlgorithms removed from this IKEv2Policies object.')