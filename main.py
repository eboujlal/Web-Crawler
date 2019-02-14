import os

projects_dir = "projects/"

# Each website with its own folder :D
def create_new_project(project_name,base_url):
    if not os.path.exists(projects_dir+project_name):
        os.makedirs(projects_dir+project_name)
        logthis("---- Start Copyright ----",project_name)
        logthis("---- Version 0.1.0 ----",project_name)
        logthis("---- Date : 10 August 2017 ----",project_name)
        logthis("---- Designed for Crawling Orienation Chabab ----",project_name)
        logthis("---- Developped By Marouane Boujlal ----",project_name)
        logthis("---- Inspired by thenewboston ----",project_name)
        logthis("---- End Copyright ----",project_name)
        logthis("---- Start ----",project_name)
        logthis("Main. Start Preparing environement",project_name)
        logthis("Main. Creating "+project_name+" project ...",project_name)
        logthis("Main. Generate data files for "+project_name+" project ...",project_name)
        create_data_files(project_name,base_url)
        logthis("Main. End Preparing environement",project_name)

# Generate Data Files
def create_data_files(project_name,base_url):
    queue = projects_dir+project_name+"/queue.txt";
    crowled = projects_dir+project_name+"/crawled.txt";
    log = projects_dir+project_name+"/log.txt";
    torecheck = projects_dir+project_name+"/torecheck.txt";
    if not os.path.exists(queue):
        write_file(queue,base_url)
    if not os.path.exists(crowled):
        write_file(crowled,'')
    if not os.path.exists(log):
        write_file(log,'')    
    if not os.path.exists(torecheck):
        write_file(torecheck,'')
    logthis("Main. Files are generated ...",project_name)
    
# Create new files
def write_file(path,data):
    f = open(path,"w")
    f.write(data)
    f.close

# Append data to file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')
# remove content of file    
def delete_file_contents(path):
    with open(path,'w'):
        pass 

# Convert a file to set    
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as f:
        for line in f :
            results.add(line.replace('\n',''))
    return results

# Convert a set to file
def set_to_file(links,file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)
def main_dir():
    return projects_dir
# Create new project
def init_project(project_name,base_url):
    create_new_project(project_name,base_url)

def logthis(text,project_name):
    print(text)
    append_to_file(projects_dir+project_name+"/log.txt",text)
    
def recheckThisWebsite(link,project_name):
    append_to_file(projects_dir+project_name+"/torecheck.txt",text)