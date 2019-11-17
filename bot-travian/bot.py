from selenium import webdriver

def get_element(css_element_address):
    css_element = browser.find_elements_by_css_selector(css_element_address)
    if type(css_element) == list:
        print(css_element)
        return css_element[0]
    return css_element

MAP_LOGINPAGE = {
    'URL':'https://ts4.lusobrasileiro.travian.com/login.php',
    'txtUsername':'html#mainLayout body div#background div#bodyWrapper div#center div#contentOuterContainer.size1 div.contentContainer div#content.login div.outerLoginBox div.innerLoginBox form table.transparent.loginTable tbody tr.account td input.text',

    'txtPass':'html#mainLayout body div#background div#bodyWrapper div#center div#contentOuterContainer.size1 div.contentContainer div#content.build div#build.gid1.level0 div.roundedCornersBox.big div.upgradeButtonsContainer div.section1 button#button5dd0ef8716a31.green.build',

    'btnLogin':'html#mainLayout body div#bodyWrapper div#center div#contentOuterContainer.size1 div.contentContainer div#content.login div.outerLoginBox div.innerLoginBox form table.transparent.loginTable tbody tr.loginButtonRow td button#s1.green'

    
}

MAP_RESOURCES = {
    'BOSQUE_1':{
        'URL':'https://ts4.lusobrasileiro.travian.com/build.php?id=1',
        'UPGRADE_BTN':'html#mainLayout body div#background div#bodyWrapper div#center div#contentOuterContainer.size1 div.contentContainer div#content.build div#build.gid1.level0 div.roundedCornersBox.big div.upgradeButtonsContainer div.section1 button#button5dd0ce2b61106.green.build'
    },
    'BOSQUE_2':'',
    'BOSQUE_3':'',
    'BOSQUE_4':''
}

browser = webdriver.Firefox()
browser.get('https://ts4.lusobrasileiro.travian.com/login.php')
MAP_LOGINPAGE['txtUsername'] = get_element(MAP_LOGINPAGE['txtUsername'])
MAP_LOGINPAGE['txtPass'] = get_element(MAP_LOGINPAGE['txtPass'])

MAP_LOGINPAGE['txtUsername'].send_keys('SorcererBR')
MAP_LOGINPAGE['txtPass'].send_keys('VIDA157')

MAP_LOGINPAGE['btnLogin'] = get_element(MAP_LOGINPAGE['btnLogin'])
MAP_LOGINPAGE['btnLogin'].click()

browser.get(MAP_RESOURCES['BOSQUE_1']['URL'])
MAP_RESOURCES['BOSQUE_1']['UPGRADE_BTN'] = get_element(MAP_RESOURCES['BOSQUE_1']['UPGRADE_BTN'])
MAP_RESOURCES['BOSQUE_1']['UPGRADE_BTN'].click()