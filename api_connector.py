import requests
    

def get_data():
    url = 'http://data.fixer.io/api/latest'
    params = {
        "access_key":'a8f1525c16255619e90fa062fb9dec28',
    }

    try:
        response = requests.get(url,params=params)
    except:
        return({'success':False,"error":{"info":"get request failed"}})

    if response.status_code == 200:
        data = response.json() 
        filtered_rates = {currency: data['rates'][currency] for currency in ['MAD', 'USD']}
        filtered_data = data.copy()
        filtered_data['rates'] = filtered_rates

        return(filtered_data)
    else:
        return({'success':False,"error":{"info":"get request failed"}})