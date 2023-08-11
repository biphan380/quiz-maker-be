import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))

from llama_index import SimpleDirectoryReader
# Make our printing look nice
from llama_index.schema import MetadataMode

def load_docs(filepath):
    loader = SimpleDirectoryReader(
        input_dir=filepath,
        recursive=True
    )

    return loader.load_data()

# load our documents from each folder.
# we keep them seperate for now, in order to create separate indexes later

# load the recent provincial offences act
recent_act = load_docs("docs/recent_act")

# load the old provincial offences act
old_act = load_docs("docs/old_act")
