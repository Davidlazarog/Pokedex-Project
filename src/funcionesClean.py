import sys
import argparse
import json
import urllib
import requests
import pandas as pd
from pandas import json_normalize
import src.funcionesPrincipal as op

def cleaning(x):
    '''
    Con esta funcion, importamos el dataset y hacemos una pequeña limpieza
    '''
    import pandas as pd
    data = pd.read_csv(x, encoding = 'latin1')
    data['Type 2'] = data['Type 2'].fillna('No')
    return data