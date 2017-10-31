import unittest
from app.models import Line,Group,User

class TestLine(unittest.TestCase):
    '''
    Test class to test behaviours of the Line class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        # self.group_ditch = Group( name="Ditch Lines" )

        # self.user_boe = User(username = "Boe", password = "banana", email = "boe@doe.com" )

        self.new_line = Line( line_content="I am Groot")

    # def tearDown(self):
    #     '''
    #     Using query.delete to delete elements in the database after each test
    #     '''
    #     Line.query.delete()
    #     User.query.delete()
    #     Group.query.delete()

    def test_instance(self):
        '''
        Test case to check if new_line is an instance of Line
        '''
        self.assertTrue( isinstance( self.new_line, Line) )

    def test_save_line(self):
        '''
        Test case to check if a line is saved to the databse
        '''
        # user_dan =  User(username = "Dan", password = "banana", email = "dan@doe.com" )

        # test_line = Line( line_content="I am Groot", group = self.group_ditch, user = user_dan )

        self.new_line.save_line()

        self.assertTrue( len(Line.query.all()) > 0)

        # Line.query.delete()
        # User.query.delete()
        # Group.query.delete()

    def test_get_lines(self):
        '''
        Test case to check if a line and its information is returned by the get_lines function that takes in an id and match it to id in the group table
        '''

        # Line.query.delete()
        # User.query.delete()
        # Group.query.delete()

        self.new_line.save_line()

        gotten_lines = Line.get_lines(4990826417581240726341234)

        self.assertFalse( len(gotten_lines) == 1)



