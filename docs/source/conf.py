# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

import os
import sys
import time
import datetime
import importlib

import sphinx_rtd_theme


sys.path.insert(0, os.path.abspath('../../'))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo', 'sphinx.ext.inheritance_diagram',
              'sphinx.ext.coverage', 'sphinx.ext.ifconfig', 'sphinx.ext.graphviz', 'sphinx.ext.intersphinx',
              'sphinx.ext.viewcode', 'sphinxcontrib.napoleon', 'autoapi.sphinx']

# Autodoc settings
# This value contains a list of modules to be mocked up.
# This is useful when some external dependencies are not met at build time and break the building process.
autodoc_mock_imports = []

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['ntemplates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'taf'
author = 'Intel Corporation'
current_year = datetime.datetime.now().year
copyright = '2011-{0}, {1}'.format(current_year, author)  # pylint: disable=redefined-builtin

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
# TODO: How will we define version and release
# The short X.Y version.
version = '0.0.1'
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = '.rst'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#
today = time.strftime('%B %d, %Y')
#
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path

# exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# A dictionary of values to pass into the template engine`s context for all pages.
html_context = {
    "last_updated": today,
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
# htmlhelp_basename = 'tafdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    'papersize': '',
    'fontpkg': '',
    'fncychap': '',
    'maketitle': '\\cover',
    'pointsize': '',
    'preamble': '',
    'releasename': "",
    'babel': '',
    'printindex': '',
    'fontenc': '',
    'inputenc': '',
    'classoptions': '',
    'utf8extra': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'taf.tex', 'TAF Documentation',
     'Intel Corporation', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'taf', 'TAF Documentation',
     [author], 1),
]

# -- Options for AutoApi -------------------------------------------------

# autoapi configuration
autoapi_modules = {
    'taf': {
        'override': False,
        'output': 'auto',
    },
    'utils': {
        'override': False,
        'output': 'auto',
    },
    'tests': {
        'override': False,
        'output': 'auto',
    },
    'unittests': {
        'override': False,
        'output': 'auto',
    },
    'reporting': {
        'override': False,
        'output': 'auto',
    },
}

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/3.4': None}


# No need to install 3rd party packages to generate the docs
class Mock(object):

    __all__ = []

    assign = None
    apply = None
    vector = None
    split = None
    interpolate = None
    copy = None
    __add__ = None
    __mul__ = None
    __neg__ = None
    get_gst = None
    SolverType_LU = None

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return Mock()

    @classmethod
    def __getattr__(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        elif name[0] == name[0].upper():
            mockType = type(name, (Mock, ), {})
            mockType.__module__ = __name__
            return mockType
        else:
            return Mock()


MOCK_MODULES = ['taf.testlib.TRex.TRex', 'taf.testlib.TRex.TRexHTL', 'taf.testlib.tempest_clients.magnum.sfc_client',
                'taf.testlib.tempest_clients.magnum.models.clusterpatch_mode', 'oslo_log', 'linux.lldp', 'pcapy',
                'tempest', 'tempest.lib', 'tempest.lib.exceptions', 'tempest.lib.common',
                'trex_stl_lib', 'trex_stl_lib.api', 'trex_stl_lib.trex_stl_hltapi',
                ]

for mod_name in MOCK_MODULES:
    try:
        importlib.import_module(mod_name)
    except ImportError:
        print("Generating mock module %s" % mod_name)
        sys.modules[mod_name] = Mock()
