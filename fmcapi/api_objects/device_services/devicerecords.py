from fmcapi.api_objects.classtemplates import APIClassTemplate
from fmcapi.api_objects.policy_services.accesspolicies import AccessPolicies
import time
import logging
import warnings


class DeviceRecords(APIClassTemplate):
    """
    The DeviceRecords Object in the FMC.
    """

    url_suffix = '/devices/devicerecords'
    required_for_post = ['accessPolicy', 'hostName', 'regKey']
    required_for_put = ['id']
    LICENSES = ['BASE', 'MALWARE', 'URLFilter', 'THREAT', 'VPN']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for DeviceRecords class.")
        self.parse_kwargs(**kwargs)

    def format_data(self):
        logging.debug("In format_data() for DeviceRecords class.")
        json_data = {}
        if 'id' in self.__dict__:
            json_data['id'] = self.id
        if 'name' in self.__dict__:
            json_data['name'] = self.name
        if 'hostName' in self.__dict__:
            json_data['hostName'] = self.hostName
        if 'natID' in self.__dict__:
            json_data['natID'] = self.natID
        if 'regKey' in self.__dict__:
            json_data['regKey'] = self.regKey
        if 'license_caps' in self.__dict__:
            json_data['license_caps'] = self.license_caps
        if 'accessPolicy' in self.__dict__:
            json_data['accessPolicy'] = self.accessPolicy
        return json_data

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for DeviceRecords class.")
        if 'hostName' in kwargs:
            self.hostName = kwargs['hostName']
        if 'natID' in kwargs:
            self.natID = kwargs['natID']
        if 'regKey' in kwargs:
            self.regKey = kwargs['regKey']
        if 'license_caps' in kwargs:
            self.license_caps = kwargs['license_caps']
        if 'accessPolicy' in kwargs:
            self.accessPolicy = kwargs['accessPolicy']
        if 'acp_name' in kwargs:
            self.acp(name=kwargs['acp_name'])
        if 'model' in kwargs:
            self.model = kwargs['model']
        if 'modelId' in kwargs:
            self.modelId = kwargs['modelId']
        if 'modelNumber' in kwargs:
            self.modelNumber = kwargs['modelNumber']
        if 'modelType' in kwargs:
            self.modelType = kwargs['modelType']
        if 'healthStatus' in kwargs:
            self.healthStatus = kwargs['healthStatus']
        if 'healthPolicy' in kwargs:
            self.healthPolicy = kwargs['healthPolicy']
        if 'keepLocalEvents' in kwargs:
            self.keepLocalEvents = kwargs['keepLocalEvents']
        if 'prohibitPacketTransfer' in kwargs:
            self.prohibitPacketTransfer = kwargs['prohibitPacketTransfer']

    def licensing(self, action, name='BASE'):
        logging.debug("In licensing() for DeviceRecords class.")
        if action == 'add':
            if name in self.LICENSES:
                if 'license_caps' in self.__dict__:
                    self.license_caps.append(name)
                    self.license_caps = list(set(self.license_caps))
                else:
                    self.license_caps = [name]
                logging.info(f'License "{name}" added to this DeviceRecords object.')

            else:
                logging.warning(f'{name} not found in {self.LICENSES}.  Cannot add license to DeviceRecords.')
        elif action == 'remove':
            if name in self.LICENSES:
                if 'license_caps' in self.__dict__:
                    try:
                        self.license_caps.remove(name)
                    except ValueError:
                        logging.warning(f'{name} is not assigned to this devicerecord thus cannot be removed.')
                    logging.info(f'License "{name}" removed from this DeviceRecords object.')
                else:
                    logging.warning(f'{name} is not assigned to this devicerecord thus cannot be removed.')

            else:
                logging.warning(f'{name} not found in {self.LICENSES}.  Cannot remove license from DeviceRecords.')
        elif action == 'clear':
            if 'license_caps' in self.__dict__:
                del self.license_caps
                logging.info('All licensing removed from this DeviceRecords object.')

    def acp(self, name=''):
        logging.debug("In acp() for Device class.")
        acp = AccessPolicies(fmc=self.fmc)
        acp.get(name=name)
        if 'id' in acp.__dict__:
            self.accessPolicy = {'id': acp.id, 'type': acp.type}
        else:
            logging.warning(f'Access Control Policy {name} not found.  Cannot set up accessPolicy for DeviceRecords.')

    def post(self, **kwargs):
        logging.debug("In post() for Device class.")
        response = super().post(**kwargs)
        if 'post_wait_time' in kwargs:
            self.post_wait_time = kwargs['post_wait_time']
        else:
            self.post_wait_time = 300
        logging.info(f'DeviceRecords registration task submitted.  '
                     f'Waiting {self.post_wait_time} seconds for it to complete.')
        time.sleep(self.post_wait_time)
        return response


class Device(DeviceRecords):
    """Dispose of this Class after 20210101."""

    def __init__(self, fmc, **kwargs):
        warnings.resetwarnings()
        warnings.warn("Deprecated: Device() should be called via DeviceRecords().")
        super().__init__(fmc, **kwargs)
