import unittest
from unittest import TestCase
from app.models import User

class TestUsermodel(unittest, TestCase):
  '''
  Tests to verify that password hashed is the same as password set
  '''
  def setUp(self):
    self.new_user = User(password = 'popote')

  def test_password_setter(self):
      self.assertTrue(self.new_user.password_hash is not None)

  def test_no_access(self):
    with self.assertRaises(AttributeError):
      self.new_user.password

    def test_password_verification(self):
      self.assertTrue(self.new_user.verify_password('popote'))