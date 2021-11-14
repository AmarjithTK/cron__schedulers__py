from cronsched import CronSched



welcome_screen = f"""
========================== Crontab Scheduler ========================

Current directory = {CronSched.crondir}

Do you want this directory as cron working directory ? Y/YES/TRUE/1 or N/NO/FALSE/1 : """

new_crontab = input(welcome_screen)

enabler = ['Y','YES','1','TRUE']
disabler = ['N','NO','0','FALSE']


if enabler.__contains__(new_crontab.upper()):
    CronSched.updateCron()
elif disabler.__contains__(new_crontab.upper()):
    print('\nSorry , come back when you need me !')
    exit()





# print('\n --------- NGINX SYNC CRONTAB  --------- \n ')
# new_crontab = input('Do you want to create crontab for this folder ? Y/yes/1/true or N/no/0/false  d/disable:')






# # for validator in validators:
# #     if new_crontab.upper() == validator:
# #        CronSched.out()
# #     else:
# #         break




# print('\n\nThank you for using the program')