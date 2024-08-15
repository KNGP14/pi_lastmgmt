from argparse import ArgumentParser
import configparser
import urllib.request, json 

# ################
# Initialisiserung
# ################
currentPower = None

# ############################
# Konfigurationsdatei einlesen
# ############################
config = configparser.ConfigParser()
config.read('pi_lastmgmt.config')

config_section='ALLGEMEIN'
CONFIG_LUPUS_IP = config.get(config_section, 'LUPUS_IP', fallback="http://localhost:8000")
CONFIG_LUPUS_URI = config.get(config_section, 'LUPUS_URI', fallback="/values-mock.json")

# ##################
# Argumente einlesen
# ##################
parser = ArgumentParser(
            description='Lastmanagement für Raspberry Pi 2B')

parser.add_argument(
            "-m",
            "--mode",
            default="UNSET",
            dest="CLI_PARAM_MODE",
            required=True,
            choices=['cron', 'now'],
            help="Ausführungsmodus: cron = via cronjob | now = jetzt sofort manuell")
parser.add_argument(
            "-d",
            "--debug",
            default=False,
            dest="CLI_PARAM_DEBUG",
            required=False,
            action="store_true",
            help="Wenn angegeben, Debug-Modus aktivieren")

args = parser.parse_args()

if(args.CLI_PARAM_DEBUG):
    print('CLI_PARAM_MODE: {:s}'.format(args.CLI_PARAM_MODE))
    print('CLI_PARAM_DEBUG: {:b}'.format(args.CLI_PARAM_DEBUG))

# ##############################
# Lastmessung von LUPUS auslesen
# ##############################

lupus_url = CONFIG_LUPUS_IP + CONFIG_LUPUS_URI
if(args.CLI_PARAM_DEBUG):
    lupus_url = "http://localhost:8000/values-mock.json"
    print('LUPUS-Daten abrufen von Demo-Server:', lupus_url)

try:
    with urllib.request.urlopen(lupus_url, data=None, timeout=5) as url:
        data = json.load(url)
        if(args.CLI_PARAM_DEBUG):
            print(data)
        for kv in data['json_values']:
            if(kv['id'] == "P"):
                currentPower = kv["value"]
                if(args.CLI_PARAM_DEBUG):
                    print(currentPower)
except (ConnectionResetError, TimeoutError, urllib.error.URLError) as error: # type: ignore
    print('Fehler beim Abrufen der Daten vom LUPUS. Vieleicht offline?')
    print(' > URL:', lupus_url)
    print(' > Fehler:', error)
except Exception as error:
    print('Fehler beim Verarbeiten der Daten vom LUPUS.')
    print(' > URL:', lupus_url)
    print(' > Fehler:', error)

if(currentPower!=None):
    print('Aktuelle Last:', currentPower)