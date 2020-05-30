import requests
from urllib import parse
import datetime

from Resources import *


class DataFetcher:

    def __init__(self):
        self.__setTemplates()

    def __setTemplates(self):
        self._query = ANILISTQUERY
        self._header = ANILISTHEADER
        self._responseTemplate = RESPONSETEMPLATE

    def __getDateString(self, date):
        if date["year"] is None or date["month"] is None or date["day"] is None:
            return "DD/MM/YY"
        else:
            startDate = datetime.datetime(date["year"], date["month"], date["day"])
            return startDate.strftime("%d/%m/%y")

    def getIdFromURL(self, url):
        try:
            path = parse.urlparse(url).path
            x = path.split('/')
            return x[2]
        except Exception:
            raise Exception("Invalid Link")

    def runQuery(self, userName, mediaId):
        query = self._query.format(userName, mediaId)
        response = requests.post('https://graphql.anilist.co', json={'query': query}, headers=self._header)
        if response.status_code == 200:
            json = response.json()

            startedAt = json["data"]["MediaList"]["startedAt"]
            completedAt = json["data"]["MediaList"]["completedAt"]
            title = json["data"]["MediaList"]["media"]["title"]["romaji"]

            result = [
                title,
                self.__getDateString(startedAt),
                self.__getDateString(completedAt)
            ]

            return result
        else:
            raise Exception("No data found. Check username and link. Maybe anime is not in your media list")

    def getResponse(self, startDate, endDate, challenge, title, link):
        return self._responseTemplate.format(start=startDate, finish=endDate, challenge=challenge, title=title,
                                             link=link)
