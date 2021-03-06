import numpy as np

label_cleaning = {
 'a supprimer': np.NaN,
 "abus de l'etat d'ignorance ou de faiblesse d'une personne elements constitutifs": "abus de l'etat d'ignorance ou de faiblesse d'une personne",
 'aide judiciaire': 'aide juridique',
 'alsace-lorraine': 'alsace',
 'alsace-moselle': 'alsace',
 'assurance (regles generales)': 'assurance',
 'assurance de personnes': 'assurance',
 'assurance dommages': 'assurance',
 'assurance en general': 'assurance',
 'assurance maritime': 'assurance',
 'assurance responsabilite': 'assurance',
 'assurances (regles generales)': 'assurance',
 'assurances de personnes': 'assurance',
 'atteinte a la vie privee elements constitutifs': 'atteinte a la vie privee',
 'bail (regles generales)': 'bail',
 'bail a loyer (loi du 1er septembre 1948)': 'bail',
 'bail a loyer (loi du 23 decembre 1986)': 'bail',
 'bail a loyer (loi du 6 juillet 1989)': 'bail',
 'bail commercial': 'bail',
 "bail d'habitation": 'bail',
 'bail emphyteotique': 'bail',
 'bail rural': 'bail',
 'bourse de valeurs': 'bourse',
 'concurrence deloyale ou illicite': 'concurrence',
 'conflit collectif du travail greve': 'conflit collectif du travail',
 'conflit de juridictions': 'conflit de juridiction',
 'contrats et obligations conventionnelles': 'contrats et obligations',
 'contrefaoeon': 'contrefacon',
 "controle d'identiteverification d'identite": "controle d'identite",
 'entreprise en difficulte (loi du 1er mars 1984)': 'entreprise en difficulte',
 'entreprise en difficulte (loi du 25 janvier 1985)': 'entreprise en difficulte',
 'entreprise en difficulte (loi du 26 juillet 2005)': 'entreprise en difficulte',
 'entreprise en difficulte (prevention et reglement amiable)': 'entreprise en difficulte',
 'expertise': 'expert judiciaire',
 'filiation adoptive': 'filiation',
 'indivision chose indivise': 'indivision',
 'jugements et arrets par defaut': 'jugements et arrets',
 'officiers publics ou ministeriels': 'officiers publics et ministeriels',
 'pouvoirs du premier president': 'pouvoirs des juges',
 'prescription acquisitive': 'prescription',
 'prescription civile': 'prescription',
 'preuve (regles generales)': 'preuve',
 'preuve litterale': 'preuve',
 'preuve testimoniale': 'preuve',
 "procedures civiles d'execution (loi du 9 juillet 1991)": "procedures civiles d'execution",
 'prostitution racolage': 'proxenetisme',
 'publicite commerciale': 'publicite',
 'referes': 'refere',
 'responsabilite civile': 'responsabilite delictuelle ou quasi delictuelle',
 'societe (regles generales)': 'societe',
 'societe a capital variable': 'societe',
 'societe a responsabilite limitee': 'societe',
 'societe anonyme': 'societe',
 'societe civile': 'societe',
 'societe civile immobiliere': 'societe',
 'societe commerciale (regles generales)': 'societe',
 'societe cooperative': 'societe',
 'societe creee de fait': 'societe',
 "societe d'amenagement foncier et d'etablissement rural": 'societe',
 'societe en nom collectif': 'societe',
 'societe par actions simplifiee': 'societe',
 'travail reglementation': 'travail'}
