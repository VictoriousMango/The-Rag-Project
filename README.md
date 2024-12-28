# The-Rag-Project

## Virtual Environment
### To Create a Virutual Environment
```
python -m venv venv
```  
### To activate virtual environment
```
venv\Scripts\activate
```    
### To deactivate virtual environment
```
venv\Scripts\deactivate
```    

## File Structure
> [!NOTE]  
>```bash
> project/
>    │
>    ├── core/
>    │   ├── retriever.py
>    │   ├── generator.py
>    │   ├── preprocessor.py
>    │   ├── postprocessor.py
>    │   ├── embedding.py
>    │lj
>    ├── utils/
>    │   ├── config.py
>    │   ├── utils.py
>    │   ├── constants.py
>    │
>    ├── data/
>    │   ├── data_loader.py
>    │   ├── indexer.py
>    │   ├── prompt_builder.py
>    │
>    ├── integration/
>    │   ├── pipeline.py
>    │   ├── app.py
>    │
>    ├── tests/
>    │   ├── test_retriever.py
>    │   ├── test_generator.py
>    │   ├── test_preprocessor.py
>    │   ├── test_pipeline.py
>    │
>    ├── docs/
>    │   ├── architecture.md
>    │   ├── usage_guide.md
>    │
>    ├── README.md
>    ├── requirements.txt
>```

## Testing Individual Files
Sample Run Commands
```
cd .\codeAssets\
python -m core.retriever
```
## Showing Logs in Web Browser 
```
python -m http.server
```
> [!NOTE]
> There should be an HTML file, which should be responsible for showing logs in some format, 
> name of the HTML should be ```index.html```.