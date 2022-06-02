import streamlit as st
import pandas as pd
import pickle
import chemparse
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier



f_rt = open('./notebooks/final_rt_model_pipe','rb')
role_type_model = pickle.load(f_rt)
f_rt.close()

f_bio_type = open('./notebooks/final_rn_bio_model_pipe', 'rb')
bio_name_model = pickle.load(f_bio_type)
f_bio_type.close()

f_chem_type = open('./notebooks/final_rn_chem_model_pipe', 'rb')
chem_name_model = pickle.load(f_chem_type)
f_chem_type.close()

f_app_type = open('./notebooks/final_rn_app_model_pipe', 'rb')
app_name_model = pickle.load(f_app_type)
f_app_type.close()

st.title('Natural Product Classifier')
st.write('## This app takes in a newly discovered naturally occuring compound')
st.write('#### It then predicts the type of role it has in a drug pipeline ')


MolecularFormula = st.text_input('Molecular Formula')
MolecularWeight = st.number_input('Molecular Weight')
XLogP = st.number_input('XLogP')
ExactMass = st.number_input('Exact Mass')
MonoisotopicMass = st.number_input('Monoisotopic Mass')
TPSA = st.number_input('Topological Polar Surface Area')
Complexity = st.number_input('Complexity')
Charge = st.number_input('Formal Charge')
HBondDonorCount = st.number_input('Number of Hydrogen Bond Donors')
HBondAcceptorCount = st.number_input('Number of Hydrogen Bond Acceptors')
RotatableBondCount = st.number_input('Number of Rotatable Bonds')
HeavyAtomCount = st.number_input('Number of Heavy Atoms')
IsotopeAtomCount = st.number_input('Number of Isotopic Atoms')
AtomStereoCount = st.number_input('Number of Seteroisomeric Atoms')
DefinedAtomStereoCount = st.number_input('Number of Defined Stereoisomeric Atoms')
UndefinedAtomStereoCount = st.number_input('Number of Undefined Stereoisomeric Atoms')
BondStereoCount = st.number_input('Number of Bond Stereocenters')



def role_type_parse(MolecularFormula, MolecularWeight, XLogP, ExactMass, MonoisotopicMass, 
              TPSA, Complexity, Charge, HBondDonorCount, HBondAcceptorCount, RotatableBondCount, 
              HeavyAtomCount, IsotopeAtomCount, AtomStereoCount, DefinedAtomStereoCount, 
              UndefinedAtomStereoCount, BondStereoCount):
    
    elements = ['H',
                 'He',
                 'Li',
                 'Be',
                 'B',
                 'C',
                 'N',
                 'O',
                 'F',
                 'Ne',
                 'Na',
                 'Mg',
                 'Al',
                 'Si',
                 'P',
                 'S',
                 'Cl',
                 'A',
                 'K',
                 'Ca',
                 'Sc',
                 'Ti',
                 'V',
                 'Cr',
                 'Mn',
                 'Fe',
                 'Co',
                 'Ni',
                 'Cu',
                 'Zn',
                 'Ga',
                 'Ge',
                 'As',
                 'Se',
                 'Br',
                 'Kr',
                 'Rb',
                 'Sr',
                 'Y',
                 'Zr',
                 'Nb',
                 'Mo',
                 'Tc',
                 'Ru',
                 'Rh',
                 'Pd',
                 'Ag',
                 'Cd',
                 'In',
                 'Sn',
                 'Sb',
                 'Te',
                 'I',
                 'Xe',
                 'Cs',
                 'Ba',
                 'La',
                 'Ce',
                 'Pr',
                 'Nd',
                 'Pm',
                 'Sm',
                 'Eu',
                 'Gd',
                 'Tb',
                 'Dy',
                 'Ho',
                 'Er',
                 'Tm',
                 'Yb',
                 'Lu',
                 'Hf',
                 'Ta',
                 'W',
                 'Re',
                 'Os',
                 'Ir',
                 'Pt',
                 'Au',
                 'Hg',
                 'Ti',
                 'Pb',
                 'Bi',
                 'Po',
                 'At',
                 'Rn',
                 'Fr',
                 'Ra',
                 'Ac',
                 'Th',
                 'Pa',
                 'U']
    
    
    data = {'Molecular_formula':[MolecularFormula], 
            'Molecular_weight': [MolecularWeight], 
            'XLogP': [XLogP], 
            'Exact_mass': [ExactMass], 
            'Monoisotpic_mass':[MonoisotopicMass], 
            'TPSA':[TPSA], 
            'Complexity':[Complexity], 
            'Charge': [Charge],
            'HBond_donor_count':[HBondDonorCount], 
            'HBond_acceptor_count':[HBondAcceptorCount], 
            'Rotatable_bond_count':[RotatableBondCount], 
            'Heavy_atom_count':[HeavyAtomCount], 
            'Isotope_atom_count':[IsotopeAtomCount], 
            'Atom_stereo_count':[AtomStereoCount], 
            'Defined_atom_stereo_count':[DefinedAtomStereoCount], 
            'Undefine_atom_stereo_count':[UndefinedAtomStereoCount], 
            'Bond_stereo_count':[BondStereoCount]}
    
    f=chemparse.parse_formula(MolecularFormula)
    
    for e in range(len(elements)):
           
        if(elements[e] in f):
            
            data.update(f)
                
        else:
            
            data[elements[e]] = 0   
 
    
    del data['Molecular_formula']
    
    X = pd.DataFrame.from_dict(data)
    
    role_type_pred = role_type_model.predict(X)[0]

    return role_type_pred




def bio_role_name_parse(MolecularFormula, MolecularWeight, XLogP, ExactMass, MonoisotopicMass, 
              TPSA, Complexity, Charge, HBondDonorCount, HBondAcceptorCount, RotatableBondCount, 
              HeavyAtomCount, IsotopeAtomCount, AtomStereoCount, DefinedAtomStereoCount, 
              UndefinedAtomStereoCount, BondStereoCount):
    
    elements = ['H',
                 'He',
                 'Li',
                 'Be',
                 'B',
                 'C',
                 'N',
                 'O',
                 'F',
                 'Ne',
                 'Na',
                 'Mg',
                 'Al',
                 'Si',
                 'P',
                 'S',
                 'Cl',
                 'A',
                 'K',
                 'Ca',
                 'Sc',
                 'Ti',
                 'V',
                 'Cr',
                 'Mn',
                 'Fe',
                 'Co',
                 'Ni',
                 'Cu',
                 'Zn',
                 'Ga',
                 'Ge',
                 'As',
                 'Se',
                 'Br',
                 'Kr',
                 'Rb',
                 'Sr',
                 'Y',
                 'Zr',
                 'Nb',
                 'Mo',
                 'Tc',
                 'Ru',
                 'Rh',
                 'Pd',
                 'Ag',
                 'Cd',
                 'In',
                 'Sn',
                 'Sb',
                 'Te',
                 'I',
                 'Xe',
                 'Cs',
                 'Ba',
                 'La',
                 'Ce',
                 'Pr',
                 'Nd',
                 'Pm',
                 'Sm',
                 'Eu',
                 'Gd',
                 'Tb',
                 'Dy',
                 'Ho',
                 'Er',
                 'Tm',
                 'Yb',
                 'Lu',
                 'Hf',
                 'Ta',
                 'W',
                 'Re',
                 'Os',
                 'Ir',
                 'Pt',
                 'Au',
                 'Hg',
                 'Ti',
                 'Pb',
                 'Bi',
                 'Po',
                 'At',
                 'Rn',
                 'Fr',
                 'Ra',
                 'Ac',
                 'Th',
                 'Pa',
                 'U']
    
    
    data = {'Molecular_formula':[MolecularFormula], 
            'Molecular_weight': [MolecularWeight], 
            'XLogP': [XLogP], 
            'Exact_mass': [ExactMass], 
            'Monoisotpic_mass':[MonoisotopicMass], 
            'TPSA':[TPSA], 
            'Complexity':[Complexity], 
            'Charge': [Charge],
            'HBond_donor_count':[HBondDonorCount], 
            'HBond_acceptor_count':[HBondAcceptorCount], 
            'Rotatable_bond_count':[RotatableBondCount], 
            'Heavy_atom_count':[HeavyAtomCount], 
            'Isotope_atom_count':[IsotopeAtomCount], 
            'Atom_stereo_count':[AtomStereoCount], 
            'Defined_atom_stereo_count':[DefinedAtomStereoCount], 
            'Undefine_atom_stereo_count':[UndefinedAtomStereoCount], 
            'Bond_stereo_count':[BondStereoCount]}
    
    f=chemparse.parse_formula(MolecularFormula)
    
    for e in range(len(elements)):
           
        if(elements[e] in f):
            
            data.update(f)
                
        else:
            
            data[elements[e]] = 0   
 
    
    del data['Molecular_formula']
    
    X = pd.DataFrame.from_dict(data)
    
    bio_role_name_pred = bio_name_model.predict(X)[0]

    return bio_role_name_pred



def chem_role_name_parse(MolecularFormula, MolecularWeight, XLogP, ExactMass, MonoisotopicMass, 
              TPSA, Complexity, Charge, HBondDonorCount, HBondAcceptorCount, RotatableBondCount, 
              HeavyAtomCount, IsotopeAtomCount, AtomStereoCount, DefinedAtomStereoCount, 
              UndefinedAtomStereoCount, BondStereoCount):
    
    elements = ['H',
                 'He',
                 'Li',
                 'Be',
                 'B',
                 'C',
                 'N',
                 'O',
                 'F',
                 'Ne',
                 'Na',
                 'Mg',
                 'Al',
                 'Si',
                 'P',
                 'S',
                 'Cl',
                 'A',
                 'K',
                 'Ca',
                 'Sc',
                 'Ti',
                 'V',
                 'Cr',
                 'Mn',
                 'Fe',
                 'Co',
                 'Ni',
                 'Cu',
                 'Zn',
                 'Ga',
                 'Ge',
                 'As',
                 'Se',
                 'Br',
                 'Kr',
                 'Rb',
                 'Sr',
                 'Y',
                 'Zr',
                 'Nb',
                 'Mo',
                 'Tc',
                 'Ru',
                 'Rh',
                 'Pd',
                 'Ag',
                 'Cd',
                 'In',
                 'Sn',
                 'Sb',
                 'Te',
                 'I',
                 'Xe',
                 'Cs',
                 'Ba',
                 'La',
                 'Ce',
                 'Pr',
                 'Nd',
                 'Pm',
                 'Sm',
                 'Eu',
                 'Gd',
                 'Tb',
                 'Dy',
                 'Ho',
                 'Er',
                 'Tm',
                 'Yb',
                 'Lu',
                 'Hf',
                 'Ta',
                 'W',
                 'Re',
                 'Os',
                 'Ir',
                 'Pt',
                 'Au',
                 'Hg',
                 'Ti',
                 'Pb',
                 'Bi',
                 'Po',
                 'At',
                 'Rn',
                 'Fr',
                 'Ra',
                 'Ac',
                 'Th',
                 'Pa',
                 'U']
    
    
    data = {'Molecular_formula':[MolecularFormula], 
            'Molecular_weight': [MolecularWeight], 
            'XLogP': [XLogP], 
            'Exact_mass': [ExactMass], 
            'Monoisotpic_mass':[MonoisotopicMass], 
            'TPSA':[TPSA], 
            'Complexity':[Complexity], 
            'Charge': [Charge],
            'HBond_donor_count':[HBondDonorCount], 
            'HBond_acceptor_count':[HBondAcceptorCount], 
            'Rotatable_bond_count':[RotatableBondCount], 
            'Heavy_atom_count':[HeavyAtomCount], 
            'Isotope_atom_count':[IsotopeAtomCount], 
            'Atom_stereo_count':[AtomStereoCount], 
            'Defined_atom_stereo_count':[DefinedAtomStereoCount], 
            'Undefine_atom_stereo_count':[UndefinedAtomStereoCount], 
            'Bond_stereo_count':[BondStereoCount]}
    
    f=chemparse.parse_formula(MolecularFormula)
    
    for e in range(len(elements)):
           
        if(elements[e] in f):
            
            data.update(f)
                
        else:
            
            data[elements[e]] = 0   
 
    
    del data['Molecular_formula']
    
    X = pd.DataFrame.from_dict(data)
    
    chem_role_name_pred = chem_name_model.predict(X)[0]

    return chem_role_name_pred


def app_role_name_parse(MolecularFormula, MolecularWeight, XLogP, ExactMass, MonoisotopicMass, 
              TPSA, Complexity, Charge, HBondDonorCount, HBondAcceptorCount, RotatableBondCount, 
              HeavyAtomCount, IsotopeAtomCount, AtomStereoCount, DefinedAtomStereoCount, 
              UndefinedAtomStereoCount, BondStereoCount):
    
    elements = ['H',
                 'He',
                 'Li',
                 'Be',
                 'B',
                 'C',
                 'N',
                 'O',
                 'F',
                 'Ne',
                 'Na',
                 'Mg',
                 'Al',
                 'Si',
                 'P',
                 'S',
                 'Cl',
                 'A',
                 'K',
                 'Ca',
                 'Sc',
                 'Ti',
                 'V',
                 'Cr',
                 'Mn',
                 'Fe',
                 'Co',
                 'Ni',
                 'Cu',
                 'Zn',
                 'Ga',
                 'Ge',
                 'As',
                 'Se',
                 'Br',
                 'Kr',
                 'Rb',
                 'Sr',
                 'Y',
                 'Zr',
                 'Nb',
                 'Mo',
                 'Tc',
                 'Ru',
                 'Rh',
                 'Pd',
                 'Ag',
                 'Cd',
                 'In',
                 'Sn',
                 'Sb',
                 'Te',
                 'I',
                 'Xe',
                 'Cs',
                 'Ba',
                 'La',
                 'Ce',
                 'Pr',
                 'Nd',
                 'Pm',
                 'Sm',
                 'Eu',
                 'Gd',
                 'Tb',
                 'Dy',
                 'Ho',
                 'Er',
                 'Tm',
                 'Yb',
                 'Lu',
                 'Hf',
                 'Ta',
                 'W',
                 'Re',
                 'Os',
                 'Ir',
                 'Pt',
                 'Au',
                 'Hg',
                 'Ti',
                 'Pb',
                 'Bi',
                 'Po',
                 'At',
                 'Rn',
                 'Fr',
                 'Ra',
                 'Ac',
                 'Th',
                 'Pa',
                 'U']
    
    
    data = {'Molecular_formula':[MolecularFormula], 
            'Molecular_weight': [MolecularWeight], 
            'XLogP': [XLogP], 
            'Exact_mass': [ExactMass], 
            'Monoisotpic_mass':[MonoisotopicMass], 
            'TPSA':[TPSA], 
            'Complexity':[Complexity], 
            'Charge': [Charge],
            'HBond_donor_count':[HBondDonorCount], 
            'HBond_acceptor_count':[HBondAcceptorCount], 
            'Rotatable_bond_count':[RotatableBondCount], 
            'Heavy_atom_count':[HeavyAtomCount], 
            'Isotope_atom_count':[IsotopeAtomCount], 
            'Atom_stereo_count':[AtomStereoCount], 
            'Defined_atom_stereo_count':[DefinedAtomStereoCount], 
            'Undefine_atom_stereo_count':[UndefinedAtomStereoCount], 
            'Bond_stereo_count':[BondStereoCount]}
    
    f=chemparse.parse_formula(MolecularFormula)
    
    for e in range(len(elements)):
           
        if(elements[e] in f):
            
            data.update(f)
                
        else:
            
            data[elements[e]] = 0   
 
    
    del data['Molecular_formula']
    
    X = pd.DataFrame.from_dict(data)
    
    app_role_name_pred = app_name_model.predict(X)[0]

    return app_role_name_pred


    
run = st.button('Predict')

if run:
    
    results_type = role_type_parse(MolecularFormula, MolecularWeight, XLogP, ExactMass, 
                        MonoisotopicMass, TPSA, Complexity, Charge, HBondDonorCount, 
                        HBondAcceptorCount, RotatableBondCount, HeavyAtomCount, 
                        IsotopeAtomCount, AtomStereoCount, DefinedAtomStereoCount, 
                        UndefinedAtomStereoCount, BondStereoCount)
   
    
    if results_type == 'biological role':
        
        results_name_bio = bio_role_name_parse(MolecularFormula, MolecularWeight, XLogP, ExactMass, 
                        MonoisotopicMass, TPSA, Complexity, Charge, HBondDonorCount, 
                        HBondAcceptorCount, RotatableBondCount, HeavyAtomCount, 
                        IsotopeAtomCount, AtomStereoCount, DefinedAtomStereoCount, 
                        UndefinedAtomStereoCount, BondStereoCount)
        st.write(f'This unknown compound is most likely a {results_name_bio}, which has a {results_type} in drug development.')
    
    if results_type == 'chemical role':
        
        results_name_chem = chem_role_name_parse(MolecularFormula, MolecularWeight, XLogP, ExactMass, 
                        MonoisotopicMass, TPSA, Complexity, Charge, HBondDonorCount, 
                        HBondAcceptorCount, RotatableBondCount, HeavyAtomCount, 
                        IsotopeAtomCount, AtomStereoCount, DefinedAtomStereoCount, 
                        UndefinedAtomStereoCount, BondStereoCount)
        st.write(f'This unknown compound is most likely a {results_name_chem}, which has a {results_type} in drug development.')
    
    
    if results_type == 'application':
        
        results_name_app = app_role_name_parse(MolecularFormula, MolecularWeight, XLogP, ExactMass, 
                        MonoisotopicMass, TPSA, Complexity, Charge, HBondDonorCount, 
                        HBondAcceptorCount, RotatableBondCount, HeavyAtomCount, 
                        IsotopeAtomCount, AtomStereoCount, DefinedAtomStereoCount, 
                        UndefinedAtomStereoCount, BondStereoCount)
        
        st.write(f'This unknown compound is most likely a {results_name_app}') 
        st.write(f'This is a medical {results_type} in the pharmaceutical industry.')
    
        
   
    
    

    
    