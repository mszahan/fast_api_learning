import pytest

def test_equal():
    assert 1 == 1


def test_is_instance():
    assert isinstance("Hello", str)
    assert isinstance(1, int)


def test_bool():
    validated = True
    assert validated is True


def test_type():
    assert type('hello') is str
    assert type(1) is int
    assert type(1.0) is float


class Student:
    def __init__(self, first_name: str, last_name: str, major: str, year: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.year = year

# def test_student():
#     p = Student('John', 'Doe', 'Computer Science', 2023)
#     assert p.first_name == 'John', 'First name should be John'
#     assert p.last_name == 'Doe', 'Last name should be Doe'
#     assert p.major == 'Computer Science' # ,this a message which is optional 
#     assert p.year == 2023


@pytest.fixture
def default_student():
    return Student('John', 'Doe', 'Computer Science', 2023)

def test_student(default_student):
    assert default_student.first_name == 'John', 'First name should be John'
    assert default_student.last_name == 'Doe', 'Last name should be Doe'
    assert default_student.major == 'Computer Science' # ,this a message which is optional 
    assert default_student.year == 2023