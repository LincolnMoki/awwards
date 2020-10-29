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

class TestProject(TestCase):
    def setUp(self) -> None:
        self.new_project = Project(
            id=1,
            title='Hello world',
            details='a hello world app',
            link='https://github.com/hello.git',
            user=new_user,
            image='/media/hello.jpg',
            user_project_id='1',
            design='7',
            usability='8',
            creativity='9',
            content='8',
            vote_submissions='87'

        )

    def testInstance(self):
        self.assertTrue(isinstance(self.new_project, Project))

    def testSaveProject(self):
        before = Project.objects.all()
        self.new_project.save()
        after = Project.objects.all()

        self.assertLess(before, after)

    def testDeleteProject(self):
        before = Project.objects.all()
        self.new_project.delete()
        after = Project.objects.all()

        self.assertGreater(before, after)

    def tearDown(self) -> None:
        Project.objects.all().delete()
