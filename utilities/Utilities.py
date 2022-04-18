from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging


class drivers():
    chromeDriver = webdriver.Chrome(ChromeDriverManager().install())


class logger():
    def logs(level=logging.DEBUG):
        logging.basicConfig(
            level=logging.DEBUG,
            format="{asctime} {levelname:<8} {message}",
            style='{',
            filename='%slog' % __file__[:-2],
            filemode='a'
        )
        logging.critical("CRITICAL LEVEL")
        logging.error("ERROR LEVEL")
        logging.warning("WARNING LEVEL")
        logging.info("INFO LEVEL")
        logging.debug("DEBUG LEVEL")
