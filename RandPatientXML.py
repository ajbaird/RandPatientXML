'''
random generation of a bioGears patient file xml 

@author abaird

'''
import xml.etree.ElementTree as ET
from random import randint, random, uniform

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

if __name__ == '__main__':

	#querry what random attribute you want
	response = input('enter random attribute (possibilities: Weight, Height, BodyFatFraction, DiastolicPressure, HeartRate, RespirationRate, SystolicPressure): ')
	print('Randomizing the following patient parameter: ' + response)
	#create patient root
	root = ET.Element('Patient')
	root.set('xmlns', 'uri:/mil/tatrc/physiology/datamodel')
	root.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
	root.set('contentVersion', 'BioGears_6.1.1-beta')
	root.set('xsi:schemaLocation', '')

	#create elements
	Name = ET.SubElement(root, 'Name')
	Sex = ET.SubElement(root, 'Sex')
	Age = ET.SubElement(root, 'Age')
	Weight = ET.SubElement(root, 'Weight')
	Height = ET.SubElement(root, 'Height')
	BodyFatFraction = ET.SubElement(root, 'BodyFatFraction')
	DiastolicArterialPressureBaseline = ET.SubElement(root, 'DiastolicArterialPressureBaseline')
	HeartRateBaseline = ET.SubElement(root, 'HeartRateBaseline')
	RespirationRateBaseline = ET.SubElement(root, 'RespirationRateBaseline')
	SystolicArterialPressureBaseline = ET.SubElement(root, 'SystolicArterialPressureBaseline')

	#set to standard male
	Name.text = 'Patient'
	Sex.text = 'Male'
	Age.set('unit', 'yr')
	Age.set('value', '44')
	Weight.set('unit', 'lb')
	Weight.set('value', '170')
	Height.set('unit', 'in')
	Height.set('value', '71.0')
	BodyFatFraction.set('value', '0.21')
	DiastolicArterialPressureBaseline.set('unit', 'mmHg')
	DiastolicArterialPressureBaseline.set('value', '73.5')
	HeartRateBaseline.set('unit', '1/min')
	HeartRateBaseline.set('value', '72.0')
	RespirationRateBaseline.set('unit', '1/min')
	RespirationRateBaseline.set('value', '16.0')
	SystolicArterialPressureBaseline.set('unit', 'mmHg')
	SystolicArterialPressureBaseline.set('value', '114.0')

	if(response == 'Weight'):
		randWeight = uniform(110, 180)   #This should change based on male/female and height but this is just a quick demo
		Weight.set('value', str(randWeight))
	elif(response == 'Height'):
		randHeight = uniform(60, 76)
		Height.set('value', str(randHeight))
	elif(response == 'BodyFatFraction'):
		randFat = random()
		BodyFatFraction.set(str(randFat))
	elif(response == 'DiastolicPressure'):
		randDiastolic = uniform(60,80)
		DiastolicArterialPressureBaseline.set('value', str(randDiastolic))
	elif(response == 'HeartRate'):
		randHeart = uniform(60,100)
		HeartRateBaseline('value', str(randHeart))
	elif(response == 'RespirationRate'):
		randRespiration = uniform(12, 20)
		RespirationRateBaseline.set('value', str(randRespiration))
	elif(response == 'SystolicPressure'):
		randSystolic = uniform(80,120)
		SystolicArterialPressureBaseline.set('value', str(randSystolic))

	tree = ET.ElementTree(root)
	indent(root)
	tree.write('Patient.xml', encoding="UTF-8", xml_declaration=True)