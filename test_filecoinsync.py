# test_filecoinsync.py
"""
Tests for FilecoinSync module.
"""

import unittest
from filecoinsync import FilecoinSync

class TestFilecoinSync(unittest.TestCase):
    """Test cases for FilecoinSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FilecoinSync()
        self.assertIsInstance(instance, FilecoinSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FilecoinSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
