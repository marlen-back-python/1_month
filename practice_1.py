'''EASTERN ANIMAL CALENDAR 1900-2079'''
print()
print('"EASTERN ANIMAL CALENDAR 1900-2079"')

rat=(1900,1912,1924,1936,1948,1960,1972,1984,1996,2008,2020,2032,2044,2056,2068)
ox=(1901,1913,1925,1937,1949,1961,1973,1985,1997,2009,2021,2033,2045,2057,2069)
tiger=(1902,1914,1926,1938,1950,1962,1974,1986,1998,2010,2022,2034,2046,2058,2070)
rabbit=(1903,1915,1927,1939,1951,1963,1975,1987,1999,2011,2023,2035,2047,2059,2071)
dragon=(1904,1916,1928,1940,1952,1964,1976,1988,2000,2012,2024,2036,2048,2060,2072)
snake=(1905,1917,1929,1941,1953,1965,1977,1989,2001,2013,2025,2037,2049,2061,2073)
horse=(1906,1918,1930,1942,1954,1966,1978,1990,2002,2014,2026,2038,2050,2062,2074)
sheep_goat=(1907,1919,1931,1943,1955,1967,1979,1991,2003,2015,2027,2039,2051,2063,2075)
monkey=(1908,1920,1932,1944,1956,1968,1980,1992,2004,2016,2028,2040,2052,2064,2076)
rooster=(1909,1921,1933,1945,1957,1969,1981,1993,2005,2017,2029,2041,2053,2065,2077)
dog=(1910,1922,1934,1946,1958,1970,1982,1994,2006,2018,2030,2042,2054,2066,2078)
boar_pig=(1911,1923,1935,1947,1959,1971,1983,1995,2007,2019,2031,2043,2055,2067,2079)

for i in range(3):
    year_of_birth = int(input('Enter your year of birth: '))
    if year_of_birth in rat:
        print('According to the eastern calendar you are - Rat')

    elif year_of_birth in ox:
        print('According to the eastern calendar you are - Ox')
    elif year_of_birth in tiger:
        print('According to the eastern calendar you are - Tiger')
    elif year_of_birth in rabbit:
        print('According to the eastern calendar you are - Rabbit')
    elif year_of_birth in dragon:
        print('According to the eastern calendar you are - Dragon')
    elif year_of_birth in snake:
        print('According to the eastern calendar you are - Snake')
    elif year_of_birth in horse:
        print('According to the eastern calendar you are - Horse')
    elif year_of_birth in sheep_goat:
        print('According to the eastern calendar you are - Sheep & Goat')
    elif year_of_birth in monkey:
        print('According to the eastern calendar you are - Monkey')
    elif year_of_birth in rooster:
        print('According to the eastern calendar you are - Rooster')
    elif year_of_birth in dog:
        print('According to the eastern calendar you are - Dog')
    elif year_of_birth in boar_pig:
        print('According to the eastern calendar you are - Boar & Pig')

    else:
        print('ONLY 1900-2079!!!')
