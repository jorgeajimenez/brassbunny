from rdkit.Chem import Draw
from rdkit import Chem
import os


def get_smiles_from_name(name):
    sample_meds = [
        ('lamotrigine', 'C1=CC(=C(C(=C1)Cl)Cl)C2=C(N=C(N=N2)N)N'),
        ('citalopram', 'CN(C)CCCC1(C2=C(CO1)C=C(C=C2)C#N)C3=CC=C(C=C3)F'),
        ('phenobarbital', 'CC1=CC=CC=C1OC(=O)N1C=CN1C(=O)C2C=CC=CC=C2')
    ]
    for med_name, smiles in sample_meds:
        if med_name == name:
            return smiles
    return None


def generate_molecule_images(drug_name, drug_smiles, output_format='png', save_dir='molecule_images'):
    os.makedirs(save_dir, exist_ok=True)
    img = Draw.MolToImage(Chem.MolFromSmiles(drug_smiles))
    img.save(os.path.join(save_dir, f'{drug_name}.{output_format}'))


test_test_drug_name = 'phenobarbital'
test_drug_smiles = get_smiles_from_name(test_test_drug_name)
if test_drug_smiles is not None:
    generate_molecule_images(test_test_drug_name, drug_smiles=test_drug_smiles)
