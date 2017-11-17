# -*- coding: utf-8 -*-
import pytest
from fixture.application_contacts import Application_contacts
from model.contact import Contact



@pytest.fixture
def app(request):
        fixture = Application_contacts()
        request.addfinalizer(fixture.Destroy)
        return fixture

def test_addcontact(app):
        success = True
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.Add_new_contact(Contact(first_name="Oleg", middlename="Leonidovich", lastname="Balashevich",
                             address="Saint-Petersburg, Ligovskiy prospect 235,apt 34", mobile="+9627275922", mail="wooler@bk.ru",
                             day="//div[@id='content']/form/select[1]//option[5]",
                             month="//div[@id='content']/form/select[2]//option[6]", year="1986"))
        app.session.logout()

def test_addcontact_empty(app):
        success = True
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.Add_new_contact(Contact(first_name="", middlename="", lastname="",
                             address="", mobile="", mail="",
                             day="//div[@id='content']/form/select[1]//option[5]",
                             month="//div[@id='content']/form/select[2]//option[6]", year="1986"))
        app.session.logout()



