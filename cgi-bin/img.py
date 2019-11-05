#!/usr/bin/env python3
# -*- coding: utf-8


import base64
import qrcode

from _sell import *

img = qrcode.make('Some data here')

decoded_data = base64.b64encode(img.load())

Html.head_html()
#print(decoded_data)
print('<img src="data:image/png;base64,{}">'.format(decoded_data))
#print('<img src="{}"'.format(decoded_data))

Html.footer_html


