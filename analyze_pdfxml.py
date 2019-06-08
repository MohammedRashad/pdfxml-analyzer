# Author : Rashad 
# Usage : 
# python3 analyze_pdfxml.py [operation type] [tag]
# [operation type] : --debug | --debug_save
# [tag] : --horizonatal_only | --vertical_only | --all
import xml.etree.ElementTree as ET
import pandas as pd
import wordninja
import sys
import ast

############################################### Extraction Funtions ###############################################
def analyze(root,tags):
    output = []
    
    for tag in tags :
        for i in root.iter(tag):  
            bbox = ast.literal_eval(i.attrib['bbox'])
            text = wordninja.split(str(i.text))
            
            if sys.argv[2] == '--debug' or '--debug_save':
                print('bbox', "=", bbox)
                print('data', "=", text)

            output.append([text , bbox[0] , bbox[1] , bbox[2]  ,bbox[3]])

        if sys.argv[2] == '--debug_save':   
            df = pd.DataFrame(output, columns=["text", "x0", "x1" , "y0" , "y1"])
            df.to_csv( tag + '.csv', index=False)
############################################### Extraction Pipeline ###############################################
if __name__ == "__main__" :

    if sys.argv[1] == '--help' :
        print("-------------- PDFXML Analyzer ---------------")
        print("Usage:")
        print("* python3 analyze_pdfxml.py --help \n* python3 analyze_pdfxml.py [operation type] [tag]")
        print("-> [operation type] : --debug | --debug_save")
        print("-> [tag] : --horizonatal_only | --vertical_only | --all")
    else :
        tags = ['LTTextBoxVertical' , 'LTTextBoxHorizontal']
        data_file = sys.argv[1] if sys.argv[1] else 'o.xml'
        tree = ET.parse(data_file)
        root = tree.getroot()
    
        if sys.argv[3] == '--horizonatal_only' :
            analyze(root, tags[1])
        if sys.argv[3] == '--vertical_only' :
            analyze(root,tags[0])
        if sys.argv[3] == '--all' :
           analyze(root, tags)
