from server import mcp
import pandas as pd
from pathlib import Path
# from tdc.multi_pred import DDI
# from tdc.utils import get_label_map

# label_map = get_label_map(name='DrugBank', task='DDI')
# data = DDI(name='DrugBank').get_split()['test']
data = []

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

filename = 'FDA_Approved_structures.csv'
file_path = DATA_DIR / filename
approved_structures_dataframe = pd.read_csv(file_path)

drugbank_filename = 'DrugBank_Drugs_All.csv'
drugbank_file_path = DATA_DIR / drugbank_filename
drugbank_dataframe = pd.read_csv(drugbank_file_path)


@mcp.tool()
def get_smiles_from_drug_name(drug_name: str) -> str:
    """
    Retrieve the SMILES (Simplified Molecular Input Line Entry System) string for a given drug name from the 
    'FDA_Approved_structures.csv' file.

    Args:
        drug_name (str): The name of the drug (case-sensitive) for which the SMILES string is needed.

    Returns:
        str: The SMILES string corresponding to the given drug name if it exists in the file; 
             an empty string if the drug name is not found.

    Note:
        The data is sourced from the 'FDA_Approved_structures.csv' file located in the project's data directory.
    """
    try:
        result = approved_structures_dataframe.loc[approved_structures_dataframe['Name'] == drug_name, 'SMILES'].values[
            0]
        return result
    except IndexError:
        return ''


@mcp.tool()
def get_drug_drug_interaction(drug_name: str, drug_name_2: str) -> str:
    """
    Retrieve and check drug-drug interaction based on DrugBank IDs in the dataset.

    Args:
        drug_name (str): The name of the first drug (case-sensitive).
        drug_name_2 (str): The name of the second drug (case-sensitive).

    Returns:
        str: A message indicating if an interaction exists between the two drugs or not.

    Note:
        The data is sourced from the 'DrugBank_Drugs_All.csv' and 'DrugBank' datasets located in the project's data directory.
    """
    try:
        result = drugbank_dataframe.loc[drugbank_dataframe['Name'] == drug_name, 'DrugBank ID'].values[0]
        result_2 = drugbank_dataframe.loc[drugbank_dataframe['Name'] == drug_name_2, 'DrugBank ID'].values[0]

        # # Check if the combination exists in the 'data' object's 'Drug_1' and 'Drug_2' columns
        # for i, record in data.iterrows():
        #     d1id = record['Drug1_ID']
        #     d2id = record['Drug2_ID']
        #     if (d1id == result and d2id == result_2) or (d1id == result_2 and d2id == result):
        #         return record['Y']

    except IndexError:
        return f"One or both drugs ({drug_name}, {drug_name_2}) not found in DrugBank data."


l = get_drug_drug_interaction('Ritonavir', 'Cholecalciferol')
print(l)
