#!/usr/bin/env python

import yaml

def _yaml_to_csv(name=None, address=None):
    # CSV Headers
    #First Name,Last Name,Home Street,Home Street 2,Home City,Home State,Home Postal Code,Home Country,E-mail Address
    if 'email' in address:
        email = address['email']
    else:
        email = ''

    return(name + ',,' + address['street'] + ',,' + address['city'] + ',' + address['state'] + ',' + address['zip'] + ',' + email + ',')

def load_guest_list():
    with open("addresses.yaml", 'r') as stream:
        try:
            party = yaml.load(stream)
            return(party)
        except yaml.YAMLError as exc:
            print(exc)

def generate_labels(guest_list=None): 
    # Create CSV
    for name, address in guest_list.iteritems():
        print(_yaml_to_csv(name, address))

def main():
    party=load_guest_list()
    print("First Name,Last Name,Home Street,Home Street 2,Home City,Home State,Home Postal Code,Home Country,E-mail Address")
    generate_labels(party['guest_list']['family'])
    generate_labels(party['guest_list']['friends'])

if __name__ == "__main__":
    main()
