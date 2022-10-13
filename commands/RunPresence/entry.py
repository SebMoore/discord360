import adsk.core
from ...lib import fusion360utils as futil
app = adsk.core.Application.get()
ui = app.userInterface
from ...pypresence import Presence
import time

# Local list of event handlers used to maintain a reference so
# they are not released and garbage collected.
local_handlers = []

def start():
    client_id = '1029740729129508974'
    global RPC
    RPC = Presence(client_id)
    RPC.connect()
    global currentDocumentName
    currentDocumentName = app.activeDocument.name
    global currentWorkspaceName
    currentWorkspaceName = ui.activeWorkspace.name
    global startTimestamp
    startTimestamp = time.time()
    RPC.update(large_image="logo", state="Workspace: {}".format(currentWorkspaceName), details="Working on {}".format(currentDocumentName), start=startTimestamp)



def documentChanged(DocumentEventArgs):
    global startTimestamp
    startTimestamp = time.time()
    global currentDocumentName
    currentDocumentName = DocumentEventArgs.document.name
    RPC.update(large_image="logo", state="Workspace: {}".format(currentWorkspaceName), details="Working on {}".format(currentDocumentName), start=startTimestamp)

def workspaceChanged(WorkspaceEventArgs):
    global currentWorkspaceName
    currentWorkspaceName = WorkspaceEventArgs.workspace.name
    RPC.update(large_image="logo", state="Workspace: {}".format(currentWorkspaceName), details="Working on {}".format(currentDocumentName), start=startTimestamp)


def stop():
    RPC.clear()
    RPC.close()

futil.add_handler(app.documentActivated, documentChanged, local_handlers=local_handlers)
futil.add_handler(ui.workspaceActivated, workspaceChanged, local_handlers=local_handlers)
