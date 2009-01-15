# coding: UTF-8
#
# Config Management Utility
#

import simplejson as json

# Better to use json module in python 2.6 here
# Tuples probably need to be converted to arrays here

class Config(object):
    """Program configuration object"""
    # The first time this object is instantiated, config is populated
    config = {}
    # All config values must exist in defaults, or they are ignored on loading config files
    # and won't be settable/readable by the program
    defaults = {
        "debug_on": True,
        "TRANSPARENT": [231,255,255],
        "default_paksize": "64",
##        "PROJECT_FILE_EXTENSION": ".tcp",
        "valid_image_extensions": [".png"],
        "OFFSET_NEGATIVE_ALLOWED": False,
        "window_size": [800,500],
        "window_position": [100,50],

        "negative_offset_allowed": False,
        "default_image_path": "test.png",


        "choicelist_paksize": [16,32,48,64,80,96,112,128,144,160,176,192,208,224,240],
        "choicelist_views": [1,2,4],
        "choicelist_dims": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
        "choicelist_dims_z": [1,2,3,4],
        }
    conf_path = "tc.config"

    def __init__(self):
        """"""
        # First time Config is intialised call the read_in function to init all the settings
        # from file. Subsequent instances of Config all refer to the same in-memory copy of
        # the settings, can add a setting by name, set a setting's value, remove a setting
        # re-read settings from file etc.
        if Config.config == {}:
            f = open(self.conf_path, "r")
            file_config = json.loads(f.read())
            f.close()
            # Now merge this into the defaults, value from default is always overrided if there
            # is a value in the file, also means only keys with a default set are loaded in
            for k in Config.defaults.keys():
                if file_config.has_key(k):
                    Config.config[k] = file_config.pop(k)
                else:
                    Config.config[k] = Config.defaults[k]
            print Config.config
    def __getattr__(self, name):
        """Lookup method by . access e.g. z = x.y"""
        if Config.config.has_key(name):
            return Config.config[name]
        else:
            raise AttributeError(name)
    def __setattr__(self, name, value):
        """Set method by . access e.g. x.y = z"""
        if name in Config.defaults:
            Config.config[name] = value
            self.save()
        else:
            object.__setattr__(self, name, value)
    def __getitem__(self, key):
        """Lookup method by dict access e.g. z = x["y"]"""
        if Config.config.has_key(key):
            return Config.config[key]
        else:
            raise KeyError(key)
    def __setitem__(self, key, value):
        """Set method by dict access e.g. x["y"] = z"""
        if Config.defaults.has_key(key):
            Config.config[key] = value
            self.save()
        else:
            raise KeyError(key)
    def save(self):
        """Save the current config out to the config file"""
        f = open(self.conf_path, "w")
        f.write(json.dumps(Config.config, sort_keys=True, indent=4))
        f.close()






