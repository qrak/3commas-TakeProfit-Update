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
