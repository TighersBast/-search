from base.base_driver import init_driver
from page.page import Page

import pytest

class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("keyword", ["xiaoming"])
    def test_search(self, keyword):
        self.page.setting.click_search()
        self.page.search.input_search(keyword)
        self.page.search.click_back()

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_hello1(self):
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_hello2(self):
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_hello3(self):
        assert 1