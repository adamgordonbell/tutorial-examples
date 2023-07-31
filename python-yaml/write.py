import yaml
import json 

data1 = {
    'Name':'John Doe',
    'Position':'DevOps Engineer',
    'Location':'England',
    'Age':'26',
    'Experience': {'GitHub':'Software Engineer',\
    'Google':'Technical Engineer', 'Linkedin':'Data Analyst'},
    'Languages': {'Markup':['HTML'], 'Programming'\
    :['Python', 'JavaScript','Golang']}
}

yaml_output = yaml.dump(data1, sort_keys=False) 

print(yaml_output)

with open('./output/data1.yaml','w') as file:
    file.write(yaml_output)

data2 = [
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

yaml_output2 = yaml.dump_all(data2, sort_keys=False) 

print(yaml_output2)

with open('./output/data2.yaml','w') as file:
    file.write(yaml_output2)

with open('./output/data1.yaml','r') as file:
    data3 = yaml.safe_load(file)

print(data3)
data3['Age'] = 99
data3['othername'] = "Tom Adams"

yaml_str = yaml.safe_dump(data3, sort_keys=False)

with open('./output/data3.yaml', 'w') as file:
    file.write(yaml_str)

with open('./output/data4.json','w') as file:
    json.dump(data3, file)
