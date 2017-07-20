Random BioGears Patient Creation Tool
----------------------------------------

Dependencies
===============
-Python 3+ (tested, not sure about python 2.x)
-xml.etree.ElementTree (standard library)
-random (standard library)

Use
===========
Make sure python is installed on your system then simply clone, and type python RandPatientXML. It will then display a list of possible patient parameters that you'd like randomized (bounded by "healthy" patient values), type desired value and then hit enter and a file will be created titled "patient.xml"

BioGears Use
=================
To run this patient into any scenario in BioGears just replace the name of the patient file at the top of the scenario file you'd like to insert your new patient into.

For example in "BasicStandard.xml" on line 5 replace StandardMale.xml with patient.xml, and your new randomized patient will be inserted and run for that scenario's duration.

Future Additions
==================
Maybe, but feel free to use and edit as you see fit.