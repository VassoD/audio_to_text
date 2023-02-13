from speechmatics.models import ConnectionSettings, BatchTranscriptionConfig
from speechmatics.batch_client import BatchClient
# create a file called config.py and add your auth token(API) there
from config import AUTH_TOKEN
# path to the file to transcribe
PATH_TO_FILE = "file.wav"
# choose the language en for english, fr for french, es for spanish etc...
LANGUAGE = "fr"

settings = ConnectionSettings(
  url='https://asr.api.speechmatics.com/v2',
  auth_token=AUTH_TOKEN,
)
  
# Define transcription parameters
conf = BatchTranscriptionConfig(
  language=LANGUAGE,
)

# Open the client using a context manager
with BatchClient(settings) as client:

  job_id = client.submit_job(
    audio=PATH_TO_FILE,
    transcription_config=conf,
  )
  print(f'job {job_id} submitted successfully, waiting for transcript')
  
  # Note that in production, you should set up notifications instead of polling. 
  # Notifications are described here: https://docs.speechmatics.com/features-other/notifications
  transcript = client.wait_for_completion(job_id, transcription_format='txt')
  print(transcript)
  
  with open("transcription.txt", "w") as file:
    file.write(transcript)

