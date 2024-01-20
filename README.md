# Psychemwiki
A wikilike description of various psychoactive molecules with texts, 3d and 2d views.
Uses Django as a framework.


Uses custom manage.py commands to handle 
various scripts to upload .mol and .sketch files (get_mol your/directory/here || get_sketch your/directory/here)
, clean the db from duplicates and merge them if necessary (clean_db),
clean the upload directories (clean_uploads),
etc.

