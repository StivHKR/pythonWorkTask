import xml_file_searcher as xml_searcher_solution1
import xml_file_searcher2 as xml_searcher_solution2

# Solution 1 with help of BeautifulSoup third party library
xml_searcher_solution1.print_target("42007")

# Solution 2 with help of xml.etree.ElementTree built in library
xml_searcher_solution2.print_target("42007")
