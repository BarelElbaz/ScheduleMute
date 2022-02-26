from __future__ import print_function
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import time
import datetime



def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current local time
    check_time = check_time or datetime.datetime.now().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

def is_time_bigger(compareT, check_time=None):
    check_time = check_time or datetime.datetime.now().time()
    return compareT < check_time

def set_volume_muted(muted):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        #print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
        #volume.SetMasterVolume(0.6, None) # change sessions volume
        if muted:
            volume.SetMute(1, None)#mute/unmute sessions
        else:
            volume.SetMute(0, None) 

def get_today():
    now = datetime.datetime.now()
    return now.strftime("%A")

def main():
    while(True):
        today = get_today()
        muted = False
        if today == "Friday":
            if is_time_bigger(datetime.time(16,30)):
                muted = True
            else:
                muted = False
        elif today == "Saturday":
            if is_time_bigger(datetime.time(19,30)):
                muted = False
            else:
                muted = True   
                
        if is_time_between(datetime.time(8,20), datetime.time(20,45)):
            set_volume_muted(muted)
        else:
            set_volume_muted(True)

        time.sleep(300)#sleep for 5 min



if __name__ == "__main__":
    main()