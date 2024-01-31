import pytest
from data import basic_data_dict
from names import unique_name, super_names, top_name


@pytest.mark.parametrize(
    'mentors_, expected', [
        [basic_data_dict()['mentors'], 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)']
    ]
)
def test_top_name(mentors_, expected):
    result = top_name(basic_data_dict()['mentors'])
    assert result == expected


@pytest.mark.parametrize(
    'mentors_, expected', [
        [basic_data_dict()['mentors'],
         'На курсах Python-разработчик с нуля и Java-разработчик с нуля преподают: Антон, Евгений, Максим']
    ]
)
def test_super_names(mentors_, expected):
    result = super_names(basic_data_dict()['mentors'], basic_data_dict()['courses'])
    assert result == expected


@pytest.mark.parametrize(
    'mentors_, expected', [
        [basic_data_dict()['mentors'], 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей,'
                                       ' Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий,'
                                       ' Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита,'
                                       ' Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар,'
                                       ' Юрий']
    ]
)
def test_unique_name(mentors_, expected):
    result = unique_name(mentors_)
    assert result == expected
