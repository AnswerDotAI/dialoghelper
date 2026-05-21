"""Web search and URL reading tools for models without native browser/search support.

This skill exposes the Solveit web-search helpers as plain text-returning tools.
"""

from dialoghelper.core import *
from ipykernel_helper import read_url
from pyskills.core import allow

__all__ = ['read_url', 'search', 'searches', 'web_answer']

allow(read_url, search, searches, web_answer)
