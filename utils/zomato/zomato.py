from selenium import webdriver
def get_number(driver,url) :
    driver.get(url)
    num_elements = driver.find_elements_by_class_name("kKemRh")
    numbers = []
    for i in range(len(num_elements)) :
        numbers.append((num_elements[i].text))
    print(numbers)
    return numbers




    
