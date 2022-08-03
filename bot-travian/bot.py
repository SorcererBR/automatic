from selenium import webdriver

browser = webdriver.Firefox()

def get_resources_elements(css_element_location):
    browser.get('https://ts4.lusobrasileiro.travian.com/dorf1.php')
    pattern = 'html#mainLayout body div#background div#bodyWrapper div#center div#contentOuterContainer.size1 div.contentContainer div#content.village1 map#rx area'
    RESOURCES_FIELD = []
    for resource_field in browser.find_elements_by_css_selector(pattern):
        RESOURCES_FIELD.append('bid':resource_field.get_attribute())

def get_element(css_element_location):
    css_element = browser.find_elements_by_css_selector(css_element_location)
    if type(css_element) == list:
        try:
            if all:
                return css_element
            return css_element[0]
        except Exception as e:
            print('[-] Elemento não encontrado')
            return []

    return css_element

MAP_ALL_CONSTRUCTIONS = {
    'URL':'https://ts4.lusobrasileiro.travian.com/build.php?id=',
    'UPGRADE_BTN':'html#mainLayout body div#background div#bodyWrapper div#center div#contentOuterContainer.size1 div.contentContainer div#content.build div  div.roundedCornersBox.big div.upgradeButtonsContainer div.section1 button'
}

MAP_LOGINPAGE = {
    'URL':'https://ts4.lusobrasileiro.travian.com/login.php',
    'txtUsername':'html#mainLayout body div#background div#bodyWrapper div#center div#contentOuterContainer.size1 div.contentContainer div#content.login div.outerLoginBox div.innerLoginBox form table.transparent.loginTable tbody tr.account td input.text',

    'txtPass':'html#mainLayout body div#background div#bodyWrapper div#center div#contentOuterContainer.size1 div.contentContainer div#content.login div.outerLoginBox div.innerLoginBox form table.transparent.loginTable tbody tr.pass td input.text',

    'btnLogin':'html#mainLayout body div#bodyWrapper div#center div#contentOuterContainer.size1 div.contentContainer div#content.login div.outerLoginBox div.innerLoginBox form table.transparent.loginTable tbody tr.loginButtonRow td button#s1.green'    
}

MAP_RESOURCES_FIELD = {
    'BOSQUE_1':{
        'BID':''
    },
    'BOSQUE_2':{
        'BID':'3'
    },
    'BOSQUE_3':{
        'BID':'14'
    },
    'BOSQUE_4':{
        'BID':'17'
    }
}

MAP_QUEUE_TIME = {
    'CONSTRUCTION':{},
    'HEADQUARTERS':{}
}

browser.get(MAP_LOGINPAGE['URL'])

## LOGIN TO ACCOUNT ##
get_element(MAP_LOGINPAGE['txtUsername']).send_keys('SorcererBR')
get_element(MAP_LOGINPAGE['txtPass']).send_keys('')
get_element(MAP_LOGINPAGE['btnLogin']).click()

'''
browser.get(MAP_ALL_CONSTRUCTIONS['URL'] + MAP_RESOURCES_FIELD['BOSQUE_2']['BID'])
get_element(MAP_ALL_CONSTRUCTIONS['UPGRADE_BTN']).click()
'''
campos = ''

var = get_element(campos, all=True)
