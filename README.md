New version with PyPi package available: https://github.com/bex-d/pointwisepy

# pwpy
Python library for the Pointwise Glyph API. Not fully tested or documented yet.

To run the Pointwise Glyph API:

1. install pointwise-glyph-client
   
	python -m pip install --user --upgrade pointwise-glyph-client

	or
	
 	https://pypi.org/project/pointwise-glyph-client/#files
	
2. to run in batch mode (port 0)
	
 	add following path to environment variables (System Properties > Advanced > Environment Variables > User Variables > Path > Edit > New)
	
 	"C:\Program Files\Cadence\PointwiseV18.6R3\win64\bin" (check correct location/version)
	
3. batch mode test 

in command line/powershell: 
	
	python
	
 	from pointwise import GlyphClient
	
 	from pointwise.glyphapi import *
	
 	glf = GlyphClient(port=0) 

	pw = glf.get_glyphapi()

4. connect to open GUI instance via command line/powershell: 

	in PW: 
	
 	Script > Glyph Server > Active & port=2807
	
 	end journalling

 	close any open function panels

in cmd line/.py file:

	python
	
 	from pointwise import GlyphClient
	
 	from pointwise.glyphapi import *
	
	glf = GlyphClient(port=2807) 

 	pw = glf.get_glyphapi()
	

http://www.pointwise.com/glyph2/ - Glyph documentation, lists all functions and options

https://github.com/pointwise/GlyphClientPython - source code
