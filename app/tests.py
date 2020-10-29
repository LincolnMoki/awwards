from django.test import TestCase

from .models import Project, Profile, User

new_user = User(username='kaphie')

test_project = Project(
    id=1,
    title='Test Hello',
    details='a test hello world app',
    link='https://github.com/testhello.git',
    user=new_user, image='/media/test_hello.jpg',
    user_project_id='1',
    design='7',
    usability='8',
    creativity='9',
    content='8',
    vote_submissions='87'
)
