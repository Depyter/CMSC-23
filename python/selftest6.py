import unittest
from datetime import date
from labex6 import daysBetween, Periodical, Book, Page, PC, LibraryCard
# Test cases for the daysBetween function
class TestDaysBetween(unittest.TestCase):
    def test_days_between_positive(self):
        d1 = date(2024, 9, 30)
        d2 = date(2024, 9, 15)
        self.assertEqual(daysBetween(d1, d2), 15)

    def test_days_between_negative(self):
        d1 = date(2024, 9, 15)
        d2 = date(2024, 9, 30)
        self.assertEqual(daysBetween(d1, d2), -15)

    def test_days_between_same_day(self):
        d1 = date(2024, 9, 30)
        d2 = date(2024, 9, 30)
        self.assertEqual(daysBetween(d1, d2), 0)

# Test cases for the Book class
class TestBook(unittest.TestCase):
    def setUp(self):
        self.pages = [Page("Introduction", "Content of introduction"), Page("Chapter 1", "Content of chapter 1")]
        self.book = Book(1, "Python Programming", "John Doe", date(2020, 5, 20), self.pages)

    def test_unique_item_id(self):
        self.assertEqual(self.book.uniqueItemId(), 1)

    def test_cover_info(self):
        self.assertEqual(self.book.coverInfo(), "Title: Python Programming\nAuthor: John Doe")

# Test cases for the Periodical class
class TestPeriodical(unittest.TestCase):
    def setUp(self):
        self.pages = [Page("Cover Story", "Content of cover story"), Page("Feature", "Content of feature")]
        self.periodical = Periodical(101, "Tech Monthly", "Jane Smith", date(2023, 7, 10), self.pages)

    def test_unique_item_id(self):
        self.assertEqual(self.periodical.uniqueItemId(), 101)

    def test_common_name(self):
        self.assertEqual(self.periodical.commonName(), "Tech Monthly issue: 2023-07-10")

# Test cases for the PC class
class TestPC(unittest.TestCase):
    def setUp(self):
        self.pc = PC(1001)

    def test_unique_item_id(self):
        self.assertEqual(self.pc.uniqueItemId(), 1001)

    def test_common_name(self):
        self.assertEqual(self.pc.commonName(), "PC1001")

# Test cases for the LibraryCard class
class TestLibraryCard(unittest.TestCase):
    def setUp(self):
        self.book = Book(1, "Python Programming", "John Doe", date(2020, 5, 20), [])
        self.pc = PC(1001)
        self.library_card = LibraryCard(12345, "Alice", {})

    def test_borrow_item(self):
        borrow_date = date(2024, 9, 1)
        self.library_card.borrowItem(self.book, borrow_date)
        self.assertIn(self.book, self.library_card._LibraryCard__borrowedItems)
        self.assertEqual(self.library_card._LibraryCard__borrowedItems[self.book], borrow_date)

    def test_borrower_report(self):
        self.library_card.borrowItem(self.book, date(2024, 9, 1))
        report = self.library_card.borrowerReport()
        self.assertIn("Alice", report)
        self.assertIn("Python Programming", report)
        self.assertIn("borrow date:2024-09-01", report)

    def test_return_item(self):
        self.library_card.borrowItem(self.book, date(2024, 9, 1))
        self.library_card.returnItem(self.book)
        self.assertNotIn(self.book, self.library_card._LibraryCard__borrowedItems)

    def test_items_due(self):
        self.library_card.borrowItem(self.book, date(2024, 9, 1))
        due_items = self.library_card.itemsDue(date(2024, 9, 15))
        self.assertIn(self.book, due_items)

    def test_total_penalty(self):
        self.library_card.borrowItem(self.book, date(2024, 9, 1))
        total_penalty = self.library_card.totalPenalty(date(2024, 9, 15))
        self.assertGreaterEqual(total_penalty, 0)

if __name__ == "__main__":
    unittest.main()