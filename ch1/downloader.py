from fastdownload import download_url
from duckduckgo import search_images
import os

def get_files(term):
    result = search_images(term)
    
    for resultItems in result.items:
        filename = os.path.basename(resultItems)
        download_url(resultItems, f'./ch1/images/{filename}',show_progress=False)

get_files("cute_puppies")