
import unittest
from pynif.bean import NIFBean

class BeanTest(unittest.TestCase):
    
    def test_to_string_blank(self):
        b = NIFBean()
        self.assertEqual("<Bean (undefined)>", str(b))
        
    def test_to_string(self):
        b = NIFBean()
        b.beginIndex = 34
        b.endIndex = 44
        b.mention = "revolution"
        self.assertEqual("""<Bean 34-44: 'revolution'>""", str(b))
        
    def test_to_turtle(self):
        b = NIFBean()
        b.context = 'http://www.cse.iitb.ac.in/~soumen/doc/CSAW/doc/yn_08Oct08_file_0'
        b.referenceContext = 'http://www.cse.iitb.ac.in/~soumen/doc/CSAW/doc/yn_08Oct08_file_0/#offset_0_1413'
        b.mention = 'Afghanistan'
        b.beginIndex = 91
        b.endIndex = 102
        b.taClassRef = None
        b.score = 1
        b.taIdentRef = 'http://dbpedia.org/resource/Afghanistan'
        
        target_ttl = """<http://www.cse.iitb.ac.in/~soumen/doc/CSAW/doc/yn_08Oct08_file_0/#offset_91_102>
\ta                       nif:OffsetBasedString , nif:Phrase ;
\tnif:anchorOf            "Afghanistan" ;
\tnif:beginIndex          "91"^^xsd:nonNegativeInteger ;
\tnif:endIndex            "102"^^xsd:nonNegativeInteger ;
\tnif:referenceContext    <http://www.cse.iitb.ac.in/~soumen/doc/CSAW/doc/yn_08Oct08_file_0/#offset_0_1413> ;
\titsrdf:taClassRef        ;
\titsrdf:taConfidence     "1"^^xsd:double ;
\titsrdf:taIdentRef       <http://dbpedia.org/resource/Afghanistan> .
        """
        
        self.assertEqual(target_ttl.strip(), b.turtle.strip())
        