from setuptools import setup, find_packages
import os.path

version = '4.0.4'

setup(name='Products.LinguaPlone',
      version=version,
      description="Manage and maintain multilingual content that integrates seamlessly with Plone.",
      long_description=".. contents::\n\n" +
                        open("README.txt").read() + "\n" +
                        open(os.path.join("docs", "FAQ.txt")).read() + "\n" +
                        open("CHANGES.txt").read(),
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
        ],
      keywords='Zope Plone multilingual translation',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/Products.LinguaPlone',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        # 'AccessControl', only in Zope 2.13
        'Acquisition',
        'DateTime',
        'Missing',
        'Products.Archetypes',
        'Products.ATContentTypes >= 2.0.2',
        'Products.CMFCore',
        'Products.CMFDynamicViewFTI',
        # 'Products.CMFPlone', only in Plone 4.1, Plone in 4.0
        'Products.GenericSetup',
        'Products.PloneLanguageTool',
        'Products.PloneTestCase',
        'Products.statusmessages',
        # 'Products.ZCTextIndex', only in Zope 2.13
        'ZODB3',
        'Zope2 >= 2.12.5',
        'plone.browserlayer',
        'plone.i18n',
        'plone.indexer',
        'plone.locking',
        'plone.memoize',
        'plone.theme',
        'plone.app.controlpanel',
        'plone.app.i18n >= 2.0.1',
        'plone.app.iterate',
        'plone.app.layout',
        'plone.app.portlets',
        'zope.component',
        'zope.formlib',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',
        'zope.site',
      ],
)
