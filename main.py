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

from llama_index import ServiceContext, set_global_service_context
from llama_index.llms import OpenAI

# create a global service context
service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-4", temperature=0))
set_global_service_context(service_context)

from llama_index import VectorStoreIndex, StorageContext, load_index_from_storage

# create a vector store index for each folder
# try and load the index if already made, else make it
try:
    recent_act_index = load_index_from_storage(StorageContext.from_defaults(persist_dir="./recent_act_index"))
    old_act_index = load_index_from_storage(StorageContext.from_defaults(persist_dir="./old_act_index/"))

except:
    recent_act_index = VectorStoreIndex.from_documents(recent_act)
    recent_act_index.storage_context.persist(persist_dir="./recent_act_index")
    old_act_index = VectorStoreIndex.from_documents(old_act)
    old_act_index.storage_context.persist(persist_dir="./old_act_index")