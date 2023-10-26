import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_create(self):
        """Test the create method of the Base class"""
        # Test creating a Rectangle object
        rectangle_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        rectangle = Base.create(**rectangle_dict)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

        # Test creating a Square object
        square_dict = {'id': 2, 'size': 6, 'x': 7, 'y': 8}
        square = Base.create(**square_dict)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_to_json_string(self):
        """Test the to_json_string method of the Base class"""
        # Test with a list of dictionaries
        list_dicts = [{'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5},
                      {'id': 2, 'size': 6, 'x': 7, 'y': 8}]
        json_string = Base.to_json_string(list_dicts)
        expected_string = '[{"id": 1, "width": 2, "height": 3, "x": 4\
            , "y": 5}, {"id": 2, "size": 6, "x": 7, "y": 8}]'
        self.assertEqual(json_string, expected_string)

        # Test with an empty list
        empty_list = []
        json_string = Base.to_json_string(empty_list)
        expected_string = '[]'
        self.assertEqual(json_string, expected_string)

        # Test with None
        json_string = Base.to_json_string(None)
        expected_string = '[]'
        self.assertEqual(json_string, expected_string)

    def test_from_json_string(self):
        """Test the from_json_string method of the Base class"""
        # Test with a JSON string
        json_string = '[{"id": 1, "width": 2, "height": 3, "x": 4\
            , "y": 5}, {"id": 2, "size": 6, "x": 7, "y": 8}]'
        list_dicts = Base.from_json_string(json_string)
        expected_list = [{'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5},
                         {'id': 2, 'size': 6, 'x': 7, 'y': 8}]
        self.assertEqual(list_dicts, expected_list)

        # Test with an empty string
        empty_string = ''
        list_dicts = Base.from_json_string(empty_string)
        expected_list = []
        self.assertEqual(list_dicts, expected_list)

        # Test with None
        list_dicts = Base.from_json_string(None)
        expected_list = []
        self.assertEqual(list_dicts, expected_list)


if __name__ == '__main__':
    unittest.main()
    