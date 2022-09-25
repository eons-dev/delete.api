import os
import logging
import apie

class delete(external):
    def __init__(this, name="delete"):
        super().__init__(name)

        this.supportedMethods = ['DELETE']

        #this.allowedNext = ['help'] only

        this.helpText = '''\
Delete any resource by offloading the actual work to another API.
This does not (currently) have access to the local filesystem (e.g. in case you wanted to delete an uploaded file).

Per the parent 'external':
'''
        this.helpText += super().helpText



    def Call(this):
        # This is a very simple wrapper at the moment.
        pass