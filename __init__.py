from element_tree import xml_compare_with_visitor, MyElementTree
from default_visitor import StdVisitor
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


if len(sys.argv) != 3:
	sys.stderr.write("Usage: python %s oldfile newfile" % sys.argv[0])

else:
	oldTree = MyElementTree(ET.parse(sys.argv[1]).getroot())
	newTree = MyElementTree(ET.parse(sys.argv[2]).getroot())
	visitor = StdVisitor()

	xml_compare_with_visitor(oldTree, newTree, visitor)