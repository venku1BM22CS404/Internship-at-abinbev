import pandas as pd
import pyodbc
import import_ipynb
import xlrd
import os
import warnings
import subprocess
import nbformat
from nbconvert import PythonExporter
from nbclient import NotebookClient

def run_notebook(notebook_path, output_path):
    """
    Execute a Jupyter notebook from a py file and save the output to a new/same notebook.
    """
    # Read the notebook
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    # Execute the notebook
    client = NotebookClient(nb)
    client.execute()

    # Save the executed notebook
    with open(output_path, 'w') as f:
        nbformat.write(nb, f)
    

def main():
    """
    Run the D0 deployment pipeline.
    """
    warnings.filterwarnings("ignore")

    #Run file_paths.py to generate the necessary folder structure (to be utilized by downstream notebooks)
    with open('file_paths.py', 'r') as file:
        code = file.read()
        exec(code)

    #Run notebooks in sequence
    run_notebook( "d0_sql_connection.ipynb", "d0_sql_connection.ipynb")
    run_notebook( "d0_sql_query.ipynb", "d0_sql_query.ipynb")
    run_notebook( "d0_preprocessing.ipynb", "d0_preprocessing.ipynb")
    return
if __name__ == "__main__":
    main()