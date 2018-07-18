"""validation page"""

class Validate():
    """class to validate diary data"""

    @classmethod
    def validate_entry(cls, entries, entry):
        """method to check for duplicate entries"""
        for data in entries:
            if (data['title'] == entry.title and
                    data['body'] == entry.body):
                return True

    @classmethod
    def validate_id(cls, entries, entry_id):
        """method to check if Id has been taken"""
        for data in entries:
            if data['entry_id'] == entry_id:
                return True
