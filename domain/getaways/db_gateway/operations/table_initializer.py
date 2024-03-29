from domain.getaways.db_gateway.db_manager import *
from entities.models.company import *
from entities.models.employee import *
from entities.models.job_listing import *
from entities.models.session import *

employee_creation_query = f""" CREATE TABLE IF NOT EXISTS {EMPLOYEE_TABLE_NAME} (
 {EMPLOYEE_ID} INTEGER PRIMARY KEY AUTO_INCREMENT , 
 {EMPLOYEE_PHOTO} VARCHAR(100) , 
 {EMPLOYEE_BIO} VARCHAR(300) , 
 {EMPLOYEE_RESUME} VARCHAR(100) , 
 {EMPLOYEE_NAME} VARCHAR(100) NOT NULL , 
 {EMPLOYEE_PHONE} VARCHAR(20) UNIQUE NOT NULL , 
 {EMPLOYEE_EMAIL} VARCHAR(50) UNIQUE NOT NULL , 
 {EMPLOYEE_TITLE} VARCHAR(50) NOT NULL , 
 {EMPLOYEE_PASSWORD} VARCHAR(200) NOT NULL 
);
"""

company_creationQuery = f""" CREATE TABLE IF NOT EXISTS {COMPANY_TABLE_NAME} (
 {COMPANY_ID} INTEGER PRIMARY KEY AUTO_INCREMENT , 
 {COMPANY_LOGO} VARCHAR(100) , 
 {COMPANY_NAME} VARCHAR(100) NOT NULL , 
 {COMPANY_INDUSTRY} VARCHAR(100) NOT NULL , 
 {COMPANY_WEBSITE} VARCHAR(100) UNIQUE , 
 {COMPANY_ABOUT} VARCHAR(300) , 
 {COMPANY_EMAIL} VARCHAR(100) UNIQUE NOT NULL , 
 {COMPANY_FACEBOOK_PAGE} VARCHAR(100) UNIQUE NOT NULL, 
 {COMPANY_PASSWORD} VARCHAR(200) NOT NULL 
);
"""

company_phone_creation_query = f""" CREATE TABLE IF NOT EXISTS company_phone (
 {COMPANY_ID_FK} INTEGER , 
 {COMPANY_PHONE} VARCHAR(20) UNIQUE NOT NULL , 
 FOREIGN KEY ({COMPANY_ID_FK}) REFERENCES company({COMPANY_ID}) ON DELETE CASCADE 
);
"""

job_listing_creation_query = f""" CREATE TABLE IF NOT EXISTS {JOB_LISTING_TABLE_NAME} (
  {JOB_LISTING_ID} INTEGER PRIMARY KEY AUTO_INCREMENT , 
  {COMPANY_ID_FK} INTEGER NOT NULL , 
  {JOB_LISTING_EXP_LEVEL} VARCHAR(15) NOT NULL , 
  {JOB_LISTING_TITLE} VARCHAR(50) NOT NULL , 
  {JOB_LISTING_STATUS} INTEGER NOT NULL DEFAULT 1 , 
  {JOB_LISTING_DESCRIPTION} VARCHAR(300) , 
  FOREIGN KEY ({COMPANY_ID_FK}) REFERENCES company({COMPANY_ID}) ON DELETE CASCADE
);
"""

job_application_creation_query = f""" CREATE TABLE IF NOT EXISTS {JOB_APPLICATION_TABLE_NAME} (
  {EMPLOYEE_ID_FK} INTEGER NOT NULL , 
  {JOB_LISTING_ID_FK} INTEGER NOT NULL , 
  {JOB_APPLICATION_STATUS} VARCHAR(30) NOT NULL , 
  FOREIGN KEY ({EMPLOYEE_ID_FK}) REFERENCES employee({EMPLOYEE_ID}) ON DELETE CASCADE , 
  FOREIGN KEY ({JOB_LISTING_ID_FK}) REFERENCES job_listing({JOB_LISTING_ID}) ON DELETE CASCADE  ,
  PRIMARY KEY ({EMPLOYEE_ID_FK}, {JOB_LISTING_ID_FK})
);
"""

experience_creation_query = f""" CREATE TABLE IF NOT EXISTS {EXPERIENCE_TABLE_NAME} (
  {EXPERIENCE_ID}  INTEGER PRIMARY KEY AUTO_INCREMENT , 
  {EMPLOYEE_ID_FK} INTEGER NOT NULL , 
  {EXPERIENCE_COMPANY_NAME} VARCHAR(100) NOT NULL , 
  {EXPERIENCE_EMP_TITLE} VARCHAR(50) NOT NULL , 
  {EXPERIENCE_EMPLOYMENT_TYPE} INTEGER , 
  {EXPERIENCE_START_DATE} DATE NOT NULL , 
  {EXPERIENCE_END_DATE} DATE , 
  FOREIGN KEY ({EMPLOYEE_ID_FK}) REFERENCES employee({EMPLOYEE_ID}) ON DELETE CASCADE
);
"""

company_session_creation_query = f""" CREATE TABLE IF NOT EXISTS {COMPANY_SESSION_TABLE_NAME} (
  {OWNER_ID} INTEGER NOT NULL , 
  {Auth_TOKEN} VARCHAR(200) UNIQUE NOT NULL , 
  {REFRESH_TOKEN} VARCHAR(200) UNIQUE NOT NULL , 
  {OWNER_EMAIL} VARCHAR(50) NOT NULL , 
  {CREATED_AT} BIGINT NOT NULL , 
  FOREIGN KEY ({OWNER_ID}) REFERENCES company({COMPANY_ID}) ON DELETE CASCADE 
);
"""

employee_session_creation_query = f""" CREATE TABLE IF NOT EXISTS {EMPLOYEE_SESSION_TABLE_NAME} (
  {OWNER_ID} INTEGER NOT NULL , 
  {Auth_TOKEN} VARCHAR(200) UNIQUE NOT NULL , 
  {REFRESH_TOKEN} VARCHAR(200) UNIQUE NOT NULL , 
  {OWNER_EMAIL} VARCHAR(50) NOT NULL , 
  {CREATED_AT} BIGINT NOT NULL , 
  FOREIGN KEY ({OWNER_ID}) REFERENCES employee({EMPLOYEE_ID}) ON DELETE CASCADE 
);
"""


def init_db_tables():
    make_db_query(employee_creation_query)
    make_db_query(company_creationQuery)
    make_db_query(company_phone_creation_query)
    make_db_query(job_listing_creation_query)
    make_db_query(job_application_creation_query)
    make_db_query(experience_creation_query)
    make_db_query(company_session_creation_query)
    make_db_query(employee_session_creation_query)
