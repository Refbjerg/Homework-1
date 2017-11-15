# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.Destroy)
    return fixture


def test_Homework1(app):
        success = True
        app.login(username="Admin", password="secret")
        app.group_creation(Group(name="Group-1", header="Groupleader", footer="Groupfooter"))
        app.Submit_group()


def test_Homework1_empty(app):
        success = True
        app.login(username="admin", password="secret")
        app.group_creation(Group(name="", header="", footer=""))
        app.Submit_group()


if __name__ == '__main__':
    unittest.main()
