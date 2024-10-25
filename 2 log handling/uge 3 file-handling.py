
import io
###
# I have interpreted the assignment as if it is supposed to sort out all the logtypes in one file
# But having the logtypes ordered 
###


def main():
    sort_log("app_log (logfil analyse) 1.txt")

        
                  
                    
def sort_log(oldfile):
    newfile = "./log2.txt"
 
    # open file
    with open(newfile, 'w') as file, open(oldfile, 'r', encoding='utf-8') as infile:
        for line in infile:   
            if "ERROR" in line:
                file.write(line)
        infile.seek(0)
        for line in infile:
            if "SUCCES" in line:
                file.write(line)
        infile.seek(0)
        for line in infile:
            if "INFO" in line:
                file.write(line)
        infile.seek(0)
        for line in infile:
            if "WARNING" in line:
                file.write(line)

  # older version (slightly slower I imagine, becasue of increased overhead 
  # by having to determine different string values to put in different lists
  # and therefore switching between memory allocation spaces more often)

# def sort_log(oldfile):
#     newfile = "./log.txt"
#     # Containers for each file type
#     Error = []
#     Succes = []
#     Info = []
#     Warning = []

    # open file
    # with open(newfile, 'w') as file, open(oldfile, 'r', encoding='utf-8') as infile:
    #     for line in infile:
    #         # Insert each log type into the correct container
    #         if "ERROR" in line:
    #             Error.append(line)
    #         if "SUCCES" in line:
    #             Succes.append(line)
    #         if "INFO" in line:
    #             Info.append(line)
    #         if "WARNING" in line:
    #             Warning.append(line)
    #     # Write the log types to the log file in order of type
    #     for i in Error:
    #             file.write(i)
    #     for i in Succes:
    #         file.write(i)
    #     for i in Info: 
    #         file.write(i)
    #     for i in Warning:
    #         file.write(i)




    # older version (using regex to discover groupes of logtypes it self, but in a way very redundant - also not finished) (KISS)

                # import re
         #         file.write(line)
       # for line in infile:
       #      log = re.search(r"[A-Z]+", line)
       #      if log:
       #          logtype = log.group()
       #          for line in infile:
       #              if logtype in line:
       #                  file.write(line)



if __name__ == '__main__':
    main()
