Scripts for convert PO to INI.
How to use:
ConvertPOstoINI.py -> run this script when you need to join all po files converted to ini.
It will create myini.ini with all *.po & *.pot files converted.

ConvertPOtoINI.py -> run this script when you need to convert only one po file.
It will create <poname>.ini <- the conversion of the po.

ConvertPOTtoINI.py  -> run this script when you need to convert a pot file.
It will only use the msgid attrib, like:
[My activity]
Open=
Close=

