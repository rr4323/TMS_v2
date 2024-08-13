import logging
import re

class SecretFilter(logging.Filter):
    def filter(self, record):
        '''
         - hide secret or password in the log message
         - regular expression will work for message having password and secret
        '''
        re.sub(r'password.*\s', '*****',record.msg)
        re.sub(r'secret.*\s', '*****',record.msg)
        return True
