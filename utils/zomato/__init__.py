import requests




def getRestaurants(url):
    # 'https://www.zomato.com/webroutes/getPage?page_url=/ncr/great-food-no-bull&location=&isMobile=0'
    headers = {
    'Connection': 'keep-alive',
    'X-user-agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 FKUA.website/42/website/Desktop',
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': '/',
    'Origin': 'https://www.zomato.com'
    }
    res = requests.get(url, headers=headers)
    restaurants = []
    try:
        json = res.json()
        restaurants.append(json['page_data']['sections']['SECTION_ENTITIES_DATA'])
    except Exception as err:
        print(err)
        return {'success': False, 'message': str(err)}
    return {
        'success': True,
        'data': restaurants
    }
