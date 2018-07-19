"""validation class with regular expressions"""
import re


class Validate2():
    """valiation class for diary inputs"""
    def __init__(self, entry_id, title, body):
        self.entry_id = entry_id
        self.title = title
        self.body = body

    def validate_empty(self):
        """method to validate my input """
        result = ""
        if type(self.entry_id) is not int:
            result = "bad id data"
        elif (not re.search("[a-zA-Z0-9]", self.title) or not
              re.search("^(\s|\S)*(\S)+(\s|\S)*$", self.body)):
            result = "wrong data"
        else:
            result = True
        return result

    @classmethod
    def validate_update(cls, title, body):
        """method to validate update input """
        result = ""
        if (not re.search("[a-zA-Z0-9]", title) or not
                re.search("^(\s|\S)*(\S)+(\s|\S)*$", body)):
            result = "wrong data"
        else:
            result = True
        return result
