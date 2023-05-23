from duckduckgo_search import ddg_images
from fastcore.all import *

def search_images(term, max_images=30):
    ddg_images_result = ddg_images(term, max_results=max_images)
    fcore_list = L(ddg_images_result).itemgot("image")
    return fcore_list
