# 3commas-TakeProfit-Updater<br>
3commas TakeProfit Updater - My first python script to auto update active bot deals to increase takeprofit by stepscale.<br>
You have to install python and py3cw python wrapper:<br>
<code>pip install py3cw</code><br>
Please add your 3commas api key and api key secret in config.py file<br>

Step scale is configurable in config.py. Default is 0.5, so every safety order hit takeprofit is increased by 0.5%<br>
You can change take profit increase to fixed mode. Bot take profit + step in steps list. Check protifIncreaseSteps in config.py


If you want program to run only once, change time interval in config file to 0


config.py: 

# To disable logging set it to False
LOGGING = False

# Enable bot compounding and interval - NOT WORKING YET, DON'T USE!
# BOT_COMPOUNDING = False
# BOT_COMPOUNDING_INTERVAL = 5 #86400 seconds - 1 day

# PROFIT INCREASE MODE:
# Change False to True if you want to set fixed take profit for every order, check PROFIT_INCREASE_STEPS

FIXED_INCREASE_MODE = False

# Configurable step scale. Default is 0.5, so every safety order hit takeprofit is increased by 0.5%
PROFIT_STEP_SCALE = 0.5

# BOT TAKE PROFIT + STEP IN % FOR EVERY SAFETY ORDER IF FIXED MODE IS SELECTED
#                    SO1, SO2, SO3 etc...
PROFIT_INCREASE_STEPS = [0.5, 1, 2]

# TIME INTERVAL IN SECONDS TO CHECK YOUR DEALS IF CHANGE IS NEEDED, CHANGE TO 0 IF YOU WANT TO RUN THE SCRIPT ONCE
TIME_INTERVAL = 360

# Add your bot id's here separated by commas, You can find bot id's by clicking on your bot in DCA
# bots. Format: https://3commas.io/bots/xxxxx <- where xxxxx is your bot id
# BotIds = [111111, 222222]

BOT_IDS = [231231, 312321312]

# YOUR 3commas API KEYS
params = {
    "apiKey": "",
    "apiSecret": "",

}
