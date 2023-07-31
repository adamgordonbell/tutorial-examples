import yaml
import json 
from typing import Any, List, Dict

data1 : dict[str,Any]= {
    'Name':'John Doe',
    'Position':'DevOps Engineer',
    'Location':'England',
    'Age':'26',
    'Experience': {'GitHub':'Software Engineer',\
    'Google':'Technical Engineer', 'Linkedin':'Data Analyst'},
    'Languages': {'Markup':['HTML'], 'Programming'\
    :['Python', 'JavaScript','Golang']}
}

print(data1)

data2 : List[Dict[str,Any]]= [
    {
    'apiVersion': 'v1',
    'kind':'persistentVolume',
    'metadata': {'name':'mongodb-pv', 'labels':{'type':'local'}},
    'spec':{'storageClassName':'hostpath'},
    'capacity':{'storage':'3Gi'},
    'accessModes':['ReadWriteOnce'],
    'hostpath':{'path':'/mnt/data'}
    },

    {
    'apiVersion': 'v1',
    'kind':'persistentVolume',
    'metadata': {'name':'mysql-pv', 'labels':{'type':'local'}},
    'spec':{'storageClassName':'hostpath'},
    'capacity':{'storage':'2Gi'},
    'accessModes':['ReadWriteOnce'],
    'hostpath':{'path':'/mnt/data'}
    }
]

print(data2)
