
import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    print "You must entry an address"

webbrowser.open('https://www.google.com/maps/place/' + address)
