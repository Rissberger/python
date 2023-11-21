"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """class to find random words from a list"""
    def __init__(self, path):
        """read words from a file and store them in a list"""
        with open(path) as file:
            self.words = self.parse(file)
        
        print(f"(len(self.words)) words read")

    def parse(self, file):

        return [word.strip() for word in file]
    
    def random(self):
        """returns a random word from the list"""
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Subclass of WordFinder that excludes comments and blank lines."""

    def __init__(self, filepath):
        """Initialize and filter words."""
        super().__init__(filepath)
        self.words = [word for word in self.words if word and not word.startswith('#')]
