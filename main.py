import os

from dotenv import load_dotenv, find_dotenv

from names import unique_name, super_names, top_name
from data import basic_data_dict
from api_yandex import YandexDisk


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    #
    # data_dict = basic_data_dict()
    #
    # print(unique_name(data_dict['mentors']))
    # print(super_names(data_dict['mentors'], data_dict['courses']))
    # print(top_name(data_dict['mentors']))
    #
    # yd = YandexDisk(os.getenv('ACCESS_TOKEN_YD'))
    #
    # print(yd.get_upload('name_folder'))
    # print(yd.get_folder_info('name_folder'))
