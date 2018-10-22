
import pytest
from unittest.mock import MagicMock
from Linereader import readFromFile


def test_canReadFromTheFile():
    readFromFile("blah")


def test_returnCorrectString(monkeypatch):
    mock_file = MagicMock()
    mock_file.readLine = MagicMock(return_value ="test line")
    mock_file = MagicMock(return_value = mock_file)
    monkeypatch.setattr("bulittins.open",mock_open)
    result = readFromFile("blah")
    