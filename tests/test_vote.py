import unittest
from app.models import Vote,User,Line,Group

class TestVote(unittest.TestCase):
    '''
    Test class to test behaviours of the Vote class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        # self.group_pick_up = Group( name="Excuse lines" )

        # self.user_jim = User(username = "Jim", password = "banana", email = "jim@doe.com" )

        # self.new_line = Line( line_content="I am Groot", group = self.group_pick_up, user=self.user_jim)

        self.new_vote = Vote(vote_number=0 )

    # def tearDown(self):
    #     '''
    #     Using query.delete to delete elements in the database after each test
    #     '''
    #     Vote.query.delete()
    #     Line.query.delete()
    #     User.query.delete()
    #     Group.query.delete()

    def test_instance(self):
        '''
        Test case to check if new_vote is an instance of Vote
        '''

        self.assertTrue( isinstance( self.new_vote, Vote) )

    def test_save_vote(self):
        '''
        Test case to check if a vote is saved to the databse
        '''

        self.new_vote.save_vote()

        self.assertTrue( len(Vote.query.all()) > 0 )

    def test_num_vote(self):
        '''
        Test to check if up_vote is working
        '''
        # self.group_pick_up = Group( name="Excuse lines" )

        # self.user_jim = User(username = "Jim", password = "banana", email = "jim@doe.com" )

        # self.new_line = Line( line_content="I am Groot", group = self.group_pick_up, user=self.user_jim)
        self.new_vote.save_vote()
        
        gotten_votes = Vote.num_vote(13242143123412341234123,123412341234123412341234)

        self.assertTrue( gotten_votes == 0)


