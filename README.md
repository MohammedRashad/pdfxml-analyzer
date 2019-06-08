# pdfxml-analyzer
small library to extract data from pdfxml and similar files 

### Usage
* Command Line Interface
  * `python3 analyze_pdfxml.py --help`
  * `python3 analyze_pdfxml.py [operation type] [tag]`
     * **[operation type] :** *--debug* **|** *--debug_save*
     * **[tag] :** *--horizonatal_only* **|** *--vertical_only* **|** *--all*
* Import Library :
   ```
   from analyze_pdfxml import * 
   root = #XML File Reading
   tags = #list of tags 
   mode = #operation type
   analyze(root,tags,mode)
   ```
