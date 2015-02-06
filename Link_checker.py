#!/usr/bin/python

from PySide import QtGui
import os
import subprocess
import sys
import shutil
import datetime

def main():
    """Look at:
    http://stackoverflow.com/questions/20657753/python-pyside-and-progress-bar-threading
    for an example of a progress bar code.
    """
    app = QtGui.QApplication([])
    dialog = QtGui.QFileDialog()
    default = "/home/damon/Documents/CODE/Programing/Python/IPython Notebook Folders (links)"
    default = "/home/damon/Documents/CODE/Programing/Python"
    dialog.setDirectory(default)
    dialog.setFileMode(QtGui.QFileDialog.ExistingFiles) #allow selection of multiple files
    dialog.filesSelected.connect(callback)
    dialog.setWindowTitle("Select files to check links and images in.")
    dialog.show()
    chose_ = dialog.exec_()
    sys.exit()
    
def callback(files):
    """http://mail.scipy.org/pipermail/ipython-dev/2014-September/015020.html
    """
    Message = """Links will be checked upon clicking OK. 
This process may take somme time, but you will 
be notified upon completion, or errors."""
    msgBox = QtGui.QMessageBox()
    msgBox.setText(Message)
    msgBox.exec_()
    cmd = 'python nblinkcheck "%s"'
    #path = files[0].rsplit('/',1)[0]
    #os.chdir(path)
    path = os.getcwd()
    #parts = path.rsplit('/',1)

    er = 0
    for f in files:
        name = f.split('/')[-1]
        
        try:
            update_message = "Checking %s\n"%name
            with open("Errors.txt",'a') as f:
                f.write(update_message)
            #shutil.copyfile(name, name+'.bak')
            subprocess.call(cmd%name,shell=True)
            with open("Errors.txt",'a') as f:
                f.write("Finished\n\n")

        except:
            error = "Failed for %s"%(name)
            print error
            log_error(path,error,er)
            msgBox = QtGui.QMessageBox()
            msgBox.setText(error)
            msgBox.exec_()
            er += 1
            if er>2:
                msgBox = QtGui.QMessageBox()
                msgBox.setText('Too many errors occured.\nEnding validation process')
                msgBox.exec_()
                break
    msgBox = QtGui.QMessageBox()
    
    msgBox.setText('Checking process is complete.\nErrors recorded in Errors.txt')
    msgBox.exec_()
    
def log_error(path,message,count):
    if count == 0:
        Date = '\n\n'+datetime.datetime.now()
    else:
        Date = ''
    if path[-1] != '/':
        file_path = path+'/'+'error.log'
    else:
        file_path = path+'error.log'
    try:
        with open(file_path,'r')as f:
            er_text = f.read()
    except:
        er_text = ''
    er_text += Date+'\n'+message
    with open(file_path,'w')as f:
        f.write(er_text)
    
if __name__ == '__main__':
    main()
