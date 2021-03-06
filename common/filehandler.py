# -- encoding: utf-8 --
# @time:    	2021/1/12 23:49
# @Author: 		jsonLiu
# @Email:  		810030709@qq.com
# @file: 		filehandler
import os


class FileHandler:
    base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    log_path = os.path.join(base_path, r'result\log')

    screenshot_path = os.path.join(base_path, r'result\screenshot')

    testcase_path = os.path.join(base_path, 'testCases')

    report_path = os.path.join(base_path, r'result\reports')

    config_path = os.path.join(base_path, 'Config')


if __name__ == '__main__':
    print(FileHandler.report_path)
    print(FileHandler.config_path)
