import modi
import time
import playsound #11.29 음성 출력을 위한 모듈 생성

bundle = modi.MODI()

ir1 = bundle.irs[0]
ir2 = bundle.irs[1]

env = bundle.envs[0]

display = bundle.displays[0] #디스플레이는 횡단보도용임.
led_crosswalk = bundle.leds[0] #횡단보도
led_traffic = bundle.leds[1] #자동차 신호등
led_spotlight1 = bundle.leds[2]
led_spotlight2 = bundle.leds[3]
led_spotlight3 = bundle.leds[4]
led_spotlight4 = bundle.leds[5]
speaker = bundle.speakers[0] #11.29 스피커 추가

#네트워크+적외선2+LED6(보행자/차/spotlight)+디스플레이+환경+스피커
#코드 돌리고 바로 실험하면 적외선 센서가 인식을 못해서 실행 한번 더 눌러줘야함!
#LED가 6개인데 실험할 때마다 위치가 바뀌어서 실험 때마다 무엇이 보행자/차/spotlight인지 확인해야 함.

while(env.brightness > 1): #낮
    display.text = "crosswalk has turned off" #횡단보도 안켜짐
    led_crosswalk.rgb = (100, 0, 0) #횡단보도 빨간불(안켜짐)
    led_traffic.rgb = (0, 100, 0) #차 초록불
    if 20 <= ir1.proximity <= 100 or 20 <= ir2.proximity <= 100: #만약 사정거리 내로 보행자 진입시, 횡단보도 on 범위 구체화 
        display.text = "pedestrian had detected"
        playsound.playsound('C:/Users/XXX/python/ped_det.mp3') #보행자가 감지됨
        display.text = "crosswalk will turn on"
        playsound.playsound('C:/Users/XXX/python/ped_on.mp3') #횡단보도 on
        led_traffic.rgb = (100, 100, 0) #차 주황불 
        time.sleep(1) #차량 신호등 주황불 -> 빨간불 time delay
        led_crosswalk.rgb = (0, 100, 0) #횡단보도 초록불
        led_traffic.rgb = (100, 0, 0) #차 빨간불
        led_spotlight1.rgb = (25, 21, 0) #스포트라이트로 자동차에게 보행자가 지나가고 있음을 확실히 각인시킴. 이하동문
        led_spotlight2.rgb = (25, 21, 0)
        led_spotlight3.rgb = (25, 21, 0)
        led_spotlight4.rgb = (25, 21, 0)
        remain_time = 10 #남은 횡단보도 시간
        for i in range(1, 11, 1):
            display.text = f'{remain_time}'
            time.sleep(1)
            remain_time = 10 - i
            if(remain_time >= 0): #횡단보도 신호음
                for i in range(1, 10, ):
                    speaker.tune = 3900, 100
                    time.sleep(0.0000001) #시간 term을 매우 짧게 잡아 삐비빅 소리 구현
                    speaker.turn_off()
                time.sleep(1) #신호음 사이의 여백
        display.text = "turn to red light"
        playsound.playsound('C:/Users/XXX/python/ped_off.mp3') #횡단보도 off
        led_spotlight1.rgb = (0, 0, 0)
        led_spotlight2.rgb = (0, 0, 0)
        led_spotlight3.rgb = (0, 0, 0)
        led_spotlight4.rgb = (0, 0, 0)
        led_crosswalk.rgb = (100, 0, 0) #횡단보도 빨간불
        led_traffic.rgb = (0, 100, 0) #차 신호 초록불
        time.sleep(1)
        
while(env.brightness <= 1): #밤(나머지 내용은 위와 동일)
    display.text = "crosswalk has turned off"
    led_crosswalk.rgb = (50, 0, 0)
    led_traffic.rgb = (0, 50, 0)
    if 20 <= ir1.proximity <= 100 or 20 <= ir2.proximity <= 100: 
        display.text = "pedestrian had detected"
        playsound.playsound('C:/Users/XXX/python/ped_det.mp3')
        display.text = "crosswalk will turn on"
        playsound.playsound('C:/Users/XXX/python/ped_on.mp3')
        led_traffic.rgb = (50, 50, 0)
        time.sleep(1)
        led_crosswalk.rgb = (0, 50, 0)
        led_traffic.rgb = (50, 0, 0)
        led_spotlight1.rgb = (50, 42, 0)
        led_spotlight2.rgb = (50, 42, 0)
        led_spotlight3.rgb = (50, 42, 0)
        led_spotlight4.rgb = (50, 42, 0)
        remain_time = 10
        for i in range(1, 11, 1):
            display.text = f'{remain_time}'
            time.sleep(1)
            remain_time = 10 - i
            if(remain_time >= 0):
                for i in range(1, 10, ):
                    speaker.tune = 3900, 100
                    time.sleep(0.0000001)
                    speaker.turn_off()
                time.sleep(1)
        display.text = "turn to red light"
        playsound.playsound('C:/Users/XXX/python/ped_off.mp3')
        led_spotlight1.rgb = (0, 0, 0)
        led_spotlight2.rgb = (0, 0, 0)
        led_spotlight3.rgb = (0, 0, 0)
        led_spotlight4.rgb = (0, 0, 0)
        led_crosswalk.rgb = (50, 0, 0)
        led_traffic.rgb = (0, 50, 0)
        time.sleep(1)
