import json

class ReadParams(object):
    def __init__(self):
        self.json_file = 'parameters/params.json'

    def reader(self):
        dict_params = {}
        with open(self.json_file, 'r') as file:
            distros_dict = json.load(file)

            driver = str(distros_dict['driver'])
            url = str(distros_dict['url'])

            username = str(distros_dict['username'])
            password = str(distros_dict['password'])
            product_choiced = str(distros_dict['product_choiced'])

            firstname = str(distros_dict['firstname'])
            lastname = str(distros_dict['lastname'])
            zipcode = str(distros_dict['zipcode'])

            dict_params = {'driver': driver, 'url': url, 'username': username,
                           'password': password, 'product_choiced': product_choiced,
                           'firstname': firstname, "lastname": lastname, "zipcode": zipcode}


        return dict_params
