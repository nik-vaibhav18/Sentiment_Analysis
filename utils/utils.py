import json
import os
import re
import pandas


def createDirectoryforUser(userId,projectId):
    """
    Creates a directory for the user if it doesn't exist
    """
    path=os.path.join('ttrainingData/',userId)
    if not os.path.isdir(path):
        os.makedirs(path)
    path=os.path.join(path,projectId)
    if not os.path.isdir(path):
        os.makedirs(path)

    


