from argparse import ArgumentParser
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

print('CLI_PARAM_MODE: {:s}'.format(args.CLI_PARAM_MODE))
print('CLI_PARAM_DEBUG: {:b}'.format(args.CLI_PARAM_DEBUG))

