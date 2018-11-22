import unittest
from unittest import TestCase

import pytest

from game import monsters


def test_default(monster):
    assert monster.sound == 'roar'
    assert monster.hit_points == 20


def test_color(monster):
    assert monster.color == 'blue'

def test_custom_hit_points(monster):
        #monster = monsters.Monster(hit_points=200)
        assert monster.hit_points ==20


def test_battle_cry(monster):
    assert monster.battle_cry() == monster.sound.upper()



