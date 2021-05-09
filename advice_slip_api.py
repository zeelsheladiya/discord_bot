import requests

def advice_slip():
     
    main_url = " https://api.adviceslip.com/advice"
 
    res = requests.get(main_url)
    adviceslip = res.json()
 
    advice = adviceslip["slip"]

    advice = advice["advice"]

    return advice
