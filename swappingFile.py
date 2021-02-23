import os
import shutil
import time

def main():
    deleted_folder_count=0
    deleted_files_count=0
     
    path='/path_to_delete'
    days=30
    seconds=time.time()-(days * 24 * 60 * 60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds>=get_fileorfolderage(root_folder):
                remove_folder(root_folder)
                deleted_folder_count=deleted_folder_count+1
                break
            else:
                 for folder in folders:
                    file_path=os.path.join(root_folder,file)
                    if seconds>=get_fileorfolderage(folder_path):
                            remove_folder(folder_path)
                            deleted_folder_count=deleted_folder_count+1
            

def get_fileorfolderage(path):
    ctime=os.stat(path).st_ctime
    return ctime            

def remove_file(path): 
    #removing the file
     if not os.remove(path):
    # success message 
            print(f"{path} is removed successfully")
        
     else: 
         print("Unable to delete the "+path)


def remove_folder(path): 
    #removing the folder
     if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    # success message 
     else: print("Unable to delete the "+path)    