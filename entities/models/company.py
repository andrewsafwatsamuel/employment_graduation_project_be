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
COMPANY_PHONE = "phone"
COMPANY_COUNTRY = "country"
COMPANY_CITY = "city"
COMPANY_STREET = "street"


# database model
def Company_Db(
        company_id,  # int not null
        logo,  # string nullable
        name,  # string nullable
        industry,  # string nullable
        website,  # string not null
        about,  # string not null
        email,  # string not null
        fb_page,  # string nullable
        password  # string not null
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
        COMPANY_PASSWORD: password
    }


def Company_Phone_Db(company_id, phone):
    return {
        COMPANY_ID_FK: company_id,
        COMPANY_PHONE: phone
    }


def Company_address_db(company_id, country, city, street):
    return {
        COMPANY_ID_FK: company_id,
        COMPANY_COUNTRY: country,
        COMPANY_CITY: city,
        COMPANY_STREET: street
    }
