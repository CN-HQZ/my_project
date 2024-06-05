from city_functions import city_country

def test_city_country():
    """测试是否输出样式为 'City Country'"""
    gettest = city_country('santiago', 'chile')
    assert gettest == 'santiago chile'


def test_city_country_population():
    gettest = city_country('santiago', 'chile', '5000000')
    assert gettest == 'santiago chile -population 5000000'