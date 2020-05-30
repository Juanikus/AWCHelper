WINDOWSIZE = "535x350"
LABELWIDTH = 15
ENTRYWIDTH = 50
RESULTWIDTH = LABELWIDTH + ENTRYWIDTH

ANILISTQUERY = """
    {{
              MediaList(userName:\"{}\", mediaId:{}) {{
                media{{
                    title{{
                        romaji
                    }}
                }},
                startedAt {{
                  year
                  month
                  day
                }},
                completedAt {{
                  year
                  month
                  day
                }}
              }}
            }}
    """

ANILISTHEADER = {"Content-Type": "application/json", "Accept": "application/json"}

RESPONSETEMPLATE = "Start: {start} Finish: {finish} __{challenge}__ [{title}]({link})"


DBNAME = "user.db"