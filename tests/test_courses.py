import unittest

import sys
sys.path.append('./src/py4hy')

import courses

class TestCourseSearch(unittest.TestCase):

    def test_course( self ):
        matti = courses.search('Matti Nelimarkka', 2020, 'fi' )
        assert len( matti ) == 8, "Matti had 8 courses in 2020"

        course = matti[0]

        assert course['code'] == 'SOST-942', "The first course has the wrong course code"
        assert course['name'] == 'Qualitative research and computers', "The first course has the wrong name"

    def test_nobody( self ):
        none = people.search('nobody has this name')
        self.assertEqual( none, None, "Code breaks when there are zero results")

    def test_many( self ):

        many = people.search('Matti')
        mattis = []

        for course in many:
            mattiFound = False
            for teacher in course['teacherNames']:
                if 'matti' in teacher.lower():
                    mattiFound = True
                    mattis.append( teacher.lower() )
            assert mattiFound == True, "API returned a course where Matti was not a teacher"

        mattis = set( mattis )
        assert len( mattis ) > 1, "API did not find many Mattis"

        print

if __name__ == '__main__':
    unittest.main()
