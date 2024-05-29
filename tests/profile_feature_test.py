from base.base_test import BAseTest
import allure
import pytest


@allure.feature("Profile Functionality")
class TestProfileFeature(BAseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def best_charge_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)

