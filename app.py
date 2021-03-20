import json
from utils.zomato import getRestaurants

with open('temp/best.json', 'w') as file:
    data = getRestaurants('https://www.zomato.com/webroutes/getPage?page_url=/ncr/great-food-no-bull&location=&isMobile=0')
    json.dump(data, file)
