from selenium.webdriver.common.by import By
import logging
import utilities.customlogger as cl
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from datetime import date
import time

class SeleniumDriver:
    log = cl.customLogger(logLevel=logging.INFO)

    def __init__(self,driver):
        self.driver = driver

    def getBytype(self,locatortype):
        locator = locatortype.lower()
        if locator == "id":
            return By.ID
        elif locator == "name":
            return By.NAME
        elif locator == "linktext":
            return By.LINK_TEXT
        elif locator == "partiallinktext":
            return By.PARTIAL_LINK_TEXT
        elif locator == "css":
            return By.CSS_SELECTOR
        elif locator == "classname":
            return By.CLASS_NAME
        elif locator == "xpath":
            return By.XPATH
        else:
            self.log.error("Please enter the valid locator :"+locatortype)
            return False

    def getWebElement(self,loctorvalue, locatortype="xpath/id"):
        element = None
        try:
            bytype = self.getBytype(locatortype)
            element = self.driver.find_element(bytype, loctorvalue)
            self.log.info("Identified element with locator type "
                        ""+locatortype+" with locator value "+loctorvalue)
        except Exception as e:
            self.log.error("Element not identified with locator type "
                                  "" + locatortype + " with locator value " + loctorvalue + str(e))
        return element

    def getWebElements(self, loctorvalue, locatortype="xpath/id"):
        listofelements = []
        try:
            bytype = self.getBytype(locatortype)
            listofelements = self.driver.find_elements(bytype, loctorvalue)
            self.log.info("Identified elements with locator type "
                "" + locatortype + " with locator value " + loctorvalue)
        except Exception as e:
            self.log.error("Elements are not found " + str(e))
        return listofelements

    def geturl(self,url):
        self.driver.get(url)
        self.log.info("Entered url "+url)

    def closewindow(self):
        self.log.info("Window closed")
        self.driver.close()

    def quitwindow(self):
        self.log.info("All windows closed")
        self.driver.quit()

    def maximizewindow(self):
        self.log.info("Window maximized")
        self.driver.maximize_window()

    def minimizewindow(self):
        self.log.info("Window minimized")
        self.driver.minimize_window()

    def setwindowsizeorposition(self,x,y,alter="size/position"):
        if alter == "size":
            self.driver.set_window_size(x,y)
            self.log.info("Setted window size to "+x +"and "+y)
        elif alter == "position":
            self.driver.set_window_position(x,y)
            self.log.info("Setted window position to " + x + "and " + y)
        else:
            self.log.error("Please enter the vaid size or position")

    def browsernatives(self,native = "back"):
        if native == "back":
            self.driver.back()
            self.log.info("Clicked on browser native back")
        elif native == "forward":
            self.driver.forward()
            self.log.info("Clicked on browser native forward")
        elif native == "refresh":
            self.driver.refresh()
            self.log.info("Clicked on browser native refresh")
        else:
            self.log.error("Please enter the valid native "
                           "list back/forward/refresh "+native)

    def getsourcecode(self):
        pagesource = self.driver.page_source
        self.log.info("Obtained page source is " + pagesource)
        return pagesource

    def getcurrenturl(self):
        current_url = self.driver.current_url
        self.log.info("Obtained current url is " + current_url)
        return current_url

    def gettitle(self):
        title = self.driver.title
        self.log.info("Obtained current title is " + title)
        return title

    def click(self,locatorvalue,locatortype):
        try:
            element = self.getWebElement(locatorvalue,locatortype)
            element.click()
            self.log.info("Click on webement with locator type "
                          +locatortype+ "locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to click on webelement with "
                           "locator type"+locatortype+" locator value "
                           +locatorvalue+" "+str(e))

    def senddata(self,locatorvalue,locatortype,data):
        try:
            element = self.getWebElement(locatorvalue,locatortype)
            element.send_keys(data)
            self.log.info("Entered data on webement with locator type "
                          +locatortype+ "locator value "+locatorvalue+" "+"data = "+data)
        except Exception as e:
            self.log.error("Unable to enter the data on webelement with "
                           "locator type"+locatortype+" locator value "
                           +locatorvalue+" "+str(e))
            raise Exception

    def getText(self,locatorvalue,locatortype):
        text = None
        try:
            element = self.getWebElement(locatorvalue,locatortype)
            text = element.text
            self.log.info("Got text from webement with locator type "
                          +locatortype+ "locator value "+locatorvalue+" "+"text = "+text)
        except Exception as e:
            self.log.error("Unable to get text from webelement with "
                           "locator type"+locatortype+" locator value "
                           +locatorvalue+" "+str(e))
        return text

    def selectoptionindrpdwn(self,locatorvalue,locatortype,option="India"):
        try:
            element = self.getWebElement(locatorvalue, locatortype)
            sel = Select(element)
            sel.select_by_visible_text(option)
            self.log.info("selcted text from drop down with locator type "
                          + locatortype + "locator value " + locatorvalue + " " + "option = " + option)
        except Exception as e:
            self.log.error("Unable to select option from drp dwn with "
                           "locator type" + locatortype + " locator value "
                           + locatorvalue + " " + str(e))

    def deselectoptionindrpdwn(self,locatorvalue,locatortype,option="India"):
        try:
            element = self.getWebElement(locatorvalue, locatortype)
            sel = Select(element)
            sel.deselect_by_visible_text(option)
            self.log.info("deselcted text from drop down with locator type "
                          + locatortype + "locator value " + locatorvalue + " " + "option = " + option)
        except Exception as e:
            self.log.error("Unable to deselect option from drp dwn with "
                           "locator type" + locatortype + " locator value "
                           + locatorvalue + " " + str(e))

    def deselectall(self,locatorvalue,locatortype):
        try:
            element = self.getWebElement(locatorvalue, locatortype)
            sel = Select(element)
            sel.deselect_all()
            self.log.info("deselected all options from drop down with locator type "
                          + locatortype + "locator value " + locatorvalue + "")
        except Exception as e:
            self.log.error("Unable to deselect all options from drp dwn with "
                           "locator type" + locatortype + " locator value "
                           + locatorvalue + " " + str(e))

    def getfirstselectedoption(self,locatorvalue,locatortype):
        text = None
        try:
            element = self.getWebElement(locatorvalue, locatortype)
            sel = Select(element)
            text = sel.first_selected_option.text
            self.log.info("Got first selected option from drop down with locator type "
                          + locatortype + "locator value " + locatorvalue + " " + "text = " + text)
        except Exception as e:
            self.log.error("Unable to obtain first selected option from drp dwn with "
                           "locator type" + locatortype + " locator value "
                           + locatorvalue + " " + str(e))
        return text

    def mouseover(self,locatorvalue,locatortype):
        try:
            act = ActionChains(self.driver)
            element = self.getWebElement(locatorvalue, locatortype)
            act.move_to_element(element).perform()
            self.log.info("Mouse overed on element with locator type "
                          + locatortype + "locator value " + locatorvalue + "")
        except Exception as e:
            self.log.error("Unable to Mouse over on element with "
                           "locator type" + locatortype + " locator value "
                           + locatorvalue + " " + str(e))

    def leftmouseclick(self,locatorvalue,locatortype):
        try:
            act = ActionChains(self.driver)
            element = self.getWebElement(locatorvalue, locatortype)
            act.move_to_element(element).click().perform()
            self.log.info("Mouse overed on element and clicked with locator type "
                          + locatortype + "locator value " + locatorvalue + "")
        except Exception as e:
            self.log.error("Unable to Mouse over on element and click with "
                           "locator type" + locatortype + " locator value "
                           + locatorvalue + " " + str(e))

    def scrolltoptobottom(self,x=0,y=1000):
        self.driver.execute_script("window.scrollBy("+str(x)+","+str(y)+");")
        self.log.info("Scrolled the page from top to bottom "+str(x)+ " "+str(y))

    def scrollbottomtotop(self,x=0,y=-500):
        self.driver.execute_script("window.scrollBy("+str(x)+","+str(y)+");")
        self.log.info("Scrolled the page from bottom to top "+str(x)+ " "+str(y))

    def switchtoframe(self,id=None,index=0):
        try:
            if id is not None:
                self.driver.switch_to.frame(id)
                self.log.info("Switched into the frame with id "+id)
            else:
                self.driver.switch_to.frame(index)
                self.log.info("Swicted into the frame with index "+index)
        except Exception as e:
            self.log.error("Unable to switch to frame "+str(e))

    def switchtoparentframe(self):
        self.driver.switch_to.parent_frame()


    def waitforelementclickable(self,locatorvalue,locatortype,time=60,poll=10):
        try:
            bytype = self.getBytype(locatortype)
            wait = WebDriverWait(self.driver, time, poll_frequency=poll,
                                 ignored_exceptions=[NoSuchElementException,
                                            ElementNotInteractableException])
            wait.until(EC.element_to_be_clickable((
                bytype, locatorvalue)))
            self.log.info("Waited for element to be clicked")
        except Exception as e:
            self.log.error("Waited for element to be clicked time = "+str(time)+" But unsccuessfull")

    def hardwait(self):
        time.sleep(5)

    def waitforvlisbleofelement(self,locatorvalue,locatortype,time=60,poll=10):
        try:
            self.hardwait()
            bytype = self.getBytype(locatortype)
            wait = WebDriverWait(self.driver, time, poll_frequency=poll,
                                 ignored_exceptions=[NoSuchElementException,
                                            ElementNotInteractableException])
            wait.until(EC.visibility_of((
                bytype, locatorvalue)))
            self.log.info("Waited for visble of element")
        except Exception as e:
            self.log.error("Waited for element to be visible time = "+str(time)+" But unsccuessfull")



    def elementisselcted(self,locatorvalue,locatortype):
        element = self.getWebElement(locatorvalue, locatortype)
        return element.is_selected()

    def elementisenabled(self, locatorvalue, locatortype):
        element = self.getWebElement(locatorvalue, locatortype)
        return element.is_enabled()

    def elementisdisplayed(self, locatorvalue, locatortype):
        element = self.getWebElement(locatorvalue, locatortype)
        return element.is_displayed()

    def getcurrentwindowid(self):
        currentwindowid = self.driver.current_window_handle
        self.log.info("Obtained window id = "+currentwindowid)
        return currentwindowid

    def getallwindowids(self):
        allwindowids = self.driver.window_handles
        self.log.info("Obtained all window ids = " + allwindowids)
        return allwindowids

    def switchtowindow(self,windowid):
        self.driver.switch_to.window(windowid)
        self.log.info("Switched into window with window id = "+windowid)


    def switchtoJSpopup(self,action="accept/dismiss"):
        if action == "accept":
            self.driver.switch_to.alert.accept()
            self.log.info("Clicked on OK button")
        elif action == "dismiss":
            self.driver.switch_to.alert.dismiss()
            self.log.info("Clicked on CANCEL button")
        else:
            self.log.error("Please provide the valid action")

    def gettextfromJSpopup(self):
        return self.driver.switch_to.alert.text

    def getcurrentdate(self):
        today = date.today()
        currentdate = today.strftime("%d")
        self.log.info("Current date is "+currentdate)
        return currentdate

    def getcurrentdateandtime(self):
        today = date.today()
        currentdateandtime = today.strftime("YYYY_MM_DDHH_MI_Sec")
        self.log.info("Current date is "+currentdateandtime)
        return currentdateandtime

    def getscreenshot(self,message):
        try:
            self.driver.save_screenshot(message+"_"+str(self.getcurrentdateandtime())+".png")
        except Exception as e:
            self.log.error("Unable to capure screen shot" +str(e))
            raise Exception
