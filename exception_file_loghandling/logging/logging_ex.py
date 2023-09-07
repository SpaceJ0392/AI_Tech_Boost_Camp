## Logging Handler
# - 프로그램이 실행되는 동안의 정보를 남기는 것 **log**
#     - 보통 유저의 접근, 프로그램의 Exception, 특정 함수의 사용 등을 남김
# - display 방식
#     - Console 화면에 출력, 파일에 남기기, DB에 남기기 등등
# - 실행 시점에서 남겨야 하는 기록, 개발 시점에서 남겨야 하는 기록이 존재
#     - 실행 시점에 남기는 것은 유저 등을 잡기 위함.
#     - 개발 시점에 남기는 것을 개발 중 error 등을 잡기 위함.
# - 기록은 `print`로 남기는 것도 가능함 그러나 Console 창에만 남기는 기록은 분석시 사용 불가
# - 때로는 레벨별(개발, 운영)로 기록을 남길 필요도 있음
# - 모듈 별로 별도의 logging을 남길 필요도 있음


import logging  # 기본적으로 일어난 결과는 print문과 유사

# 기본적인 logging leven은 warning 이므로 warning 부터 출력됨.
logging.debug("틀렸잖아!")
logging.info("확인해")
logging.warning("조심해!")
logging.error("에러났어!!!")
logging.critical("망했다...")  # 프로그램이 완전히 종료 될 때 남김.
