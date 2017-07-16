# fop-service
rest-wrapper for Apache FOP (https://xmlgraphics.apache.org/fop/)

# Example
1) Generate pdf

```python
import requests
     
data = {
    'filename': 'test.xml',
    'fo_data': '''
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
  <fo:layout-master-set>
    <fo:simple-page-master master-name="simpleA4" page-height="29.7cm" page-width="21cm" margin-top="2cm" margin-bottom="2cm" margin-left="2cm" margin-right="2cm">
      <fo:region-body/>
    </fo:simple-page-master>
  </fo:layout-master-set>
  <fo:page-sequence master-reference="simpleA4">
    <fo:flow flow-name="xsl-region-body">
      <fo:block>Hello World!</fo:block>
    </fo:flow>
  </fo:page-sequence>
</fo:root>
''',
}
  
requests.post(YOU URL, data=data)
```

2) Generate pdf with image

```python
import requests
  
data = {
    'filename': 'test.xml',
    'fo_data': '''
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
  <fo:layout-master-set>
    <fo:simple-page-master master-name="simpleA4" page-height="40.7cm" page-width="29.7cm" margin-top="2cm" margin-bottom="2cm" margin-left="2cm" margin-right="2cm">
      <fo:region-body/>
    </fo:simple-page-master>
  </fo:layout-master-set>
  <fo:page-sequence master-reference="simpleA4">
    <fo:flow flow-name="xsl-region-body">
      <fo:block>Hello World!</fo:block>
      <fo:block><fo:external-graphic src="1.jpg"/></fo:block>
      <fo:block><fo:external-graphic src="2.jpg"/></fo:block>
    </fo:flow>
  </fo:page-sequence>
</fo:root>
''',
}
  
files = [
    ('images', ('1.jpg', open('1.jpg', 'rb'), 'image/jpg')),
    ('images', ('2.jpg', open('2.jpg', 'rb'), 'image/jpg'))
]
  
requests.post(YOU URL, data=data, files=files)
```
