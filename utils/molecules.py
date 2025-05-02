from rdkit.Chem import Draw
from rdkit import Chem


def generate_molecule_images(medications, output_format):
    for name, smiles in medications:
        img = Draw.MolToImage(Chem.MolFromSmiles(smiles))
        img.save(f'{name}.{output_format}')


sample_meds = [
    ('lamotrigine', 'C1=CC(=C(C(=C1)Cl)Cl)C2=C(N=C(N=N2)N)N'),
    ('citalopram', 'CN(C)CCCC1(C2=C(CO1)C=C(C=C2)C#N)C3=CC=C(C=C3)F')
]

generate_molecule_images(sample_meds, 'png')

