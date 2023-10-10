간단한 웹 스크래핑
===

Beautiful Soup과 Requests 라이브러리를 사용하여 웹 페이지에서 정보 추출 (정적 크롤링)

## 패키지 다운로드

<pre><code>

  #!/bin/bash

  pip3 install beautifulsoup4
  
</code></pre>

## 기본 코드

<pre><code>

import requests
from bs4 import BeautifulSoup

def main():

    URL = "https://www.naver.com"

    response = requests.get(URL)

    if response.status_code == 200:
        targetData = response.text
        htmlData = BeautifulSoup(targetData, 'html.parser')

        #title parser
        print(htmlData.title)
        
    else : 
        print(response.status_code)

if __name__ == "__main__":
    main()

  
</code></pre>

## 구현 관련 문의

김지훈, xxxjjhhh@naver.com, 010-8792-7589

---
