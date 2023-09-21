from conductor.client.configuration.settings.authentication_settings import AuthenticationSettings
from conductor.client.configuration.configuration import Configuration
from conductor.client.automator.task_handler import TaskHandler
from string_reverser_worker import StringReverserWorker

#### Add these lines if running on a mac####
#from multiprocessing import set_start_method
#set_start_method("fork")
############################################

SERVER_API_URL = 'https://play.orkes.io/api'
KEY_ID = 'f17f2eab-5398-4def-a6a4-08a03609e5b7'
KEY_SECRET = '8Kvny0WX0J5rmyyfnAhtg0Rh1WjM08lAVvi4n26oQGCLLnEe'

configuration = Configuration(
    server_api_url=SERVER_API_URL,
    debug=True,
    authentication_settings=AuthenticationSettings(
        key_id=KEY_ID,
        key_secret=KEY_SECRET
    ),
)

workers = [
    StringReverserWorker(
        task_definition_name='reverse'
    )
]

with TaskHandler(workers, configuration, scan_for_annotated_workers=False) as task_handler:
    task_handler.start_processes()
    task_handler.join_processes()
    task_handler.stop_processes()