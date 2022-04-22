# Project Setup
1. Change Python version to `{ your_python_version }` (like `3.7`) @ `./Pipfile`
2. Setup environment
    ```
    rm Pipfile.lock
    pip install pipenv
    pipenv shell
    pipenv install
    ```
3. open `./src/main.ipynb` and run all cell