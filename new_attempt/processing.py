import os, sys
import pandas as pd
import json



class Data_Manager:
    def __init__(self, data_location, columns_keep_data_location):
    #def __init__(self):
    #    pass
    #    self.data_location = data_definition_file
    #    self.columns_to_keep = data_types
        #data_loaded = pd.read_csv(data_location, compression = 'gzip')

        data_loaded = self._loading_data(data_location)
        self.columns_to_keep = self._loading_options(columns_keep_data_location)
        self.raw_data = data_loaded.loc[:, self.columns_to_keep]


    def _loading_data(self, data_location):
        data_loaded = pd.read_csv(data_location, compression = 'gzip')
        return data_loaded

    def _loading_options(self, columns_keep_data_location):
        with open(str(columns_keep_data_location), 'r') as f:
            return json.load(f)


f = '../../data/20200908/listings.csv.gz'
collistlocation = 'columns_keep.json'
dm = Data_Manager(f, collistlocation)

import code
code.interact(local=locals())
