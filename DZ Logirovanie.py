import requests as rq
import logging


#logger = logging.getLogger('RequestsLogger')

logging.basicConfig(level=logging.INFO, filename="success_responses.log", filemode="w", encoding="utf-8",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.WARNING, filename="bad_responses.log", filemode="w", encoding="utf-8",
                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.ERROR, filename="blocked_responses.log", filemode="w", encoding="utf-8",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

success_responses = open("success_responses.log", "w")
bad_responses = open("bad_responses.log", "w")
blocked_responses = open("blocked_responses.log", "w")


sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:

    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            #logging.info(f'{site}, response - {response}')
            success_responses.write(f'INFO: {site}, response ({response.status_code})\n')
            print(f'INFO: Сайт {site} доступен, response - 200 ')
        else:
            if response.status_code != 200:
                #logging.warning(f'{site}, response - {response}')
                bad_responses.write(f'WARNING: {site}, response ({response.status_code})\n')
                print(f'WARNING: Сайт {site} не доступен, response - {response}')
    except(rq.exceptions.ConnectionError, rq.exceptions.Timeout):
        #logging.error(f'ERROR: Сайт {site} не доступен, NO CONNECTION')
        blocked_responses.write(f'ERROR: {site}, response ({response.status_code})\n')
        print(f'ERROR: Сайт {site} не доступен, response - {response}')

success_responses.close()
bad_responses.close()
blocked_responses.close()
