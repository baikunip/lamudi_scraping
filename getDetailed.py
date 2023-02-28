# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options #Use your own web browser
from user_agent import generate_user_agent, generate_navigator
import json
import pandas as pd

# df=pd.read_json('./bandungAll.geojson')
with open('./BDSK.geojson') as f:
    objt = json.load(f)
# for feature in objt['features']:
#     print(feature['properties'])
DRIVERPATH ="./chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
print(objt['features'][2999])
chartLabel=['2018-04', '2018-07', '2018-10', '2019-01', '2019-04', '2019-07', '2019-10', '2020-01', '2020-04', '2020-07', '2020-10', '2021-01', '2021-04', '2021-07', '2021-10', '2022-01', '2022-04']
print(len(objt['features']))
loopIndex=0
def update_result(payload):
    with open('./BDSKDetailed.geojson') as f:
        objt = json.load(f)
    objt['features'].append(payload)
    json_object = json.dumps(objt, indent=4)
    with open("BDSKDetailed.geojson", "w") as outfile:
        outfile.write(json_object)
    print(payload['properties']['id'])
driver1=webdriver.Chrome(executable_path=DRIVERPATH,options=chrome_options)
driver2=webdriver.Chrome(executable_path=DRIVERPATH,options=chrome_options)
driver3=webdriver.Chrome(executable_path=DRIVERPATH,options=chrome_options)
driver4=webdriver.Chrome(executable_path=DRIVERPATH,options=chrome_options)
driver5=webdriver.Chrome(executable_path=DRIVERPATH,options=chrome_options)
while loopIndex<len(objt['features']):
    # time.sleep(2)
    driver1.get(objt['features'][loopIndex]['properties']['link'])
    try:
        chartValue=driver1.find_element(By.CLASS_NAME,'ct-series-a').find_elements(By.TAG_NAME,'line')
        for index,val in enumerate(chartValue):
            objt['features'][loopIndex]['properties'][chartLabel[index]]=val.get_attribute('ct:value')
    except:
        for index,val in enumerate(chartLabel):
            objt['features'][loopIndex]['properties'][val]=0
    update_result(objt['features'][loopIndex])
    print(loopIndex)
    driver2.get(objt['features'][loopIndex+1]['properties']['link'])
    try:
        chartValue=driver2.find_element(By.CLASS_NAME,'ct-series-a').find_elements(By.TAG_NAME,'line')
        for index,val in enumerate(chartValue):
            objt['features'][loopIndex+1]['properties'][chartLabel[index]]=val.get_attribute('ct:value')
    except:
        for index,val in enumerate(chartLabel):
            objt['features'][loopIndex+1]['properties'][val]=0
    update_result(objt['features'][loopIndex+1])
    print(loopIndex+1)
    driver3.get(objt['features'][loopIndex+2]['properties']['link'])
    try:
        chartValue=driver3.find_element(By.CLASS_NAME,'ct-series-a').find_elements(By.TAG_NAME,'line')
        for index,val in enumerate(chartValue):
            objt['features'][loopIndex+2]['properties'][chartLabel[index]]=val.get_attribute('ct:value')
    except:
        for index,val in enumerate(chartLabel):
            objt['features'][loopIndex+2]['properties'][val]=0
    update_result(objt['features'][loopIndex+2])
    print(loopIndex+2)
    driver4.get(objt['features'][loopIndex+3]['properties']['link'])
    try:
        chartValue=driver4.find_element(By.CLASS_NAME,'ct-series-a').find_elements(By.TAG_NAME,'line')
        for index,val in enumerate(chartValue):
            objt['features'][loopIndex+3]['properties'][chartLabel[index]]=val.get_attribute('ct:value')
    except:
        for index,val in enumerate(chartLabel):
            objt['features'][loopIndex+3]['properties'][val]=0
    update_result(objt['features'][loopIndex+3])
    print(loopIndex+3)
    if not loopIndex==2995:
        driver5.get(objt['features'][loopIndex+4]['properties']['link'])
        try:
            chartValue=driver5.find_element(By.CLASS_NAME,'ct-series-a').find_elements(By.TAG_NAME,'line')
            for index,val in enumerate(chartValue):
                objt['features'][loopIndex+4]['properties'][chartLabel[index]]=val.get_attribute('ct:value')
        except:
            for index,val in enumerate(chartLabel):
                objt['features'][loopIndex+4]['properties'][val]=0
        update_result(objt['features'][loopIndex+4])
        print(loopIndex+4)
    if loopIndex==2995:
        loopIndex=loopIndex+4
    else:
        loopIndex=loopIndex+5
    

# json_object = json.dumps(objt, indent=4)
# with open("bandungDetailed.geojson", "w") as outfile:
#     outfile.write(json_object)
    