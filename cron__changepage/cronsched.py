import os
from crontab import CronTab


# to copy using brace expansion ================================================

#  only copying .html, .css , .js files from a group of files

#  cp -r test/{*.html,*.css,*.js} test2/


class CronSched:
    
    cron = CronTab(user='starship')
    
    crondir = cron.env['crondir']
    @classmethod
    def updateCron(self):
        cron_dir = os.getcwd()
        extension='{*.html,*.css,*.js}'
        add_command = f"""rsync -a --del {cron_dir}/{extension} himadri@192.168.1.196:mobile-testing/templates"""
        print('\nCron Updated successfully')
        self.cron.remove_all(comment='nginx-sync')
        job = self.cron.new(add_command,comment='nginx-sync')
        job.minutes.every(2)
        dir_string = (os.getcwd().split('/'))
        self.cron.env['crondir'] = dir_string[dir_string.__len__()-1]
        self.cron.write()




    # def enableCron(self):
    #     self.job.enable(True)
    #     self.cron.write()

    #     print('Cron Enabled successfully')


    # def disableCron(self):
    #     self.job.enable(False)
    #     self.cron.write()
    #     print('Cron disabled successfully') 

    # def getDir(self):
    #     if self.cron.env['crondir'] != 'not available':
    #         self.dir_list= self.cron.env['crondir'].split('/')
    #         self.currentDir = self.dir_list[self.dir_list.__len__()-2]  
    #         return self.currentDir


















