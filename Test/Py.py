import xml.etree.ElementTree as ET

e = ET.parse('C:\\Users\Casper\Documents\PythonProjects\Test\DataExport_ActivityTypes.dtsx').getroot()
ns = {'DTS': 'www.microsoft.com/SqlServer/Dts'}

for c in e:
    for i in c:
        ObjectName = i.get('{www.microsoft.com/SqlServer/Dts}ObjectName')

        if i.tag == "{www.microsoft.com/SqlServer/Dts}Variable":
            ObjectType = "Variable"
        elif i.tag == "{www.microsoft.com/SqlServer/Dts}ConnectionManager":
            ObjectType = "ConnectionManager"
        elif i.tag == "{www.microsoft.com/SqlServer/Dts}Executable":
            ObjectType = "Executable"
        elif i.tag == "{www.microsoft.com/SqlServer/Dts}PrecedenceConstraint":
            ObjectType = "PrecedenceConstraint"
        print(c, ObjectType, ObjectName)
