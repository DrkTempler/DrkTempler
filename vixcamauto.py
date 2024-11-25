from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pymediainfo import MediaInfo
import requests
import time
import logging
import os

#터미널에 로그출력
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#메인페이지
def setup_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service() 
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    return driver

#로그인
def login(driver, username, password):
    driver.get('http://172.16.15.108/')
    action = ActionChains(driver)
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/form/p[1]/input').click()
    action.send_keys(username).key_down(Keys.TAB).send_keys(password).pause(1).key_down(Keys.ENTER).perform()
    action.reset_actions()
    time.sleep(5)
    logger.info('로그인 성공')

#설정로그인 + 비디오 스트림 3, 4 h.264로 설정
def loginop(driver, username, password):
    driver.get('http://172.16.15.108/')
    action = ActionChains(driver)
    time.sleep(5)
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/form/p[3]/div/ins').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/form/p[1]/input').click()
    action.send_keys(username).key_down(Keys.TAB).send_keys(password).pause(1).key_down(Keys.ENTER).perform()
    action.reset_actions()
    time.sleep(5)
    logger.info('설정로그인 성공')

    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[2]/a').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[2]/ul/li[2]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[1]/select/option[1]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[2]/select/option[1]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/a[3]').click()
    logger.info('비디오 스트림 3,4 H264 코덱으로 설정 완료')

#탭 호출 > 라이브
def tab_l(driver):
    driver.find_element(By.XPATH, '/html/body/div[1]/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[1]/a[1]').click()
    logger.info('라이브 화면으로 이동')

#탭 호출 > 플레이백
def tab_p(driver):
    driver.find_element(By.XPATH, '/html/body/div[1]/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[1]/a[2]').click()
    logger.info('플레이백 화면으로 이동')

#탭 호출 > 설정
def tab_o(driver):
    driver.find_element(By.XPATH, '/html/body/div[1]/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[1]/a[3]').click()
    logger.info('설정 화면으로 이동')

#탭 호출 > 로그아웃
def tab_bye(driver):
    driver.find_element(By.XPATH, '/html/body/div[1]/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[1]/a[4]').click()
    logger.info('로그아웃')

#설정 > 비디오 스트림 진입
def op_stream(driver):
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[2]/a').click()
    streamgo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/ul/li[2]/ul/li[2]/a')))
    streamgo.click()
    logger.info('비디오 스트림 진입 완료')

#플레이백 > 비디오 스트림 진입
def op_stream_pb(driver):
    driver.find_element(By.XPATH, '/html/body/div[1]/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/a[3]/i').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[2]/a').click()
    streamgo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/ul/li[2]/ul/li[2]/a')))
    streamgo.click()
    logger.info('비디오 스트림 진입 완료')


#저장소 겹쳐쓰기 설정
def reckeep(driver):
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[4]/a').click()
    driver.find_element(By.XPATH, '//*[@id="tab-record"]/div[1]/label/div').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('저장소 겹쳐쓰기 설정 완료')

#이벤트 녹화 사용설정-비디오 스트림1
def recon(driver):
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[5]/a').click()
    driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[5]/ul/li[2]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="tab-record"]/div[1]/label/div').click()
    driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('비디오 스트림1로 이벤트 녹화 사용설정 완료')

#이벤트 녹화 사용설정-비디오 스트림2
def recon2(driver):
    driver.find_element(By.XPATH, '/html/body/div[1]/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/a[3]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[5]/a').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[5]/ul/li[2]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[1]/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[1]/div[2]/select/option[2]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('비디오 스트림2로 이벤트 녹화 사용설정 완료')

#이벤트 녹화 사용설정-비디오 스트림3
def recon3(driver):
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[5]/a').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[5]/ul/li[2]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[1]/div[2]/select').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[1]/div[2]/select/option[3]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('비디오 스트림3로 이벤트 녹화 사용설정 완료')

#이벤트 녹화 사용설정-비디오 스트림4
def recon4(driver):
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[5]/a').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[5]/ul/li[2]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[1]/div[2]/select').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[1]/div[2]/select/option[4]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('비디오 스트림4로 이벤트 녹화 사용설정 완료')


#이벤트 녹화 설정(타이머)
def rectimer(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[1]/ul/li[5]/a'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/ul/li[5]/ul/li[1]/a'))).click()
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/div[1]/ul/li[9]/a'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tab-timer"]/div[1]/label/div'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[9]/div[3]/select'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[9]/div[3]/select/option[1]'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[9]/div[4]/select'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[9]/div[4]/select/option[2]'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button'))).click()
    logger.info('타이머 트리거 설정 완료 - 1분!')
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/ul/li[5]/ul/li[3]/a'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[2]/input[1]'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/div[2]/div/div[1]/select'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/div[2]/div/div[1]/select/option[46]'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="modal_rule"]/div/div/div[2]/form/div[3]/div[2]/div[8]/div/label/div'))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]'))).click()
    logger.info('이벤트 규칙 설정완료 - 타이머')

#이벤트 영상 추출하기
def videosave(driver, videoname):
    driver.find_element(By.XPATH, '//*[@id="sidebar-shortcuts-large"]/a[2]').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/td[2]'))).click()
    video_element = driver.find_element(By.TAG_NAME, 'video')
    video_url = video_element.get_attribute('src')
    response = requests.get(video_url)
    directory = "D:/testvideo"
    os.makedirs(directory, exist_ok=True)
    file_name = f"{videoname}.mp4"
    file_path = os.path.join(directory, file_name)
    try:
        with open(file_path, 'wb') as file:
             file.write(response.content)
        logger.info(f"비디오 파일이 '{file_path}'으로 저장되었습니다.")
    except Exception as e:
        logger.error(f"비디오 파일 저장 중 오류 발생: {e}")

#이벤트 영상 조건 확인하기
def info(videoname):
    directory = os.path.join("D:", "testvideo")
    file_path = os.path.join(directory, f"{videoname}")
    file_path = os.path.join("D:", "testvideo", f"{videoname}.mp4")
    media_info = MediaInfo.parse(file_path)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            print("코덱", track.codec_id)
            print("코덱 프로파일", track.format_profile)
            print("영상길이", track.duration)
            print("fps", track.frame_rate)
            print("width", track.width)
            print("height", track.height)
            print("비트레이트 모드", track.bit_rate_mode)
            print("비트레이트", track.bit_rate)
            # print("frames", int(round((float(track.duration) * float(track.frame_rate))/1000)))
            # print(track.to_data())

#초기화 하기
def clear(driver, password):
    action = ActionChains(driver)
    loginop()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[6]/a').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[6]/ul/li[5]/a').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[4]/div/div/div[1]/div[2]/div/div[3]/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[4]/div[7]/button[2]').click()
    time.sleep(100)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div/div[2]/div/input').click()
    action.send_keys(password).key_down(Keys.TAB).send_keys(password).pause(1)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[7]/button[2]').click()

#CAMa-1 압축방식 High
def CAMa1(driver):
    videoname = 'CAMa1'
    #압축 방식 H.264 High
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[1]/select/option[1]').click()
    #해상도 2160
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[2]/select/option[1]').click()
    #프레임레이트 30
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select/option[1]').click()
    #GOP크기 60
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select/option[1]').click
    #비트레이트 제어 CBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[6]/select/option[2]').click()
    #비트레이트 6000
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[7]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[7]/select/option[101]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-1 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-2 압축방식 Main
def CAMa2(driver):
    videoname = 'CAMa2'
    #압축 방식 H.264 Main
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[1]/select/option[2]').click()
    #해상도 2160
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[2]/select/option[1]').click()
    #프레임레이트 30
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select/option[1]').click()
    #GOP크기 60
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select/option[1]').click
    #비트레이트 제어 CBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[6]/select/option[2]').click()
    #비트레이트 6000
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[7]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[7]/select/option[101]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-2 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-3 압축방식 Smart
def CAMa3(driver):
    videoname = 'CAMa3'
    #압축 방식 H.264+ Smart
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[1]/select/option[3]').click()
    #해상도 2160
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[2]/select/option[1]').click()
    #프레임레이트 30
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select/option[1]').click()
    #GOP크기 60
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select/option[1]').click
    #비트레이트 제어 CBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[6]/select/option[2]').click()
    #비트레이트 6000
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[7]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[7]/select/option[101]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-3 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-4 해상도 1728, 프레임 1
def CAMa4(driver):
    videoname = 'CAMa4'
    #압축 방식 H.264 High
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[1]/select/option[1]').click()
    #해상도 1728
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[2]/select/option[2]').click()
    #프레임레이트 1
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select/option[30]').click()
    #GOP크기 60
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select/option[1]').click
    #비트레이트 제어 CBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[6]/select/option[2]').click()
    #비트레이트 6000
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[7]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[7]/select/option[101]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-4 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-5 해상도 1440, 프레임 15, 비트레이트12000
def CAMa5(driver):
    videoname = 'CAMa5'
    #압축 방식 H.264 High
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[1]/select/option[1]').click()
    #해상도 1440
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[2]/select/option[3]').click()
    #프레임레이트 1
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select/option[15]').click()
    #GOP크기 60
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select/option[1]').click
    #비트레이트 제어 CBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[6]/select/option[2]').click()
    #비트레이트 12000
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[7]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[7]/select/option[1]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-5 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-6 비트레이트 제어 VBR
def CAMa6(driver):
    videoname = 'CAMa6'
    #압축 방식 H.264 High
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[1]/select/option[1]').click()
    #해상도 1440
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[2]/select/option[3]').click()
    #프레임레이트 1
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select/option[15]').click()
    #GOP크기 60
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[3]/select/option[1]').click
    #비트레이트 제어 VBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[2]/div/div[6]/select/option[2]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-6 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-7 ************************비디오스트림2 필수지정!!*******************************
def CAMa7(driver):
    videoname = 'CAMa7'
    #압축 방식 H.264 High
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[1]/select/option[1]').click()
    #해상도 1080
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[2]/select/option[1]').click()
    #프레임레이트 30
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select/option[1]').click()
    #GOP크기 60
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select/option[1]').click
    #비트레이트 제어 CBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[6]/select/option[2]').click()
    #비트레이트 12000
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[7]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[7]/select/option[1]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-7 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-8
def CAMa8(driver):
    videoname = 'CAMa8'
    #압축 방식 H.264 Main
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[1]/select/option[2]').click()
    #해상도 896
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[2]/select/option[2]').click()
    #프레임레이트 1
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select/option[30]').click()
    #GOP크기 60
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select/option[1]').click
    #비트레이트 제어 CBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[6]/select/option[2]').click()
    #비트레이트 6000
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[7]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[7]/select/option[61]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-8 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

# #CAMa-9
# def CAMa9(driver):
#     videoname = 'CAMa9'
#     #압축 방식 MJPEG
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[1]/select').click()
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[1]/select/option[6]').click()
#     #해상도 720
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[2]/select').click()
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[2]/select/option[3]').click()
#     #프레임레이트 30
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select').click()
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select/option[1]').click()
#     #품질 99
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[5]/select').click()
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[5]/select/option[1]').click()
#     #저장
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
#     logger.info('CAMa-9 TC Precondition 설정 완료')
#     time.sleep(150)
#     videosave(driver, videoname)

#CAMa-10
def CAMa10(driver):
    videoname = 'CAMa10'
    #압축 방식 H.264 Main
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[1]/select/option[2]').click()
    #해상도 432
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[2]/select/option[4]').click()
    #프레임레이트 30
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select/option[1]').click()
    #GOP크기 60
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select/option[1]').click
    #비트레이트 제어 CBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[6]/select/option[2]').click()
    #비트레이트 4500
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[7]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[7]/select/option[36]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-10 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-11
def CAMa11(driver):
    videoname = 'CAMa11'
    #압축 방식 H.264 High
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[1]/select/option[1]').click()
    #해상도 392
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[2]/select/option[5]').click()
    #프레임레이트 20
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select/option[11]').click()
    #GOP크기 60
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select/option[1]').click
    #비트레이트 제어 VBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[6]/select/option[1]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-11 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-12
def CAMa12(driver):
    videoname = 'CAMa12'
    #압축 방식 H.264 High
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[1]/select/option[1]').click()
    #해상도 360
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[2]/select/option[5]').click()
    #프레임레이트 1
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select/option[30]').click()
    #GOP크기 60
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[3]/select/option[1]').click
    #비트레이트 제어 VBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[2]/div/div[6]/select/option[1]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-12 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-13 *********************비디오스트림3 필수 지정!!!!!!**************************
def CAMa13(driver):
    videoname = 'CAMa13'
    #압축 방식 H.264 High
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[1]/select/option[1]').click()
    #해상도 432
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[2]/select/option[1]').click()
    #프레임레이트 30
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[3]/select/option[1]').click()
    #GOP크기 10
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[4]/select/option[246]').click
    #비트레이트 제어 CBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[6]/select/option[2]').click()
    #비트레이트 8000
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[7]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[7]/select/option[1]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-13 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-14
def CAMa14(driver):
    videoname = 'CAMa14'
    #압축 방식 H.264 Main
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[1]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[1]/select/option[2]').click()
    #해상도 392
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[2]/select/option[2]').click()
    #프레임레이트 15
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[3]/select/option[16]').click()
    #GOP크기 10
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[4]/select/option[246]').click
    #비트레이트 제어 VBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[6]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[6]/select/option[1]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-14 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-15
# def CAMa15(driver):
#     videoname = 'CAMa15'
#     #압축 방식 MJPEG
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[1]/select').click()
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[1]/select/option[6]').click()
#     #해상도 360
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[2]/select').click()
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[2]/select/option[3]').click()
#     #프레임레이트 1
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[3]/select').click()
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[3]/select/option[30]').click()
#     #품질 10
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[5]/select').click()
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[3]/div/div[2]/div/div[5]/select/option[10]').click
#     #저장
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
#     logger.info('CAMa-15 TC Precondition 설정 완료')
#     time.sleep(150)
#     videosave(driver, videoname)

#CAMa-16 *****************비디오스트림4 필수 지정!!!!!!!!!!!!!!!!**************************************
def CAMa16(driver):
    videoname = 'CAMa16'
    #압축 방식 H.264 High
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[2]/select/option[1]').click()
    #해상도 720
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[3]/select/option[1]').click()
    #프레임레이트 30
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[4]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[4]/select/option[1]').click()
    #GOP크기 10
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[5]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[5]/select/option[246]').click
    #비트레이트 제어 VBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[7]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[7]/select/option[1]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-16 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-17
def CAMa17(driver):
    videoname = 'CAMa17'
    #압축 방식 H.264 Main
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[2]/select/option[2]').click()
    #해상도 432
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[3]/select/option[2]').click()
    #프레임레이트 30
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[4]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[4]/select/option[1]').click()
    #GOP크기 100
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[5]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[5]/select/option[156]').click
    #비트레이트 제어 VBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[7]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[7]/select/option[1]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-17 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-18
def CAMa18(driver):
    videoname = 'CAMa18'
    #압축 방식 H.264 Main
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[2]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[2]/select/option[2]').click()
    #해상도 392
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[3]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[3]/select/option[3]').click()
    #프레임레이트 15
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[4]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[4]/select/option[16]').click()
    #GOP크기 10
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[5]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[5]/select/option[246]').click
    #비트레이트 제어 CBR
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[7]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[7]/select/option[2]').click()
    #비트레이트 4000
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[8]/select').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[8]/select/option[41]').click()
    #저장
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
    logger.info('CAMa-18 TC Precondition 설정 완료')
    time.sleep(150)
    videosave(driver, videoname)
    info(videoname)

#CAMa-19
# def CAMa19(driver):
#     videoname = 'CAMa19'
#     #압축 방식 MJPEG
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[2]/select').click()
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[2]/select/option[3]').click()
#     #해상도 360
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[3]/select').click()
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[3]/select/option[3]').click()
#     #프레임레이트 15
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[4]/select').click()
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[4]/select/option[16]').click()
#     #품질 30
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[6]/select').click()
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]/div/form/div[4]/div/div[2]/div/div[6]/select/option[8]').click()
#     #저장
#     driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/h1/button').click()
#     logger.info('CAMa-19 TC Precondition 설정 완료')
#     time.sleep(150)
#     videosave(driver, videoname)
# 이 코드가 궁금하신가요? 코드 짠애가 똥멍청이라서 영상으로 못뽑히는 프로파일까지 코드를 짜놨답니다


    
##테스트 진행 전 무조건 저장소 초기화, 시스템 초기화 후 비밀번호 초기 설정까지 완료하세요
def main():
    driver = setup_driver()
    try:
        loginop(driver, 'admin', 'pass0001!')
        time.sleep(5)
        recon(driver)
        time.sleep(5)
        reckeep(driver)
        time.sleep(5)
        rectimer(driver)
        time.sleep(5)
        op_stream(driver)
        time.sleep(5)
        CAMa1(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        CAMa2(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        CAMa3(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        CAMa4(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        CAMa5(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        CAMa6(driver)
        time.sleep(5)
        recon2(driver)
        time.sleep(5)
        op_stream(driver)
        time.sleep(5)
        CAMa7(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        CAMa8(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        # CAMa9(driver)
        # time.sleep(5)
        # op_stream_pb(driver)
        # time.sleep(5)
        CAMa10(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        CAMa11(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        CAMa12(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        recon3(driver)
        time.sleep(5)
        op_stream(driver)
        time.sleep(5)
        CAMa13(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        CAMa14(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        # CAMa15(driver)
        # time.sleep(5)
        # op_stream_pb(driver)
        # time.sleep(5)
        recon4(driver)
        time.sleep(5)
        op_stream(driver)
        time.sleep(5)
        CAMa16(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        CAMa17(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        CAMa18(driver)
        time.sleep(5)
        op_stream_pb(driver)
        time.sleep(5)
        # CAMa19(driver)
        # time.sleep(5)
        # op_stream_pb(driver)
        # time.sleep(5)
    finally:
        pass

if __name__ == "__main__":
    main()