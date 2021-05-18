import datetime
import sys
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import ElementClickInterceptedException


class Converter:
    """
    A class for carrying out a CRUD operation test for testing the endpoint "user".

    ...

    Attributes
    ----------

    Methods
    -------
    go_to_site():
       Just goes to site.
    celsius_to_fahrenheit(value=None):
        Just converts Celsius to Fahrenheit temperature.
    meters_to_feet(value=None):
        Just converts meters to feet.
    ounces_to_grams(value=None):
        Just converts ounces to grams.
    close_browser(self):
       Just closes the browser.
   """

    start_time = datetime.datetime.now()

    def __init__(self):

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        # self.options.add_argument("--headless")

        self.browser = webdriver.Chrome(executable_path='/home/alex/test/chromedriver/chromedriver',
                                        options=self.options)
        self.__site = 'https://www.metric-conversions.org/'

    def go_to_site(self):
        """Just goes to site."""

        self.browser.get(self.__site)
        print(f"I successfully got to the site {self.__site}")
        print('')
        self.browser.implicitly_wait(3)
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        self.browser.implicitly_wait(3)

    def check_value(self, value):
        if type(value) not in (int, float, None):
            return False
        else:
            return True

    def celsius_to_fahrenheit(self, value=None):
        """Just converts Celsius to Fahrenheit temperature."""

        try:
            celsius_div_link = '/html/body/div[1]/div[5]/a[3]'
            celsius_div = self.browser.find_element_by_xpath(celsius_div_link).get_attribute('href')
            # celsius_div.click()
            self.browser.get(celsius_div)

            cel_input_link = '/html/body/div[1]/div[1]/section[1]/form/input[1]'
            cel_input = self.browser.find_element_by_xpath(cel_input_link)
            cel_input.click()
            cel_input.clear()
            if value:
                if self.check_value(value):
                    cel_input.send_keys(value)
                else:
                    print('Testing of conversion: Celsius to Fahrenheit temperature')
                    print(f'Incorrect value "{value}". You have to use only numbers.')
                    print('')
                    self.browser.get(self.__site)
                    return None
            else:
                cel_input.send_keys(1)

            output_link = '/html/body/div[1]/div[1]/section[2]/p[1]'
            output = self.browser.find_element_by_xpath(output_link).text
            print('Testing of conversion: Celsius to Fahrenheit temperature')
            print(output)
            print('')

            self.browser.get(self.__site)
        except (NoSuchElementException, InvalidSelectorException, InvalidArgumentException,
                ElementClickInterceptedException):
            print('!!! ERROR !!!')
            err_type, err_value, err_trace = sys.exc_info()
            print(err_type)
            print(err_value, end='')
            traceback.print_tb(err_trace, limit=1, file=sys.stdout)
            print('!!! ERROR !!!')
            print('')

    def meters_to_feet(self, value=None):
        """Just converts meters to feet."""

        try:
            meters_div_link = '/html/body/div[1]/div[5]/a[9]'
            meters_div = self.browser.find_element_by_xpath(meters_div_link).get_attribute('href')
            # celsius_div.click()
            self.browser.get(meters_div)

            met_input_link = '/html/body/div[1]/div[1]/section[1]/form/input[1]'
            met_input = self.browser.find_element_by_xpath(met_input_link)
            met_input.click()
            met_input.clear()
            if value:
                if self.check_value(value):
                    met_input.send_keys(value)
                else:
                    print('Testing of conversion: meters to feet')
                    print(f'Incorrect value "{value}". You have to use only numbers.')
                    print('')
                    self.browser.get(self.__site)
                    return None
            else:
                met_input.send_keys(1)

            select_div_link = '/html/body/div[1]/div[1]/section[2]/div[2]/select'
            select_div = self.browser.find_element_by_xpath(select_div_link)
            select_div.click()
            decimal_option_link = '/html/body/div[1]/div[1]/section[2]/div[2]/select/option[2]'
            decimal_option = self.browser.find_element_by_xpath(decimal_option_link)
            decimal_option.click()

            output_link = '/html/body/div[1]/div[1]/section[2]/p[1]'
            output = self.browser.find_element_by_xpath(output_link).text
            print('Testing of conversion: meters to feet')
            print(output)
            print('')

            self.browser.get(self.__site)
        except (NoSuchElementException, InvalidSelectorException, InvalidArgumentException,
                ElementClickInterceptedException):
            print('!!! ERROR !!!')
            err_type, err_value, err_trace = sys.exc_info()
            print(err_type)
            print(err_value, end='')
            traceback.print_tb(err_trace, limit=1, file=sys.stdout)
            print('!!! ERROR !!!')
            print('')

    def ounces_to_grams(self, value=None):
        """Just converts ounces to grams."""

        try:
            main_input_link = '/html/body/div[1]/section[1]/form/p/input[1]'
            main_input = self.browser.find_element_by_xpath(main_input_link)
            # main_input.click()
            main_input.clear()
            main_input.send_keys('o')

            ounces_input_link = '/html/body/div[1]/section[2]/div/ol/li[1]/div/input'
            ounces_input = self.browser.find_element_by_xpath(ounces_input_link)
            ounces_input.click()
            ounces_input.clear()
            if value:
                if self.check_value(value):
                    ounces_input.send_keys(value)
                else:
                    print('Testing of conversion: ounces to grams')
                    print(f'Incorrect value "{value}". You have to use only numbers.')
                    print('')
                    self.browser.get(self.__site)
                    return None
            else:
                ounces_input.send_keys(1)
            ounces_input.send_keys(Keys.ENTER)

            output_link = '/html/body/div[1]/div[1]/section[2]/p[1]'
            output = self.browser.find_element_by_xpath(output_link).text
            print('Testing of conversion: ounces to grams')
            print(output)
            print('')

            self.browser.get(self.__site)
        except (NoSuchElementException, InvalidSelectorException, InvalidArgumentException,
                ElementClickInterceptedException):
            print('!!! ERROR !!!')
            err_type, err_value, err_trace = sys.exc_info()
            print(err_type)
            print(err_value, end='')
            traceback.print_tb(err_trace, limit=1, file=sys.stdout)
            print('!!! ERROR !!!')
            print('')

    def close_browser(self):
        """Just closes the browser."""

        self.browser.close()
        self.browser.quit()
        finish_time = datetime.datetime.now()
        print('-' * 40)
        print('Spent time:', finish_time - self.start_time)
        # print("I closed Chrome browser")


if __name__ == '__main__':
    first_test = Converter()
    first_test.go_to_site()
    first_test.celsius_to_fahrenheit()
    first_test.meters_to_feet('f')
    first_test.ounces_to_grams()
    first_test.celsius_to_fahrenheit(100)
    first_test.celsius_to_fahrenheit('f')
    first_test.ounces_to_grams(20)
    first_test.ounces_to_grams('f')
    first_test.meters_to_feet(10)
    first_test.close_browser()
