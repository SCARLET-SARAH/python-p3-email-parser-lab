# your code goes here!
import re
class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split the string by commas and spaces
        split_addresses =re.split(r'[,\s]+', self.addresses)

        # Filter out empty strings and whitespace-only entries
        split_addresses = [address.strip() for address in split_addresses if address.strip()]

        return split_addresses