import requests

def NewsFromBBC():
     
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"
 
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    # getting all articles in a string article
    article = open_bbc_page["articles"]
 
    # empty list which will
    # contain all trending news
    results = []
     
    for ar in article:
        results.append(ar["title"])

    news = ""   

    for i in range(len(results)):
         
        # printing all trending news
        #print(i + 1, results[i])
        news = news + str(i+1) + " -> " + results[i] + '\n'


    return news
    #to read the news out loud for us
    #from win32com.client import Dispatch
    #speak = Dispatch("SAPI.Spvoice")
    #speak.Speak(results)
