import xml.etree.ElementTree as ET
import xml_file_searcher as file



def print_target(id):
    print("Solution 2")
    tree = ET.parse('sma_gentext.xml')
    for child in tree.getroot().iter():
        if child.tag.__eq__("trans-unit"):
            if child.attrib["id"].__eq__(id):
                for sub_child in child.iter():
                    if sub_child.tag.__eq__("target"):
                        print("Target : ", sub_child.text)
                        file.writeToFile(sub_child.text, "Solution 2")

