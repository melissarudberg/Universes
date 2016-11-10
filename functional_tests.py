# My computer history web site as an example

# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if os.name=='nt':
            self.browser = webdriver.Chrome()
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    #####################
    # END OF BOILER PLATE
    #####################

    def test_home_page(self):
        """

        Stephen Hawking’s theory of “The Big Bang Theory,” an event dating
        back 15 billion years, does not preclude genesis. “The Big Bang
        Theory’s” explosive origin of the universe does not, however,
        easily conform to the notion of a God created world. Moreover,
        according to “The Big Bang Theory”, the Universe is continuously
        expanding, whereas Genesis is ongoing. According to concrete scientific
        evidence, Einstein’s relativity theory, E=Mc^2 (Aviezer), posits the
        possibility of other Universes similar to our own. Genesis might also
        represent a metaphoric shorthand for evolving scientific inquiry.
        Furthermore, this research attempts to understand the complex and
        vague idea of multiple universes and where they begin to exist as
        individual entities.   

        """

        self.browser.get('http://localhost:8000/index.html')

        # there is a page title defined by <title></title> on the home page
        # check it

        self.assertIn('The Big Bang',self.browser.title)

        # You will have an image for your home page I am assuming.
        # Put the name of your image here in place of homebrew.png
        # In general this is how we check for images on a page.

        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('journeytolighthouse.jpg',m.get_attribute('src'))

        # We check here for the title of your home page.
        # uncomment the next lines and change the text when you set your title.
        # put your title in place of "The Title of My Home Page"

        h=self.browser.find_element_by_css_selector('h1')
        self.assertIn("The Big Bang",h.text)

        # There is an area specified around the computer keyboard.
        # the 'id' of this area is 'keyboard'

        # this is how we find that area.
        a=self.browser.find_element_by_id('keyboard')

        # this is how we click on it.
        a.click()

        # after clicking on it, we should see the next page.
        e=self.browser.find_element_by_css_selector("h1")
        self.assertIn('Keyboards',e.text)

        # The page should have a picture of a teletype machine. 
        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('teletype.jpg',m.get_attribute('src'))
    

if __name__=="__main__":
        unittest.main(warnings="ignore")
