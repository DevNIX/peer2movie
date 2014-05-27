import yaml
import globals

import System


def bootstrap():
    System.debug("Bootstrapping")

    config_file = globals.CONFIG_FOLDER + "/" + globals.SERVER_NAME + ".yml"

    f_config = open(config_file)
    config = yaml.safe_load(f_config)
    f_config.close()

    System.debug("Using port " + str(config["network"]["port"]))
