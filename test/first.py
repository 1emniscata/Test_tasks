import time
import datetime
import json
from selenium import webdriver


class QuerySet:
    """
    A class for carrying out a CRUD operation test for testing the endpoint "user".

    ...

    Attributes
    ----------
    id : int
        id of the user
    username : str
        username of the user
    firstname : str
        first name of the user
    lastname : str
        last name of the user
    email : str
        email of the user
    password : str
        password of the user
    phone : str
        phone of the user

    Methods
    -------
    go_to_site():
        Just goes to site.
    test_create():
        Checks if a brand new user can be created.
    test_read():
        Checks if a user can be got.
    test_login():
        Checks if a user can be logged in.
    test_update():
        Checks if a user can be updated.
    test_delete():
        Checks if a user can be deleted.
    close_browser(self):
        Just closes the browser.
    """
    start_time = datetime.datetime.now()

    def __init__(self, userid, username, firstname, lastname, email, password, phone):

        self.__id = userid
        self.__username = username
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.list_of_users = [self.__username]

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        # self.options.add_argument("--headless")

        self.browser = webdriver.Chrome(executable_path='/home/alex/test/chromedriver/chromedriver',
                                        options=self.options)
        self.site = 'https://petstore.swagger.io/'

    def go_to_site(self):
        """Just goes to site."""
        self.browser.get(self.site)
        print("I successfully got to the site")
        print('')
        self.browser.implicitly_wait(3)
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        self.browser.implicitly_wait(3)

    def test_create(self, userid=None, username=None, firstname=None, lastname=None, email=None,
                    password=None, phone=None):
        """
        Checks if a brand new user can be created.
        Prints that test passed successfully in case if the code of response == 200.
        """
        if username is not None:
            self.list_of_users.append(username)
        create_div = '/html/body/div[1]/section/div[2]/div[2]/div[4]/section/div/span[3]/div/' \
                     'div/div/span[8]/div/div'
        self.browser.find_element_by_xpath(create_div).click()
        # time.sleep(5)
        self.browser.implicitly_wait(3)

        try_button = '/html/body/div[1]/section/div[2]/div[2]/div[4]/section/div/span[3]/div/' \
                     'div/div/span[8]/div/div[2]/div/div[2]/div[1]/div[2]/button'
        self.browser.find_element_by_xpath(try_button).click()
        # time.sleep(2)
        self.browser.implicitly_wait(3)

        model_data_link = '/html/body/div[1]/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                          'div/div/div/span[8]/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr/' \
                          'td[2]/div[2]/div/div/textarea'
        model_data = self.browser.find_element_by_xpath(model_data_link)
        model_data_str_old = model_data.text
        model_data_json = json.loads(model_data_str_old)
        # print(model_data_json)
        fields_list = ["id", "username", "firstName", "lastName", "email", "password", "phone"]
        args_list = [self.__id, self.__username, self.__firstname, self.__lastname, self.__email,
                     self.__password, self.__phone]
        func_args = [userid, username, firstname, lastname, email, password, phone]
        # for i in range(len(fields_list)):
        #     model_data_json[fields_list[i]] = args_list[i]
        # for i, field in enumerate(fields_list):
        #     model_data_json[field] = args_list[i]
        # model_data_str_new = json.dumps(model_data_json, indent=2)

        for i, field in enumerate(fields_list):
            if func_args[i] is None:
                model_data_json[field] = args_list[i]
            else:
                model_data_json[field] = func_args[i]
        model_data_str_new = json.dumps(model_data_json, indent=2)

        # print(model_data_str_new)
        # time.sleep(3)
        self.browser.implicitly_wait(3)
        model_data.clear()
        model_data.send_keys(model_data_str_new)
        # time.sleep(3)
        self.browser.implicitly_wait(3)

        execute_button = '/html/body/div[1]/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                         'div/div/div/span[8]/div/div[2]/div/div[3]/button'
        self.browser.find_element_by_xpath(execute_button).click()
        # time.sleep(10)
        self.browser.implicitly_wait(3)

        code_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/div/' \
                    'div/span[8]/div/div[2]/div/div[4]/div[2]/div/div/table/tbody/tr/td[1]'
        code = self.browser.find_element_by_xpath(code_link).text
        if code == '200':
            print('---Test CREATE passed successfully')
            print(f'The user <{model_data_json[fields_list[1]]}> created')
            print('')
        elif code == '400':
            print(f'Invalid username supplied for <{model_data_json[fields_list[1]]}>')
            print('')
        elif code == '404':
            print(f'User <{model_data_json[fields_list[1]]}> not found')
            print('')

        # time.sleep(5)
        cancel_button_link = '/html/body/div[1]/section/div[2]/div[2]/div[4]/section/div/' \
                             'span[3]/div/div/div/span[8]/div/div[2]/div/div[2]/div[1]/' \
                             'div[2]/button'
        cancel_button = self.browser.find_element_by_xpath(cancel_button_link)
        cancel_button.click()

        close_create_div_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                                'div/div/div/span[8]/div/div[1]'
        close_create_div = self.browser.find_element_by_xpath(close_create_div_link)
        close_create_div.click()

    def test_read(self, username=None):
        """
        Checks if a user can be got.
        Prints that test passed successfully in case if the code of response == 200.
        """
        read_div = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/' \
                   'div/div/span[2]/div/div'
        self.browser.find_element_by_xpath(read_div).click()
        # time.sleep(5)
        self.browser.implicitly_wait(3)

        try_button = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/' \
                     'div/div/span[2]/div/div[2]/div/div[1]/div[1]/div[2]/button'
        self.browser.find_element_by_xpath(try_button).click()
        # time.sleep(2)
        self.browser.implicitly_wait(3)

        username_input_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                              'div/div/div/span[2]/div/div[2]/div/div[1]/div[2]/div/table/tbody/' \
                              'tr/td[2]/input'
        username_input = self.browser.find_element_by_xpath(username_input_link)
        username_input.click()
        username_input.clear()
        if username is None:
            username_input.send_keys(self.__username)
            username_for_print = self.__username
        else:
            username_input.send_keys(username)
            username_for_print = username
        # time.sleep(3)
        self.browser.implicitly_wait(3)

        execute_button = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/' \
                         'div/div/span[2]/div/div[2]/div/div[2]/button'
        self.browser.find_element_by_xpath(execute_button).click()
        # time.sleep(10)
        self.browser.implicitly_wait(3)

        code_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/div/div/' \
                    'span[2]/div/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]'
        code = self.browser.find_element_by_xpath(code_link).text
        # print(code)
        if code == '200':
            print('---Test READ passed successfully')
            print(f'The user <{username_for_print}> is accessible')
            print('')
        elif code == '400':
            print(f'Invalid username supplied for <{username_for_print}>')
            print('')
        elif code == '404':
            print('WARNING ' * 7)
            print('!!!Test READ failed')
            print(f'User <{username_for_print}> not found')
            # print('')
            print('WARNING ' * 7)
            print('')

        cancel_button_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                             'div/div/div/span[2]/div/div[2]/div/div[1]/div[1]/div[2]/button'
        cancel_button = self.browser.find_element_by_xpath(cancel_button_link)
        cancel_button.click()

        close_create_div_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                                'div/div/div/span[2]/div/div[1]'
        close_create_div = self.browser.find_element_by_xpath(close_create_div_link)
        close_create_div.click()

    def test_login(self):
        """
        Checks if a user can be logged in.
        Prints that test passed successfully in case if the code of response == 200.
        """
        # time.sleep(2)
        self.browser.implicitly_wait(3)
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        # time.sleep(2)
        self.browser.implicitly_wait(3)

        login_div = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/' \
                    'div/div/span[5]/div/div'
        self.browser.find_element_by_xpath(login_div).click()
        # time.sleep(5)
        self.browser.implicitly_wait(3)

        try_button = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/div/' \
                     'div/span[5]/div/div[2]/div/div[1]/div[1]/div[2]/button'
        self.browser.find_element_by_xpath(try_button).click()
        # time.sleep(2)
        self.browser.implicitly_wait(3)

        username_input_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                              'div/div/div/span[5]/div/div[2]/div/div[1]/div[2]/div/table/tbody/' \
                              'tr[1]/td[2]/input'
        username_input = self.browser.find_element_by_xpath(username_input_link)
        username_input.click()
        username_input.send_keys(self.__username)
        # time.sleep(3)
        self.browser.implicitly_wait(3)

        password_input_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                              'div/div/div/span[5]/div/div[2]/div/div[1]/div[2]/div/table/tbody/' \
                              'tr[2]/td[2]/input'
        password_input = self.browser.find_element_by_xpath(password_input_link)
        password_input.click()
        password_input.send_keys(self.__password)
        # time.sleep(3)
        self.browser.implicitly_wait(3)

        execute_button = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/' \
                         'div/div/span[5]/div/div[2]/div/div[2]/button'
        self.browser.find_element_by_xpath(execute_button).click()
        # time.sleep(10)
        self.browser.implicitly_wait(3)

        code_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/div/div/' \
                    'span[5]/div/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[1]'
        code = self.browser.find_element_by_xpath(code_link).text
        if code == '200':
            print('---Test LOGIN passed successfully')
        elif code == '400':
            print('Invalid username supplied')
        elif code == '404':
            print('User not found')

    def test_update(self, userid=None, username=None, firstname=None, lastname=None, email=None,
                    password=None, phone=None, other_username=None):
        """
        Checks if a user can be updated.
        Prints that test passed successfully in case if the code of response == 200.
        """
        update_div = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/div/' \
                     'div/span[3]/div/div'
        self.browser.find_element_by_xpath(update_div).click()
        # time.sleep(5)
        self.browser.implicitly_wait(3)

        try_button = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/div/' \
                     'div/span[3]/div/div[2]/div/div[2]/div[1]/div[2]/button'
        self.browser.find_element_by_xpath(try_button).click()
        # time.sleep(2)
        self.browser.implicitly_wait(3)

        username_input_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                              'div/div/div/span[3]/div/div[2]/div/div[2]/div[2]/div/table/tbody/' \
                              'tr[1]/td[2]/input'
        username_input = self.browser.find_element_by_xpath(username_input_link)
        username_input.click()
        # username_input.send_keys(self.__username)
        username_input.clear()
        if other_username is None:
            username_input.send_keys(self.__username)
            username_for_print = self.__username
        else:
            username_input.send_keys(other_username)
            username_for_print = other_username
        # time.sleep(3)
        self.browser.implicitly_wait(3)

        model_data_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/' \
                          'div/div/span[3]/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/' \
                          'td[2]/div[2]/div/div/textarea'
        model_data = self.browser.find_element_by_xpath(model_data_link)
        model_data_str_old = model_data.text
        model_data_json = json.loads(model_data_str_old)
        # print(model_data_json)
        fields_list = ["id", "username", "firstName", "lastName", "email", "password", "phone"]
        args_list = [self.__id, self.__username, self.__firstname, self.__lastname, self.__email,
                     self.__password, self.__phone]
        func_args = [userid, username, firstname, lastname, email, password, phone]
        for i, field in enumerate(fields_list):
            if func_args[i] is None:
                model_data_json[field] = args_list[i]
            else:
                model_data_json[field] = func_args[i]
        model_data_str_new = json.dumps(model_data_json, indent=2)
        # print(model_data_str_new)
        # time.sleep(3)
        self.browser.implicitly_wait(3)
        model_data.clear()
        model_data.send_keys(model_data_str_new)
        # time.sleep(3)
        self.browser.implicitly_wait(3)

        execute_button = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                         'div/div/div/span[3]/div/div[2]/div/div[3]/button'
        self.browser.find_element_by_xpath(execute_button).click()
        # time.sleep(10)
        self.browser.implicitly_wait(5)

        code_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/' \
                    'div/div/span[3]/div/div[2]/div/div[4]/div[2]/div/div/table/tbody/' \
                    'tr/td[1]'
        code = self.browser.find_element_by_xpath(code_link).text
        # print(code)
        self.browser.implicitly_wait(5)
        if code[:3] == '200':
            if username_for_print in self.list_of_users:
                print('---Test UPDATE passed successfully')
                print(f'The user <{username_for_print}> can be updated')
            else:
                print("---!!!Test UPDATE passed, but the user didn't exist before")
                print(f'The user <{username_for_print}> has been created')
            print('')
        elif code[:3] == '400':
            print(f'Invalid username supplied for <{username_for_print}>')
            print('')
        elif code[:3] == '404':  # What's the need in it there?
            print('WARNING ' * 7)
            print('!!!Test UPDATE failed')
            print(f'User <{username_for_print}> not found')
            # print('')
            print('WARNING ' * 7)
            print('')

        cancel_button_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                             'div/div/div/span[3]/div/div[2]/div/div[2]/div[1]/div[2]/button'
        cancel_button = self.browser.find_element_by_xpath(cancel_button_link)
        cancel_button.click()

        close_create_div_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/' \
                                'span[3]/div/div/div/span[3]/div/div[1]'
        close_create_div = self.browser.find_element_by_xpath(close_create_div_link)
        close_create_div.click()

    def test_delete(self, username=None):
        """
        Checks if a user can be deleted.
        Prints that test passed successfully in case if the code of response == 200.
        """
        delete_div = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                     'div/div/div/span[4]/div/div'
        self.browser.find_element_by_xpath(delete_div).click()
        # time.sleep(5)
        self.browser.implicitly_wait(3)

        try_button = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/div/' \
                     'div/span[4]/div/div[2]/div/div[2]/div[1]/div[2]/button'
        self.browser.find_element_by_xpath(try_button).click()
        # time.sleep(2)
        self.browser.implicitly_wait(3)

        username_input_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/' \
                              'div/div/div/span[4]/div/div[2]/div/div[2]/div[2]/div/table/tbody/' \
                              'tr/td[2]/input'
        username_input = self.browser.find_element_by_xpath(username_input_link)
        username_input.click()
        # username_input.send_keys(self.__username)
        username_input.clear()
        if username is None:
            username_input.send_keys(self.__username)
            username_for_print = self.__username
        else:
            username_input.send_keys(username)
            username_for_print = username
        # time.sleep(3)
        self.browser.implicitly_wait(3)

        execute_button = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/div/' \
                         'div/span[4]/div/div[2]/div/div[3]/button[1]'
        self.browser.find_element_by_xpath(execute_button).click()
        # time.sleep(10)
        self.browser.implicitly_wait(3)

        code_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/span[3]/div/div/div/' \
                    'span[4]/div/div[2]/div/div[4]/div[2]/div/div/table/tbody/tr/td[1]'
        code = self.browser.find_element_by_xpath(code_link).text
        if code[:3] == '200':
            print('---Test DELETE passed successfully')
            print(f'The user <{username_for_print}> can be deleted')
        elif code[:3] == '400':
            print('Invalid username supplied')
        elif code[:3] == '404':

            print('WARNING ' * 7)
            print('!!!Test DELETE failed')
            print(f'User <{username_for_print}> not found')
            # print('')
            print('WARNING ' * 7)
        print('')

        cancel_button_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/' \
                             'span[3]/div/div/div/span[4]/div/div[2]/div/div[2]/div[1]/' \
                             'div[2]/button'
        cancel_button = self.browser.find_element_by_xpath(cancel_button_link)
        cancel_button.click()

        close_create_div_link = '/html/body/div/section/div[2]/div[2]/div[4]/section/div/' \
                                'span[3]/div/div/div/span[4]/div/div[1]'
        close_create_div = self.browser.find_element_by_xpath(close_create_div_link)
        close_create_div.click()

    def close_browser(self):
        """Just closes the browser."""
        self.browser.close()
        self.browser.quit()
        finish_time = datetime.datetime.now()
        print('-' * 40)
        print('Spent time:', finish_time-self.start_time)
        # print("I closed Chrome browser")


first_test = QuerySet(1, '1emniscata', 'Alex', 'Suzen', 'alex@gmail.com', '123', '12345')
first_test.go_to_site()
first_test.test_create()
first_test.test_create(3, 'person', 'Kolya', 'Ivanov', 'koly@gmail.com', '456', '45678')
first_test.test_read()
first_test.test_read('person')
first_test.test_read('rrr')
# first_test.test_login()
first_test.test_update(userid=2, lastname='AAA')
first_test.test_update(userid=4, lastname='BBB', other_username='person')
first_test.test_update(userid=5, username='no', lastname='CCC', other_username='no')
first_test.test_delete()
first_test.test_delete(username='1emniscata')
first_test.test_delete(username='person')
first_test.test_read()  # Still possible to get "1emniscata"
first_test.test_read('person')
first_test.close_browser()
