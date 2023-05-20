# company variable names
COMPANY_TABLE_NAME = "company"
COMPANY_ID = "id"
COMPANY_LOGO = "logo"
COMPANY_NAME = "name"
COMPANY_INDUSTRY = "industry"
COMPANY_WEBSITE = "website"
COMPANY_ABOUT = "about"
COMPANY_EMAIL = "email"
COMPANY_FACEBOOK_PAGE = "fbPage"
COMPANY_PASSWORD = "password"
COMPANY_ID_FK = "company_id"
COMPANY_PHONE_TABLE_NAME = "company_phone"
COMPANY_PHONE = "phone"


# COMPANY_COUNTRY = "country"
# COMPANY_CITY = "city"
# COMPANY_STREET = "street"


# database model
def Company_Db(
        company_id=None,  # int not null
        logo=None,  # string nullable
        name=None,  # string nullable
        industry=None,  # string nullable
        website=None,  # string not null
        about=None,  # string not null
        email=None,  # string not null
        fb_page=None,  # string nullable
        password=None,  # string not null
        phones=None,
):
    return {
        COMPANY_ID: company_id,
        COMPANY_LOGO: logo,
        COMPANY_NAME: name,
        COMPANY_INDUSTRY: industry,
        COMPANY_WEBSITE: website,
        COMPANY_ABOUT: about,
        COMPANY_EMAIL: email,
        COMPANY_FACEBOOK_PAGE: fb_page,
        COMPANY_PASSWORD: password,
        COMPANY_PHONE_TABLE_NAME: phones
    }


def Company_Phone_Db(company_id, phone):
    return {
        COMPANY_ID_FK: company_id,
        COMPANY_PHONE: phone
    }
