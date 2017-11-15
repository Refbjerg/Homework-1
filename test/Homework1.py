# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.Destroy)
    return fixture


def test_Homework1(app):
        success = True
        app.session.login(username="Admin", password="secret")
        app.group.create(Group(name="Group-1", header="Groupleader", footer="Groupfooter"))
        app.group.Submit_group()


def test_Homework1_empty(app):
        success = True
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.group.Submit_group()


if __name__ == '__main__':
    unittest.main()
