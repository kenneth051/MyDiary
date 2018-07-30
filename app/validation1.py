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
    def validate_duplicate_on_update( cls, entries, update_data):
        """method to check for duplicate entries when validating"""
        for data in entries:
            if( data["title"] == update_data["title"] or
                data["body"] == update_data["body"]):
                return True
