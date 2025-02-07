import requests
import threading
import requests
import json
import os

url = os.environ.get('TARGET_URL3')
ORIGIN_URL = os.environ.get("ORIGIN_URL3")
REFERER_URL = os.environ.get("REFERER_URL3")



payload = {}
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Origin': ORIGIN_URL,
  'Pragma': 'no-cache',
  'Referer': REFERER_URL,
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Lude.cc',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCIsInRlYW0iOiJzdW9oYSB0ZWFtIGRldmVsb3AifQ.eyJpc3MiOiJzdW9oYSBzeXN0ZW0iLCJleHAiOjE3NDE1NDIxMTQsImp0aSI6IjQ1MTE2MzYwMjY1ODA0NTk5MzYifQ.u1Rlt4Ru82b_dPV2-SHXgUkkp80X4FwtSaEAy7u45zD35PTiv9pfUi67UYRu0rnb'
}



def send_request():
    try:
        response = requests.request(
            "POST", url, headers=headers, data=payload, timeout=10)
        print(response.status_code)
    except Exception as e:
        # print(e)
        print('exception')


thread_list = []
for i in range(100):
    t = threading.Thread(target=send_request)
    t.start()
    thread_list.append(t)


for t in thread_list:
    t.join()
    
print("done")