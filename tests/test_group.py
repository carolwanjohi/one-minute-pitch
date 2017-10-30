import unittest
from app.models import Group

class TestGroup(unittest.TestCase):
    '''
    Test class to test behaviours of the Group class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_group = Group(name="Pick-up lines" )
        pass

    def tearDown(self):
        '''
        Using query.delete to delete elements in the database after each test
        '''
        Group.query.delete()

    def test_instance(self):
        '''
        Test case to check if new_group is an instance of Group
        '''

        self.assertTrue( isinstance( self.new_group, Group) )

    def test_save_group(self):
        '''
        Test case to check if a group is saved to the databse
        '''

        self.new_group.save_group()

        self.assertTrue( len(Group.query.all()) > 0 )

    def test_get_groups(self):
        '''
        Test case to check if all groups are returned by the get_groups function
        '''

        gotten_groups = Group.get_groups()

        self.assertEqual( len(gotten_groups) , 1 )

