import xml.etree.ElementTree as ET 

import csv 

class Dom2Parser: 

    def __init__(self): 

        self.xml_file = ET.parse("compiler.xml") 

        self.root = self.xml_file.getroot() 

        self.book_div = self.root.find("book") 

  

    def print_parsed_data(self): 

      with open("mycsv.csv" , "w",newline='') as file: 

        csvreader = csv.writer(file) 

        csvreader.writerow(["id","author","title","genre","price", "publish_date","description"]) 

        for child in self.xml_file.getroot(): 

            print("id:", child.attrib) 

            print("author:", child.find("author").text) 

            print("title:", child.find("title").text) 

            print("genre:", child.find("genre").text) 

            print("price:", child.find("price").text) 

            print("publish_date:", child.find("publish_date").text) 

            print("description:", child.find("description").text) 

            print() 

            csvreader.writerow([child.attrib['id'], 

                                child.find("author").text, 

                                child.find("title").text, 

                               child.find("genre").text,child.find("price").text, 

                               child.find("publish_date").text, 

                               child.find("description").text] 

                               ) 

            #self.book_div = self.book_div.find("book") 

  

    def write_to_file(self): 

        with open("parsed_data.txt", "w") as f: 

            for child in self.xml_file.getroot(): 

                print("id:", child.attrib) 

                print("author:", child.find("author").text) 

                print("title:", child.find("title").text) 

                print("genre:", child.find("genre").text) 

                print("price:", child.find("price").text) 

                print("publish_date:", child.find("publish_date").text) 

                print("description:", child.find("description").text) 

                print() 

  

if __name__ == "__main__": 

    parser = Dom2Parser() 

    parser.print_parsed_data() 
