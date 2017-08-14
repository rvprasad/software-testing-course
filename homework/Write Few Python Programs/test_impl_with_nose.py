import impl
import nose


def test_anagram_check_success():
    nose.tools.assert_true(impl.anagram_check('Madam Curie', 'Radium came'))
    nose.tools.assert_true(impl.anagram_check('Who came', 'How mace'))
    
    nose.tools.assert_true(impl.anagram_check('his malt', 'salt him'))
    
    nose.tools.assert_true(impl.anagram_check('god', 'dog'))
    nose.tools.assert_true(impl.anagram_check('evil', 'live'))
    nose.tools.assert_true(impl.anagram_check('mace', 'came'))
    
    nose.tools.assert_true(impl.anagram_check('who ever', 'however'))


def test_anagram_check_for_invalid_words():
    nose.tools.assert_false(impl.anagram_check('collapse', 'lapsecol'))
    
    nose.tools.assert_false(impl.anagram_check('collapse', 'laps cole'))
    
    nose.tools.assert_false(impl.anagram_check('karaoke singing', 'ring soaking kae'))
    nose.tools.assert_false(impl.anagram_check('life time', 'meet fili'))

    nose.tools.assert_false(impl.anagram_check("fall", "llaf")) # ??
    
    
def test_anagram_check_not_permutation():
    nose.tools.assert_false(impl.anagram_check('really', 'leary'))
    
    nose.tools.assert_false(impl.anagram_check('collapse', 'elapsed'))
    
    nose.tools.assert_false(impl.anagram_check('life time', 'meet file'))
    

def test_anagram_for_None1():
    flag1 = False
    flag2 = False
    try:
        flag2 = not impl.anagram_check(None, '')
    except ValueError: # What can go wrong without specific exception type?
        flag1 = True
    assert flag1 or flag2   # Using assert 


def test_anagram_for_None2():
    flag1 = False
    flag2 = False
    try:
        flag2 = not impl.anagram_check('', None)
    except ValueError:
        flag1 = True
    nose.tools.assert_true(flag1 or flag2)


def test_anagram_for_None3():
    flag1 = False
    flag2 = False
    try:
        flag2 = not impl.anagram_check(None, None)
    except ValueError:
        flag1 = True
    nose.tools.assert_true(flag1 or flag2)
    

def test_anagram_for_invalid_type1():
    flag1 = False
    flag2 = False
    try:
        flag2 = not impl.anagram_check(1234, '')
    except ValueError:
        flag1 = True
    nose.tools.assert_true(flag1 or flag2)


def test_anagram_for_invalid_type2():
    flag1 = False
    flag2 = False
    try:
        flag2 = not impl.anagram_check('', 1234)
    except ValueError:
        flag1 = True
    nose.tools.assert_true(flag1 or flag2)


def test_anagram_for_invalid_type3():
    flag1 = False
    flag2 = False
    try:
        flag2 = not impl.anagram_check(1234, 1234)
    except ValueError:
        flag1 = True
    nose.tools.assert_true(flag1 or flag2)


NAME = "Harry"
PHONE = 7855326350
EMAIL = "harry@ksu.edu"
URL = "http://ksu.edu/~harry"
URL = "http://www.microsoft.com/~harry"
URL = "http://127.1.1.0"


def test_shopinfo_for_all_valid1():
    tmp1 = impl.ShopInfo(NAME, PHONE, EMAIL, URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    assert tmp1.get_website() == URL  # Using assert 


def test_shopinfo_for_all_valid2():
    email = "john.doe@example.com"
    tmp1 = impl.ShopInfo(NAME, PHONE, email, URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_equal(tmp1.get_email(), email)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_for_all_valid3():
    url = "http://1.2.3.4/what/"
    tmp1 = impl.ShopInfo(NAME, PHONE, EMAIL, url)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_equal(tmp1.get_website(), url)


def test_shopinfo_name_for_invalid_value1():
    tmp1 = impl.ShopInfo("1234", PHONE, EMAIL, URL)
    nose.tools.assert_raises(ValueError, tmp1.get_name)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_name_for_invalid_value2():
    tmp1 = impl.ShopInfo("", PHONE, EMAIL, URL)
    nose.tools.assert_raises(ValueError, tmp1.get_name)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_name_for_invalid_value3():
    tmp1 = impl.ShopInfo(None, PHONE, EMAIL, URL)
    nose.tools.assert_raises(ValueError, tmp1.get_name)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_name_for_invalid_value4():
    name = "Seven-11"
    tmp1 = impl.ShopInfo(name, PHONE, EMAIL, URL)
    nose.tools.assert_raises(ValueError, tmp1.get_name)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_name_for_invalid_type():
    tmp1 = impl.ShopInfo(1234, PHONE, EMAIL, URL)
    nose.tools.assert_raises(ValueError, tmp1.get_name)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shoipinfo_phone_for_invalid_value1():
    tmp1 = impl.ShopInfo(NAME, -7855326350, EMAIL, URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_raises(ValueError, tmp1.get_phone)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shoipinfo_phone_for_invalid_value2():
    tmp1 = impl.ShopInfo(NAME, 0, EMAIL, URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_raises(ValueError, tmp1.get_phone)
    nose.tools.assert_equal(tmp1.get_email(),  EMAIL)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shoipinfo_phone_for_invalid_value3():
    tmp1 = impl.ShopInfo(NAME, 123412341234, EMAIL, URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_raises(ValueError, tmp1.get_phone)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shoipinfo_phone_for_invalid_value4():
    tmp1 = impl.ShopInfo(NAME, -412341234, EMAIL, URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_raises(ValueError, tmp1.get_phone)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_phone_for_invalid_value5():
    tmp1 = impl.ShopInfo(NAME, None, EMAIL, URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_raises(ValueError, tmp1.get_phone)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_phone_for_invalid_type():
    tmp1 = impl.ShopInfo(NAME, str(PHONE), EMAIL, URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_raises(ValueError, tmp1.get_phone)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_email_for_invalid_value1():
    tmp1 = impl.ShopInfo(NAME, PHONE, "harry", URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_raises(ValueError, tmp1.get_email)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_email_for_invalid_value2():
    tmp1 = impl.ShopInfo(NAME, PHONE, "a@b@c", URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_raises(ValueError, tmp1.get_email)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_email_for_invalid_value3():
    tmp1 = impl.ShopInfo(NAME, PHONE, "john..doe@example.com", URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_raises(ValueError, tmp1.get_email)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_email_for_invalid_value4():
    tmp1 = impl.ShopInfo(NAME, PHONE, "john.doe@example..com", URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_raises(ValueError, tmp1.get_email)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_email_for_invalid_value5():
    tmp1 = impl.ShopInfo(NAME, PHONE, "john/doe@example..com", URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_raises(ValueError, tmp1.get_email)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_email_for_invalid_value6():
    tmp1 = impl.ShopInfo(NAME, PHONE, None, URL)
    assert tmp1.get_name() == NAME
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_raises(ValueError, tmp1.get_email)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_email_for_invalid_value7():
    tmp1 = impl.ShopInfo(NAME, PHONE, "b", URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_raises(ValueError, tmp1.get_email)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_email_for_invalid_value8():
    tmp1 = impl.ShopInfo(NAME, PHONE, "b@", URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_raises(ValueError, tmp1.get_email)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_email_for_invalid_value9():
    tmp1 = impl.ShopInfo(NAME, PHONE, "@a", URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_raises(ValueError, tmp1.get_email)
    nose.tools.assert_equal(tmp1.get_website(), URL)


def test_shopinfo_email_for_invalid_type():
    tmp1 = impl.ShopInfo(NAME, PHONE, 1234, URL)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_raises(ValueError, tmp1.get_email)
    nose.tools.assert_equal(tmp1.get_website(), URL)
    

def test_shopinfo_website_for_invalid_value1():
    tmp1 = impl.ShopInfo(NAME, PHONE, EMAIL, "ksu")
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_raises(ValueError, tmp1.get_website)


def test_shopinfo_website_for_invalid_value2():
    tmp1 = impl.ShopInfo(NAME, PHONE, EMAIL, "http://ksu%$^")
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_raises(ValueError, tmp1.get_website)


def test_shopinfo_website_for_invalid_value3():
    tmp1 = impl.ShopInfo(NAME, PHONE, EMAIL, None)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_raises(ValueError, tmp1.get_website)


def test_shopinfo_website_for_invalid_type():
    tmp1 = impl.ShopInfo(NAME, PHONE, EMAIL, 1234)
    nose.tools.assert_equal(tmp1.get_name(), NAME)
    nose.tools.assert_equal(tmp1.get_phone(), PHONE)
    nose.tools.assert_equal(tmp1.get_email(), EMAIL)
    nose.tools.assert_raises(ValueError, tmp1.get_website)
    
