import pytest
import pong_functions


def test_computer():
    assert pong_functions.computer(521.0, 493.0, 0.5, 75, [900, 600]) == 493.5


def test_file_managment():
    assert type(pong_functions.file_managment('read', {})) != 'int'


def test_writing_text():
    assert pong_functions.ball_coordinates(0.5, -0.5, 10, 767.0, 389.0, 300, 389.5, 15, 50, 75, [900, 600], 0, 0,
                                           {'nick': 'cos', 'rekord': 0, 'rekord-computer': 0})[3] == False
