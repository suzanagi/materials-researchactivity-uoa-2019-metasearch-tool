import sys
import result_item
from google_module import google_search_module as google
from yahoo_module import yahoo_search_module as yahoo
from bing_module import bing_search_module as bing
from baidu_module import baidu_search_module as baidu

# Collect the search results from each search modules
def metasearch(query):
    results = list()
    for item in google.search(query):
        results.append(item)
    for item in yahoo.search(query):
        results.append(item)
    for item in bing.search(query):
        results.append(item)
    for item in baidu.search(query):
        results.append(item)
    return results

# Main Function
if __name__ == "__main__":
    #Prepare query variable
    query = sys.argv[1]
    # Append multiple query words with "+"
    for arg in sys.argv[2:]:
        query = query + "+" + arg
    # Experiment the search function
    result = metasearch(query)
    # Print the result list to the command line
    for item in result:
        print("[title] "+item.title)
        print("[url] "+item.url)
