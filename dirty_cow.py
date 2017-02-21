from __future__ import print_function
import requests
import json

nodes = []

def get_fact(certname, fact):
    url = "http://localhost:8080/pdb/query/v4/nodes/{}/facts/{}".format(certname, fact)
    r = requests.get(url)
    response = json.loads(r.text)
    for i in response:
        result = i['value']
        return result

def get_nodes():
    url = "http://localhost:8080/pdb/query/v4/nodes"
    r = requests.get(url)
    response = json.loads(r.text)
    for i in response:
        if not i['deactivated'] and not i['expired']:
            nodes.append(i['certname'])

def print_report(node, operatingsystem, operatingsystemrelease, kernelversion):
    print(node, end='')
    print("," + operatingsystem, end='')
    print("," + operatingsystemrelease, end='')
    print("," + kernelversion)

def main():
    get_nodes()
    print("node,operatingsystem,operatingsystemrelease,kernelversion")
    for node in nodes:
        operatingsystem = get_fact(node, 'operatingsystem')
        operatingsystemrelease = get_fact(node, 'operatingsystemrelease')
        kernelversion = get_fact(node, 'kernelversion')
        print_report(node, operatingsystem, operatingsystemrelease, kernelversion)

main()
