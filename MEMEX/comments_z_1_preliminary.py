# Comments to explain every line

import os, yaml

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "z_config.yml"                                     # variables yml file to have all the settings stored in an extra place 
vars = yaml.load(open(settingsFile))

###########################################################
# FUNCTIONS ###############################################
###########################################################

# analyze bibTeX data; identify what needs to be fixed

def bibAnalyze(bibTexFile):

    tempDic = {}                                                   # creates a temporary dictionary

    with open(bibTexFile, "r", encoding="utf8") as f1:             # opens the bibtexfile with the encoding to make sure special characters can be read
        records = f1.read()                                        # to get the records it reads through the document
        records = records.split("\n@")                             # it splits the record at new line and @

        for record in records[1:]:                                 # looping through the records to get the data we want, ignoring first line - its empty
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower():                           # looks at the records with pdfs; .lower - lower case letters
                record = record.strip()                            # strips it of spaces
                record = record.split("\n")[:-1]                   # splits the records again, this time at new line, doesnt look at last charakter - }

                for r in record[1:]:                               # loops through the records again
                    r = r.split("=")[0].strip()                    # splits the records at = and strips of spaces

                    if r in tempDic:                               # if the record is already in the tempdic add the info
                        tempDic[r] += 1
                    else:                                          # if not add record and info
                        tempDic[r] = 1

    results = []                                                   # results as a list 
    for k,v in tempDic.items():                                    # loops through key value pairs 
        result = "%010d\t%s" % (v, k)                              # results in a way that can be analyzed in a yml file
        results.append(result)                                     # puts together results 

    results = sorted(results, reverse=True)                        # sorts the results
    results = "\n".join(results)                                   # joins at new line 

    with open("bibtex_analysis.txt", "w", encoding="utf8") as f9:  # saves the results in a new file, with the encoding again; closes the file automatically
        f9.write(results)

bibAnalyze(vars['bib_all'])                                        # calls the function



