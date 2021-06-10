import unittest

import sys
sys.path.append('./src/pyhy')

import people

class TestPeopleSearch(unittest.TestCase):

    def test_person( self ):
        matti = people.search('Matti Nelimarkka')
        self.assertEqual( matti['firstnames'], "Matti", "First name incorrect" )
        self.assertEqual( matti['lastname'], "Nelimarkka", "Last name incorrect" )
        self.assertEqual( matti['email'], "matti.nelimarkka@helsinki.fi", "Email incorrect" )
        self.assertEqual( matti['phoneNumber'], "0294124545", "Phone number incorrect")
        self.assertEqual( matti['title'], "University Lecturer", "Title incorrect")

    def test_nobody( self ):
        none = people.search('nobody has this name')
        self.assertEqual( none, None, "Code breaks when there are zero results")

    def test_many( self ):
        many = people.search('Matti')
        assert len( many ) > 1, "Code breaks when there are many results"

class TestOrganisationSearch(unittest.TestCase):

    def test_organisation( self ):
        csds = people.by_organisation( [62060775] )

        ## todo: here it would be nice to do a bit more proper testing
        assert len( csds ) > 1, 'Organisation does not collect all people'

        names = map( lambda x: x['firstnames'], csds )
        assert 'Matti' in names, 'Known person not working for right organisation'

    def test_shorthands( self ):
        csds1 = people.by_organisation( [62060775] )
        csds2 = people.by_organisation( 62060775 )
        csds3 = people.by_organisation( '62060775' )

        ## todo: here it would be nice to do a bit more proper testing
        assert csds1 == csds2, 'Giving integer as parameter does not work in the shorthand'
        assert csds1 == csds3, 'Giving string as parameter does not work in the shorthand'

if __name__ == '__main__':
    unittest.main()
