
import unittest
from pynif.context import NIFContext

class ContextTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.example_text = "    Primary Navigation Secondary Navigation Search: Nearly 60 militants killed in southern Afghanistan Tue Oct 7, 9:14 AM ET KABUL (Reuters) - U.S.-led coalition and Afghan security forces killed nearly 60 militants during separate clashes in southern Afghanistan, the U.S. military and a police official said Tuesday. Violence has surged in the war-torn country with some 3,800 people, a third of them civilians, killed as a result of the conflict by the end of July this year, according to the United Nations. U.S.-led coalition and Afghan security forces killed 43 militants during heavy fighting in Qalat district of southern Zabul province Sunday, the U.S. military said in a statement Tuesday. \"ANSF (Afghan National Security Forces ) and coalition forces on a patrol received heavy weapons, machine gun and sniper fire from militants in multiple locations,\" the U.S. military said in a statement. The combined forces responded with small arms fire , rocket propelled grenades and close air support , killing the militants, it said. No Afghan or U.S.-led troops were killed or wounded during incident, it said. In a separate incident, Afghan and international troops killed 16 Taliban insurgents and wounded six more during a gun battle in Nad Ali district of southern Helmand province on Monday, provincial police chief Asadullah Sherzad told Reuters. (Writing by Jonathon Burch; Editing by Bill Tarrant)"
    
    def test_to_string_undefined(self):
        c = NIFContext()
        self.assertEqual("<NIFContext (undefined)>", str(c))
        
    def test_to_string(self):
        c = NIFContext()
        c.baseURI = 'http://www.cse.iitb.ac.in/~soumen/doc/CSAW/doc/yn_08Oct08_file_0/'
        c.beginIndex = 0
        c.mention = "    Primary Navigation Secondary Navigation Search: Nearly 60 militants killed"
        c.endIndex = len(c.mention)
        self.assertEqual("<NIFContext 0-78: '    Primary Navigation Secondary Navigation Search...'>", str(c))
        
    def test_add_bean(self):
        c = NIFContext()
        c.baseURI = 'http://www.cse.iitb.ac.in/~soumen/doc/CSAW/doc/yn_08Oct08_file_0'
        c.beginIndex = 0
        c.endIndex = len(self.example_text)
        c.mention = self.example_text
        
        b = c.addBean(91, 102)
        self.assertEqual(91, b.beginIndex)
        self.assertEqual(102, b.endIndex)
        self.assertEqual("Afghanistan", b.mention)
        self.assertEqual("http://www.cse.iitb.ac.in/~soumen/doc/CSAW/doc/yn_08Oct08_file_0", b.context)
        
    def test_turtle(self):
        self.maxDiff = None
        turtle = """<http://www.cse.iitb.ac.in/~soumen/doc/CSAW/doc/yn_08Oct08_file_0/#offset_0_1411>
\ta                       nif:OffsetBasedString , nif:Context ;
\tnif:beginIndex  "0"^^xsd:nonNegativeInteger ;
\tnif:endIndex    "{}"^^xsd:nonNegativeInteger ;
\tnif:isString    "{}" .

<http://www.cse.iitb.ac.in/~soumen/doc/CSAW/doc/yn_08Oct08_file_0/#collection>
\ta               nif:ContextCollection ;
\tnif:hasContext\t<http://www.cse.iitb.ac.in/~soumen/doc/CSAW/doc/yn_08Oct08_file_0/#offset_0_1411>
\t<http://purl.org/dc/terms/conformsTo>
\t\t<http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core/2.1> .""".format(len(self.example_text), self.example_text.replace('"', '\\"'))

        c = NIFContext()
        c.baseURI = 'http://www.cse.iitb.ac.in/~soumen/doc/CSAW/doc/yn_08Oct08_file_0'
        c.beginIndex = 0
        c.endIndex = len(self.example_text)
        c.mention = self.example_text
        
        gen_turtle = c.turtle.strip()
        
        self.assertEqual(turtle.strip(), gen_turtle)
