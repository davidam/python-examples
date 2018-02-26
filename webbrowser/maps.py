
import webbrowser, sys

if len(sys.argv) > 1:
    # Get address from command line.
    address = sys.argv[1]
    webbrowser.open('https://www.google.com/maps/place/' + address)
else:
    # Get address from clipboard.
    print("You must entry an address")


