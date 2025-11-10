import xml.etree.ElementTree


try:
    NYSE = xml.etree.ElementTree.parse("data/nyse.xml")
except FileNotFoundError:
    print("Stock data file not found")
except xml.etree.ElementTree.ParseError:
    print("Stock data file contains invalid data")
else:
    quotes = NYSE.getroot()
    print("COMPANY".ljust(40), end="")
    print("LAST".rjust(10), end="")
    print("CHANGE".rjust(10), end="")
    print("MIN".rjust(10), end="")
    print("MAX".rjust(10))
    print("-" * 80)
    for quote in quotes.findall("quote"):
        print(quote.text.ljust(40), end="")
        print("{:10.2f}".format(float(quote.attrib["last"])), end="")
        print("{:10.2f}".format(float(quote.attrib["change"])), end="")
        print("{:10.2f}".format(float(quote.attrib["min"])), end="")
        print("{:10.2f}".format(float(quote.attrib["max"])))
