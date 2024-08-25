import os

# Dictionary for service prices
service_prices = {
    'oil change': 35,
    'tire rotation': 19,
    'car wash': 7,
    'car wax': 12,
    '-': 0  # Option for no service
}

# ASCII art banners for visual enhancement
ascii_banner = r"""
       _____                    _                     _           _____ _                    _____                 _               
      |  __ \                  ( )         /\        | |         / ____| |                  / ____|               (_)              
      | |  | | __ ___   ___   _|/ ___     /  \  _   _| |_ ___   | (___ | |__   ___  _ __   | (___   ___ _ ____   ___  ___ ___  ___ 
      | |  | |/ _` \ \ / / | | | / __|   / /\ \| | | | __/ _ \   \___ \| '_ \ / _ \| '_ \   \___ \ / _ \ '__\ \ / / |/ __/ _ \/ __|
      | |__| | (_| |\ V /| |_| | \__ \  / ____ \ |_| | || (_) |  ____) | | | | (_) | |_) |  ____) |  __/ |   \ V /| | (_|  __/\__ \
      |_____/ \__,_| \_/  \__, | |___/ /_/    \_\__,_|\__\___/  |_____/|_| |_|\___/| .__/  |_____/ \___|_|    \_/ |_|\___\___||___/
                           __/ |                                                   | |                                             
                          |___/                                                    |_|                                            
"""
invoice_banner = r"""
       ____                    _          _         _          ____  _                   ___                 _          
      |  _ \  __ ___   ___   _( )___     / \  _   _| |_ ___   / ___|| |__   ___  _ __   |_ _|_ ____   _____ (_) ___ ___ 
      | | | |/ _` \ \ / / | | |// __|   / _ \| | | | __/ _ \  \___ \| '_ \ / _ \| '_ \   | || '_ \ \ / / _ \| |/ __/ _ \
      | |_| | (_| |\ V /| |_| | \__ \  / ___ \ |_| | || (_) |  ___) | | | | (_) | |_) |  | || | | \ V / (_) | | (_|  __/
      |____/ \__,_| \_/  \__, | |___/ /_/   \_\__,_|\__\___/  |____/|_| |_|\___/| .__/  |___|_| |_|\_/ \___/|_|\___\___|
                         |___/                                                  |_|
"""

# Resize terminal window for proper display
def setup_terminal():
    os.system('mode 145, 40')

# Print ASCII art banners
def display_banner(banner):
    print(banner)

# Request class handling service selections and pricing
class Request:
    def __init__(self):
        self.service = self.get_user_input()
        self.display_service_info()

    def get_user_input(self):
        while True:
            service = input('Select a service (or type "-" for no service):\n').lower()
            if service in service_prices:
                return service
            print("Invalid service. Please select a valid service.")

    def display_service_info(self):
        if service_prices[self.service] > 0:
            print(f"Service: {self.service.capitalize()} - ${service_prices[self.service]}")
        elif self.service == '-':
            print("No service selected")

    def get_price(self):
        return service_prices[self.service]

# Main function to control program flow
def main():
    setup_terminal()
    display_banner(ascii_banner)

    print('\nPlease select services from the list below:')
    for service, price in service_prices.items():
        if service != '-':
            print(f"{service.capitalize()} -- ${price}")
    print('No service    -- Type \'-\'\n')

    services = [Request(), Request()]
    total_price = sum(service.get_price() for service in services)

    display_banner(invoice_banner)
    print("Total: $", total_price)

    os.system("pause")

if __name__ == "__main__":
    main()
