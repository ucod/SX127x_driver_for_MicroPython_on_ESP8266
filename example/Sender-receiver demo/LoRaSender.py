from time import sleep
#import time


def send(lora):
    counter = 0
    print("LoRa Sender")

    while True:
        payload = 'ehlo ({0})'.format(counter)
        print("Sending packet: \n{}\n".format(payload))
        lora.println(payload)
        print("Sent \n")
        counter += 1
        sleep(90)
        #time.sleep_ms(30000)
