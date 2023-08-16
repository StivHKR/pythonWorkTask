from bs4 import BeautifulSoup


def print_target(Id):
    print("Solution 1")
    with open("sma_gentext.xml", "r") as f:
        data = f.read()
    parsed_data = readXml(data, Id)
    writeToFile(parsed_data,"solution1")


def readXml(data, Id):
    bs_data = BeautifulSoup(data, "lxml")
    trans_attribute = bs_data.find('trans-unit', {'id': Id})
    target_element = trans_attribute.find('target').string
    print("Target : ", target_element)
    return target_element


def writeToFile(data, filename):
    result_file = open(filename + '.txt', 'w')
    result_file.write(data)
    result_file.close()
