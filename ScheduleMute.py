from __future__ import print_function
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import time
import datetime

class VolumeControl:

    def __init__(self):
        self.muted = False

    def is_time_between(self, begin_time, end_time, check_time=None):
        # If check time is not given, default to current local time
        check_time = check_time or datetime.datetime.now().time()
        if begin_time < end_time:
            return check_time >= begin_time and check_time <= end_time
        else: # crosses midnight
            return check_time >= begin_time or check_time <= end_time

    def is_time_bigger(self, compareT, check_time=None):
        check_time = check_time or datetime.datetime.now().time()
        return compareT < check_time

    def set_volume_muted(self, muted):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if muted:
                volume.SetMute(1, None)#mute/unmute sessions
            else:
                volume.SetMute(0, None) 

    def get_today(self):
        now = datetime.datetime.now()
        return now.strftime("%A")

    def main(self):
        while(True):
            today = self.get_today()
            self.muted = False
            if today == "Friday":
                if self.is_time_bigger(datetime.time(16,30)):
                    self.muted = True
                else:
                    self.muted = False
            elif today == "Saturday":
                if self.is_time_bigger(datetime.time(21,00)):
                    self.muted = False
                else:
                    self.muted = True   

            if self.is_time_between(datetime.time(7,30), datetime.time(21,00)):
                self.set_volume_muted(self.muted)
            else:
                self.set_volume_muted(True)

            time.sleep(300)#sleep for 5 min

if __name__ == "__main__":
    vol_control = VolumeControl()
    vol_control.main()
