import pytest
from Exceptions import ExceptionsDemo, MyException  

@pytest.mark.unit
def test_divide_0():

    demo = ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):
        demo.divide(10,0)

@pytest.mark.unit
def test_TypeError():

    demo = ExceptionsDemo()
    with pytest.raises(TypeError):
        demo.divide('Tamaulipas',5)

@pytest.mark.unit
def test_IndexError():

    demo = ExceptionsDemo()
    with pytest.raises(IndexError):
        demo.access_list([3,5,4],7)

@pytest.mark.unit
def test_Index_Type_Error():

    demo = ExceptionsDemo()
    with pytest.raises((TypeError,IndexError)):
        demo.access_list([3,5,4],1)
        demo.access_list([3,5,4],7)
        demo.access_list([3,5,4],'5')

@pytest.mark.unit
def test_Key_Error():

    demo = ExceptionsDemo()
    with pytest.raises(KeyError):
        demo.access_dict({'Manzana':'Dulce','Limon':'Agrio'},'Tomate')

@pytest.mark.unit
def test_File_not_found():

    demo = ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file('Frutas.txt')

@pytest.mark.unit
def test_Access_atribute():
    demoFake=ExceptionsDemo()
    demo = ExceptionsDemo()
    with pytest.raises(AttributeError):
        demo.access_attribute(demoFake)

@pytest.mark.wip
def test_Myexception():

    demo = ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-3)


