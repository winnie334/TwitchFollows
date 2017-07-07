from selenium import webdriver
import pickle


if __name__ == '__main__':
	url = 'https://www.twitchfollows.com/login'
	driver = webdriver.Chrome(executable_path=r'C:\Users\winnie33\Downloads\chromedriver_win32\chromedriver.exe')
	driver.get(url)


"""
<button onclick="AjaxLoader('Offer4618', 'func', 'new_follow', '&amp;offer=4618&amp;streamer=duckbit1');"
class="btn btn-pink btn-lg">Follow &nbsp;(+25 <i class="fa fa-database" title="Credits"></i>)</button>
"""