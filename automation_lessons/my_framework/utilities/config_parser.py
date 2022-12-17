import configparser

abs_path = '/home/denis/Python/Projects/hillel_qa_automation_160922/automation_lessons/less2/configurations/configuration.ini'
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def reset_password_page_url():
        return config.get('app_info', 'reset_password_page_url')

    @staticmethod
    def get_login():
        return config.get('user_data', 'login')

    @staticmethod
    def get_password():
        return config.get('user_data', 'password')

    @staticmethod
    def get_browser_id():
        return config.get('browser_data', 'browser_id')
