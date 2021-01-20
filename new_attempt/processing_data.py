import os, sys
import pandas as pd
import json



class Data_Manager:
    def __init__(self, data_location, columns_keep_data_location):

        data_loaded = self._loading_data(data_location)
        self.columns_to_keep = self._loading_options(columns_keep_data_location)
        self.raw_data = data_loaded.loc[:, self.columns_to_keep]


    def _loading_data(self, data_location):
        data_loaded = pd.read_csv(data_location, compression = 'gzip')
        return data_loaded

    def _loading_options(self, file_location):
        with open(str(file_location), 'r') as f:
            return json.load(f)

    def _property_type_function(x, property_type_options_file):
        options_list = self._loading_options(property_type_options_file)
        if x in options_list:
            x = options_list[x]
        if "Entire" in x:
            return 1
        elif "Private" in x:
            return 2
        elif "Shared" in x:
            return 3
        else:
            raise ValueError

    def recoding_property_type(property_type_options_file):
        self.raw_data['property_type'] = self.raw_data['property_type'].apply(lambda x: self._property_type_function(x, property_type_options_file))


import code
code.interact(local=locals())
