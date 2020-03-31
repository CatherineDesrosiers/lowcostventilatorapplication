import subprocess

class Alarm:

    @classmethod
    def startAlarm(cls):
        subprocess.call([f'aplay {__file__}//analog-watch-alarm.wav'], shell=True)

    @classmethod
    def stopAlarm(cls):
        subprocess.call([f'pkill play'], shell=True)
