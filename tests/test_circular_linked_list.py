import pytest
from src.circular_linked_list import CircularLinkedList

def test_append_and_length():
    lst = CircularLinkedList()
    assert lst.length() == 0
    lst.append('a')
    lst.append('b')
    assert lst.length() == 2

def test_insert_and_get():
    lst = CircularLinkedList()
    lst.append('a')
    lst.append('c')
    lst.insert('b', 1)
    assert lst.get(1) == 'b'

def test_delete():
    lst = CircularLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    deleted = lst.delete(1)
    assert deleted == 'b'
    assert lst.length() == 2

def test_delete_all():
    lst = CircularLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('a')
    lst.deleteAll('a')
    assert lst.length() == 1
    assert lst.get(0) == 'b'

def test_clone():
    lst = CircularLinkedList()
    lst.append('a')
    clone = lst.clone()
    assert clone.get(0) == 'a'
    clone.append('b')
    assert lst.length() != clone.length()

def test_reverse():
    lst = CircularLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    lst.reverse()
    assert lst.get(0) == 'c'
    assert lst.get(2) == 'a'

def test_find_first_last():
    lst = CircularLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('a')
    assert lst.findFirst('a') == 0
    assert lst.findLast('a') == 2

def test_clear():
    lst = CircularLinkedList()
    lst.append('a')
    lst.clear()
    assert lst.length() == 0

def test_extend():
    lst1 = CircularLinkedList()
    lst1.append('a')
    lst2 = CircularLinkedList()
    lst2.append('b')
    lst1.extend(lst2)
    assert lst1.length() == 2
