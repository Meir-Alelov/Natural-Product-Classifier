# natural_product_classifier
Classifies natural products based on chemical and physical properties into specific drug pipelines

this is why natural products

Natural products and their structural analogues have historically made a major contribution to pharmacotherapy, especially for cancer and infectious diseases. Nevertheless, natural products also present challenges for drug discovery, such as technical barriers to screening, isolation, characterization and optimization, which contributed to a decline in their pursuit by the pharmaceutical industry from the 1990s onwards. In recent years, several technological and scientific developments — including improved analytical tools, genome mining and engineering strategies, and microbial culturing advances — are addressing such challenges and opening up new opportunities. Consequently, interest in natural products as drug leads is being revitalized, particularly for tackling antimicrobial resistance. 

NPs offer special features in comparison with conventional synthetic molecules, which confer both advantages and challenges for the drug discovery process. NPs are characterized by enormous scaffold diversity and structural complexity. They typically have a higher molecular mass, a larger number of sp3 carbon atoms and oxygen atoms but fewer nitrogen and halogen atoms, higher numbers of H-bond acceptors and donors, lower calculated octanol–water partition coefficients (cLogP values, indicating higher hydrophilicity) and greater molecular rigidity compared with synthetic compound libraries1,6,7,8,9. These differences can be advantageous; for example, the higher rigidity of NPs can be valuable in drug discovery tackling protein–protein interactions10

NPs are structurally ‘optimized’ by evolution to serve particular biological functions1, including the regulation of endogenous defence mechanisms and the interaction (often competition) with other organisms, which explains their high relevance for infectious diseases and cancer. Furthermore, their use in traditional medicine may provide insights regarding efficacy and safety. Overall, the NP pool is enriched with ‘bioactive’ compounds covering a wider area of chemical space compared with typical synthetic small-molecule libraries13.

Despite these advantages and multiple successful drug discovery examples, several drawbacks of NPs have led pharmaceutical companies to reduce NP-based drug discovery programmes. NP screens typically involve a library of extracts from natural sources (Fig. 1), which may not be compatible with traditional target-based assays14. Identifying the bioactive compounds of interest can be challenging, and dereplication tools have to be applied to avoid rediscovery of known compounds. Accessing sufficient biological material to isolate and characterize a bioactive NP may also be challenging15. 

1. what is mode of action? 
    uses role type to determine the best drug pipeline to send this molecule in
2. once you know whether biological, chem, or medical application, which methods do you use to test for target compound?
    some methods are better for certain roles. more importantly, the role name can shed light on which specific tests to use. 
3. What parameters for these methodologies?
    use important features to better tune experiemts. what is the compounds complexity? c count? 

this is why my classification specifically helps
ONTOLOGY
IDENTIFIES MODE OF ACTION FOR COMPOUND 

ontology of applicatoin:

Any substance introduced into a living organism with therapeutic or diagnostic purpose.

ontology of chemical 

A role played by the molecular entity or part thereof within a chemical context.

ontology of biological

first preclinical step of drug discovery pipeline is identifying target. 
that is, this is where it all begins. 

Target Discovery
During the first phase, known as target discovery, in vitro research is performed to identify targets involved in specific diseases. A target is usually a molecule integral to gene regulation or intracellular signaling, such as a nucleic acid sequence or protein. 

by idendtifying whether a natural compound has a biological role, chemical role, or application, as well as the specific name of the role of that compound, I offer insight to pharmaceutical companies which are trying to speed up their pipeline. This will cut down on the time and resources needed to complete that very first step of drug discovery. 

Good target identification increases confidence in the relationship between target and disease and allows us to explore whether target modulation will lead to mechanism-based side effects

methodologies used for the identification of disease-relevant compounds

Affinity chromatography
Expression-cloning
Protein microarray
Reverse transfected cell microarray
Biochemical suppression
siRNA
DNA microarray
Systems biology
Study of existing drugs

Besides knowing the role type (biological, chemical, application), knowledge of the role name will allow scientists to more accurately pick the initial methodologies which they will use to identify the target. 

Not every method works for every compound, but rather some methods are better for certain ontologies. 

Some are better for chemical role types than they are for biological role types. To get even more granular, some methods work better for specific role names within a role type. 

for example, let's say my model classifies an unknown compound as a bacterial metabolite, which is a biological application. 

some of the most important features in predicting role type and role name are complexity, carbon count, hydrogen count, TPSA, and rotatable bond count.

Therefore scientists should pay special attention to these values when setting up parameters in their experiments for identifying target molecule in drug pipeline. 

based on the above properties of bacterial metabolites, scientists will know to pick affinity chromatography for identifying the target over a method like DNA microarrays.

affinity chromatography  separates a biomolecule from a mixture, based on a highly specific macromolecular binding interaction between the biomolecule and another substance. an example of this would be enzyme/inhibitor interactions. knowing the properties of a bacterial metabolite will make this process easier, as we know which enzymes and inhibitors to use. 

Scientists use DNA microarrays to measure the expression levels of large numbers of genes simultaneously. This is useless in the scope of bacterial metabolites. 


avoiding wasting time and money on long and costly testing methods that would not have yielded them good results in the first place. They can avoid unnecessary testing. 