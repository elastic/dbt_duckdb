import os,subprocess
from time import sleep

# set color class
# https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
# https://www.oreilly.com/library/view/bash-cookbook/0596526784/apas03.html
class bcolors:
    GREEN = '\033[32m'
    GREEN_REVERSE = '\033[32;7m'
    RED = '\033[31m'
    RED_REVERSE = '\033[31;7m'
    YELLOW = '\033[33m'
    BLUE = '\033[34;1;43m'
    ELASTIC = '\033[36;1;45m'
    GREY = '\033[37;2m'
    ENDC = '\033[0m'

# initial print to terminal
print('')
print(f"{bcolors.GREEN}Running Setup Checks...{bcolors.ENDC} ☕☕☕")
print('')
sleep(1.5)
# check for glcoud ADC's
if os.path.isfile('/root/.config/gcloud/application_default_credentials.json') == False:
    print(f"{bcolors.RED}To Log into GCP..{bcolors.ENDC}")
    print('')
    sleep(1.5)
    os.system('gcloud auth application-default login --project=esbi-test')
    print('')
else:
    print(f"{bcolors.GREEN}You are logged into BigQuery... ✔{bcolors.ENDC}")
    print('')
    sleep(1.5)
# check for dbt packages
if os.path.exists('/workspaces/dbt/dbt_packages') == False:
    print(f"{bcolors.YELLOW}Installing dbt Packages...{bcolors.ENDC} ☕☕☕")
    print('')
    sleep(1.5)
    os.system('dbt deps')
else:
    print(f"{bcolors.GREEN}dbt packages are installed... ✔{bcolors.ENDC}")
    print('')
    sleep(1.5)
# check for dev schema env var
if "DBT_DEV_DATASET" not in os.environ:
    print(f"{bcolors.RED_REVERSE}Your dbt development schema is not set, enter it below...{bcolors.ENDC} ✍✍✍")
    print(f"{bcolors.GREY}Examples: dbt_myfeature, dbt_myname{bcolors.ENDC}")
    print('')
    dev_dataset = input(f"{bcolors.YELLOW}DBT_DEV_DATASET: {bcolors.ENDC}")
    print('')
    os.system(f'echo export DBT_DEV_DATASET={dev_dataset} > ~/.bashrc')
    sleep(1.5)
else:
    change = input(f"{bcolors.GREEN}Your dbt dev schema is set as {bcolors.BLUE}{os.environ['DBT_DEV_DATASET']}{bcolors.ENDC}. {bcolors.YELLOW}Would you like to update it? (Y/n): {bcolors.ENDC}")
    print('')
    if change.lower() == 'y':
        dev_dataset = input(f"{bcolors.YELLOW}DBT_DEV_DATASET: {bcolors.ENDC}")
        os.system(f'echo export DBT_DEV_DATASET={dev_dataset} > ~/.bashrc')
        # os.system('source ~/.bashrc')
        print('')
        print(f'{bcolors.YELLOW}Please open a new shell after this script finishes.{bcolors.ENDC}')
        print('')
        sleep(1.5)
    else:
        pass
# Give the Green Light
print(f"{bcolors.GREEN_REVERSE}Be sure to make a branch for your development!{bcolors.ENDC} ↱")
print('')
sleep(1)
print(f"{bcolors.ELASTIC}Enjoy!{bcolors.ENDC} 🤖🤖🤖")