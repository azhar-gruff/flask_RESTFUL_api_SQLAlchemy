# coding: utf-8
from sqlalchemy import Column, DateTime, Unicode
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CompanyCodeMapping(Base):
    __tablename__ = 'company_code_mapping'
    __table_args__ = {'schema': 'company'}

    company_code = Column(Unicode(15), primary_key=True)
    duns_no = Column(Unicode(15))
    company_unity_code = Column(Unicode(15))
    registration_date = Column(DateTime)
    update_date = Column(DateTime)
    registration_user_name = Column(Unicode(50))
    update_user_name = Column(Unicode(50))
