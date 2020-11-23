# comments to explain every line

import re
import yaml

"""
1. load bibtex file
    - bibliography should be curated in Zotero (one can program cleaning procedures into the script, but this is not as reliable);
    - loading bibtex data, keep only those records that have PDFs;
    - some processing might be necessary (like picking one file out of two and more)
2. convert into other formats
    - csv
    - json
    - yml
"""

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "z_config.yml"                                                     # variables in yml file to have all the settings in one place
settings = yaml.load(open(settingsFile))
bibKeys = yaml.load(open("zotero_biblatex_keys.yml"))

###########################################################
# FUNCTIONS ###############################################
###########################################################

# load bibTex Data into a dictionary
def bibLoad(bibTexFile):

    bibDic = {}                                                                  # creates a dicitonary 

    with open(bibTexFile, "r", encoding="utf8") as f1:                           # opens file with the encoding; automatically closes it again
        records = f1.read().split("\n@")                                         # reads through the recors in the file and splits at new line and @

        for record in records[1:]:                                               # loops through the records, ignoring first one (empty line)
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower():                                         # checks if the records have a pdf, lower - lower case letters

                record = record.strip().split("\n")[:-1]                         # strips the record of spaces and splits at new line; except for last one: }

                rType = record[0].split("{")[0].strip()                          # record type - splits at curley brackets, strips of spaces
                rCite = record[0].split("{")[1].strip().replace(",", "")         # citekey, splits at curley brackets, strips of spaces, replaces comma with space

                bibDic[rCite] = {}                                               # defining dictionary
                bibDic[rCite]["rCite"] = rCite                                   # citationkey
                bibDic[rCite]["rType"] = rType                                   # recordtype

                for r in record[1:]:                                             # loops through records
                    key = r.split("=")[0].strip()                                # splits into pairs at =; strips of space
                    val = r.split("=")[1].strip()                                # splits into pairs at = and strips of space
                    val = re.sub("^\{|\},?", "", val)                            # using regular expressions to format the values 

                    fixedKey = bibKeys[key]                                      # using the list of fixed keys as bibkeys

                    bibDic[rCite][fixedKey] = val                                # defining the dictionary


    print("="*80)                                                                # format in readable way
    print("NUMBER OF RECORDS IN BIBLIGORAPHY: %d" % len(bibDic))                 # again
    print("="*80)                                                                # again
    return(bibDic)                                                               # return the dictionary so that it can be used in the next steps 

# CONVERSION FUNCTIONS

import json                                                                      # import json to start converion 
def convertToJSON(bibTexFile):                                                   # new function 
    data = bibLoad(bibTexFile)                                                   # where we get data from
    with open(bibTexFile.replace(".bib", ".json"), 'w', encoding='utf8') as f9:  # opens the bibtexfile and saves it into the json file, with encoding; plus makes new file 
        json.dump(data, f9, sort_keys=True, indent=4, ensure_ascii=False)


import yaml
def convertToYAML(bibTexFile):
    data = bibLoad(bibTexFile)
    with open(bibTexFile.replace(".bib", ".yaml"), 'w', encoding='utf8') as f9:  #safes the bibtexfile as yaml file with the enocidng; makes new file
        yaml.dump(data, f9)

# CSV is the trickest because bibTeX is not symmetrical
def convertToCSV(bibTexFile):
    data = bibLoad(bibTexFile)
    # let's handpick fields that we want to save: citeKey, type, author, title, date
    headerList = ['citeKey', 'type', 'author', 'title', 'date'] 
    header = "\t".join(headerList)

    dataNew = [header]

    for k,v in data.items():                                                     # goes through the fields we picked to see if they are there;
        citeKey = k                                                              # if not it prints NA; because VSV has to be symmetrical

        if 'rType' in v:
            rType = v['rType']
        else:
            rType = "NA"

        if 'author' in v:
            author = v['author']
        else:
            author = "NA"

        if 'title' in v:
            title = v['title']
        else:
            title = "NA"

        if 'date' in v:
            date = v['date']
        else:
            date = "NA"

        tempVal = "\t".join([citeKey, rType, author, title, date])
        dataNew.append(tempVal)

    finalData = "\n".join(dataNew)
    with open(bibTexFile.replace(".bib", ".csv"), 'w', encoding='utf8') as f9:         # creates a new file, encoding, closes everything
        f9.write(finalData)


###########################################################
# RUN EVERYTHING ##########################################
###########################################################

print(settings["bib_all"])

#convertToJSON(settings["bib_all"])                                                 # remove hashtags to get the conversion you want
#convertToYAML(settings["bib_all"])
#convertToCSV(settings["bib_all"])


print("Done!")                                                                      # to see when it is actually done 