from pointwise import GlyphClient
from pointwise.glyphapi import *
import sys
import time
from .get import *

def connectPort(port=0,result=None):   
    """
    Connects to a Pointwise license. 
    For GUI: Script > Glyph Server > Active & port=2807

    Arguments:
    port: 0 for batch mode, 2807 for GUI
    result: None  - Will keep pinging server if no license 
            False - Only look for license once
            
    Returns:
    pw,glf
    """
    print('Looking for license...')
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    
    while result is None:
        try:
            glf = GlyphClient(port=port)
            pw = glf.get_glyphapi()
            print('\nConnected to Pointwise, port {}'.format(port))
            return pw,glf
        
        except:
            if port==2807:  
                print(' Cannot connect to Pointwise. Ensure Glyph server is active. Close function panels and end Glyph journalling')
                sys.stdout.write("\r")
                sys.stdout.flush()
                # sys.stdout.write("\r")
                
            else:
                print(' No Pointwise license')
        
        for i in range(10,0,-1):
        
            sys.stdout.write('\rWaiting to retry in... '+str(i)+' \r')
            sys.stdout.flush()
            time.sleep(1)
            if i == 1:
                print(LINE_UP,LINE_UP)
            
def disconnectPW():
    """
    Disconnects from a Pointwise license. Does not take arguments. 
    """
    pw = 0
    glf = 0
    print('Disconnected from Pointwise License')

def reset(pw):
    pw.Application.reset()
    
def clearModified(pw):
    pw.Application.clearModified()
        
def setDefaultDimension(pw,dim=0):
    pw.Connector.setDefault('Dimension',dim)
 
def setUndoMaximumLevels(pw,levels=5):
    pw.Application.setUndoMaximumLevels(levels)
          
def delete(pw,ents):
    """
    Deletes pointwise entities.

    Arguments:
    pw: Must be connected to Pointwise instance
    ents: Entities to delete. Accepts defined entities and string names. May have to be a list? 
            
    Examples:
    delete(pw,getByType(pw,'Connector'))
    delete(pw,[surf1,surf2])
    """
    try:
        for ent in ents:
            if type(ent) == str:
                try: 
                    ent = getByName(pw,ent)
                except:
                    print("No entity by name: {}".format(ent))
            ent.delete()
    except:
        ent = ents
        if type(ent) == str:
            try: 
                ent = getByName(pw,ent)
            except:
                print("No entity by name: {}".format(ent))
            ent.delete()
        
def deleteSpecial(pw,ents):
    pw.Entity.checkDelete('-freed',ents)
    pw.Entity.delete(ents)
    pw.Application.markUndoLevel('Delete Special')

def save(pw,fileloc,env=0):
    #C:/location/filename.pw
    if env == 1:
        pw.Application.save('-environment',fileloc)
    else:
        pw.Application.save(fileloc)
        
def projectLoader(pw,fileloc,defer=0,append=False):
    with pw.Application.begin('ProjectLoader') as loader:
        loader.initialize(fileloc)
        loader.setRepairMode('Defer')
        loader.setAppendMode(append)
        loader.load() 
    pw.Application.markUndoLevel('Append')

def undo(pw):
    pw.Application.undo()

def save(pw,filename):
    pw.Application.save(filename)    