import traceback
import sys

# custom class to handle exception
class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error_message, error_detail:sys):
        # this is static as we don't want to create objects of this class for default exceptions
        
        # this only takes the exception traceback message and leaves the other 2 messages
        _, _, exc_tb = error_detail.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename   # to get the filename where error occured
        line_number = exc_tb.tb_lineno                  # to get the line no. where error occured

        return f"Error in {filename}, line {line_number}: {error_message}"

    # magic function which gives returns in string format
    def __str__(self):
        return self.error_message