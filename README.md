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
>    │
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
