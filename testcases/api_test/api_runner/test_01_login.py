import pytest
import allure
from operation.user import login_user
from testcases.conftest import api_data
from common.project_path import api_root_url
from common.logger import logger
# from common.CopyFiles import CopyFiles

@allure.step("步骤1 ==>> 登录用户")
def step_1(username):
    logger.info("步骤1 ==>> 登录用户：{}".format(username))


@allure.tag(api_root_url + "/api/auth/login")
@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户登录模块")
class TestUserLogin():

    # @allure.story("这是用户故事")
    @allure.title("用例--登录用户")
    @allure.description("接口请求地址:" + api_root_url + "/api/auth/login")
    @pytest.mark.parametrize("username, password, except_result, except_code, except_msg",
                             api_data["test_login_user"])
    @pytest.mark.test1
    def test_login_user(self, username, password, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = login_user(username, password)
        step_1(username)
        # assert result.response.status_code == except_code
        # assert result.success == except_result, result.error
        assert result.json().get("code") == except_code, "接口返回码是 【 {} 】, 返回信息：{} ".format(result.json()["code"],
                                                                                          result.json()["msg"])
        assert result.json()["msg"] in except_msg, "接口返回码是 【 {} 】, 返回信息：{} ".format(result.json()["code"],
                                                                                    result.json()["msg"])
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        # assert except_msg in result.msg


if __name__ == '__main__':
    pytest.main(["-q", "test_01_login.py"])
# CopyFiles().EvromentConfig()
