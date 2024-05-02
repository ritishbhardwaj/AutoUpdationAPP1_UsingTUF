import socket
import win32serviceutil
import servicemanager
import win32event
import win32service
import random
from pathlib import Path
import time


class SMWinservice(win32serviceutil.ServiceFramework):
    _svc_name_ = 'TestingService'
    _svc_display_name_ = 'Testing for leap-service'
    _svc_description_ = 'Python Service Description'

    @classmethod
    def parse_command_line(cls):
        '''
        ClassMethod to parse the command line
        '''
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        '''
        Constructor of the winservice
        '''
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        '''
        Called when the service is asked to stop
        '''
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        '''
        Called when the service is asked to start
        '''
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def start(self):
        self.isrunning =  True

    def stop(self):
        self.isrunning = False


    def main(self):
        i = 0
        while self.isrunning:
            random.seed()
            x = random.randint(1, 1000000)
            Path(f'c:{x}.txt').touch()
            time.sleep(5)
if __name__ == '__main__':
    SMWinservice.parse_command_line()