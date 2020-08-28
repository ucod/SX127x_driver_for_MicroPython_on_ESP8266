import network
import time
#access the wifi and disable
ap = network.WLAN(network.AP_IF)
ap.active(False)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(False)

from esp import deepsleep
from machine import reset_cause, DEEPSLEEP_RESET
#turn off the wifi modem for a ~30ma drop in consumption
if not reset_cause() == DEEPSLEEP_RESET:
    # call 'system_deep_sleep_set_option' with value 4 and go to sleep for 1 uS 
    deepsleep(1, 4)
else:
    time.sleep(6)
    import gc
    gc.collect()
    import sx127x
    gc.collect()
    import test
    gc.collect()
    test.main()
