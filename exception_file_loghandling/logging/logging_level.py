import logging

if __name__ == "__main__":
    logger = logging.getLogger("main")
    # logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.INFO)
    # -- python 3.8 이전 버전 (지금은 basicConfig 쓰고 써야함.)

    # 출력 위치 설정
    steam_handler = logging.FileHandler(
        "my_log", mode="a", encoding="utf-8"
    )
    logger.addHandler(steam_handler)

    logger.debug("틀렸잖아!")
    logger.info("확인해")
    logger.warning("조심해!")
    logger.error("에러났어!!!")
    logger.critical("망했다...")
