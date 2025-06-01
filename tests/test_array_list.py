import pytest
from src.array_list import ArrayList

def test_append_and_length():
    lst = ArrayList()
    assert lst.length() == 5
    lst.append('a')
    lst.append('b')
    assert lst.length() == 2

def test_insert_and_get():
    lst = ArrayList()
    lst.append('a')
    lst.append('c')
    lst.insert('b', 1)
    assert lst.get(1) == 'b'

def test_delete():
    lst = ArrayList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    deleted = lst.delete(1)
    assert deleted == 'b'
    assert lst.length() == 2

def test_delete_all():
    lst = ArrayList()
    lst.append('a')
    lst.append('b')
    lst.append('a')
    lst.deleteAll('a')
    assert lst.length() == 1
    assert lst.get(0) == 'b'

def test_clone():
    lst = ArrayList()
    lst.append('a')
    clone = lst.clone()
    assert clone.get(0) == 'a'
    clone.append('b')
    assert lst.length() != clone.length()

def test_reverse():
    lst = ArrayList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    lst.reverse()
    assert lst.get(0) == 'c'
    assert lst.get(2) == 'a'

def test_find_first_last():
    lst = ArrayList()
    lst.append('a')
    lst.append('b')
    lst.append('a')
    assert lst.findFirst('a') == 0
    assert lst.findLast('a') == 2

def test_clear():
    lst = ArrayList()
    lst.append('a')
    lst.clear()
    assert lst.length() == 0

def test_extend():
    lst1 = ArrayList()
    lst1.append('a')
    lst2 = ArrayList()
    lst2.append('b')
    lst1.extend(lst2)
    assert lst1.length() == 2
