# Tool for metasearching
This is a prototype of the tool implementing a mechanism to find the real news on the internet.

## Structure
```bash
├── README.md
├── tasks.md
├── search.py - main part executes the search process
├── result_item.py - definition of the class to pack a search result item
│   ├── String title
│   ├── String url
│   ├── String engine
│   ├── Integer rank
│   ├── String abstract
│   ├── void __init__(title, url, engine)
│   ├── void add_rank(rank) - Setter for rank variable
│   ├── void add_abstract(abstract) - Setter for abstract variable
│   ├── String get_domain(void) - Returns the domain such as "google.com"
├── [Directory] classification_data - package of the materials such as URL to be used for detecting specific category of result items
├── [Directory] google_module - incompleted module to obtain search result from Google
├── [Directory] yahoo_module - incompleted module to obtain search result from Google
├── [Directory] baidu_module - incompleted module to obtain search result from Google
├── [Directory] bing_module - incompleted module to obtain search result from Google
├── [Directory] yandex_module - incompleted module to obtain search result from Google
```