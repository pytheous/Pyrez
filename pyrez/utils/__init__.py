
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

def fix_param(param, *, _join=None):
  #if isinstance(params, (list, tuple)):
    #  from datetime import datetime
    #  from enum import Enum
    #  url += f"/{'/'.join(p.strftime('yyyyMMdd') if isinstance(p, datetime) else str(p.value) if isinstance(p, Enum) or hasattr(p, 'value') else str(p) for p in params if p)}"
  #else:
    #  url += f'/{params}'
  if isinstance(param, (list, tuple)):
    #if _join: return f'{_join}'.join([fix_param(p) for p in param if p])
    return [fix_param(p) for p in param if p]
  from datetime import datetime
  from enum import Enum
  if isinstance(param, datetime):
    return param.strftime('yyyyMMdd')
  if hasattr(param, 'value') or isinstance(param, Enum):
    return str(param.value)
  return str(param)

def ___(_, __, _____=None, *, api=None, **kw):
  if is_instance_or_subclass(_, str) or is_instance_or_subclass(_, dict):
    try:
      if is_instance_or_subclass(_, dict):
        return __(**_, api=api) if api else __(**_)
        #'NoneType' object is not callable
      return __(_, api=api) if api else __(_)
    except (TypeError, ValueError) as exc:
      print(exc, _)
  if is_instance_or_subclass(_, list):# or is_instance_or_subclass(_, tuple):
    if __:
      if api:
        __r__ = [__(api=api, **____) for ____ in (_ or []) if ____]
      else:
        __r__ = [__(**____) for ____ in (_ or []) if ____]
    else:
      __r__ = _
    if __r__ and len(__r__) < 2:
      return __r__[0]
    if kw.get('filter_by'):
      from .num import num_or_string
      try:
        if kw.get('accepted_values'):
          __r__ = [_ for _ in __r__ if num_or_string(_[kw.get('filter_by')]) in kw.get('accepted_values', [])]# or num_or_string(_[kw.get('filter_by')]) not in kw.get('ignored_values', [])
        else:
          __r__ = [_ for _ in __r__ if num_or_string(_[kw.get('filter_by')])]
      except (KeyError, TypeError):
        pass
    if kw.get('sorted_by') or kw.get('filter_by'):
      try:
        __r__ = sorted(__r__, key=lambda x: x.get(kw.get('sorted_by')) or x.get(kw.get('filter_by')), reverse=kw.get('reverse') or False)
      except (KeyError, TypeError):
        pass
    return __r__
  '''
  try:
    return __(**_[0])
  except (IndexError, KeyError):
    return __(**_)
  except TypeError:
    pass
  '''
  if _____:
    raise _____
  return _ or None

def is_instance_or_subclass(x, cls):
  """Return True if ``x`` is either a subclass or instance of ``cls``."""
  try:
    return issubclass(x, cls)
  except TypeError:
    return isinstance(x, cls)

def slugify(value):
  """Normalizes string, converts to lowercase, removes non-alpha characters, and converts spaces to hyphens.
  From: http://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename-in-python"""
  import re
  import unicodedata
  return (re.sub(r'[-\s]+', '-', re.sub(r'[^\w\s-]', '', unicodedata.normalize('NFKD', str(value)).encode('ascii', 'ignore').decode('utf-8', 'ignore'))) or value).strip().replace(' ', '-').replace("'", '').lower()

class Info:
  @property
  def aiohttp(self):
    try:
      import aiohttp
    except ImportError:
      return
    else:
      return aiohttp.__version__
  @property
  def os(self):
    import platform
    #return '{platform.system} {platform.release} {platform.version}'.format(platform=platform.uname())
    return platform.platform()
  @property
  def pyrez(self):
    from ..__version__ import version_info
    #return '{ver.major}.{ver.minor}.{ver.micro}-{ver.releaselevel}'.format(ver=version_info)
    return version_info
  @property
  def python(self):
    import sys
    #return '{py.major}.{py.minor}.{py.micro}-{py.releaselevel}'.format(py=sys.version_info)
    return sys.version.replace('\n', '')
  @property
  def python_implementation(self):
    import platform
    return platform.python_implementation()
  @property
  def rapidjson(self):
    try:
      import rapidjson
    except ImportError:
      return
    else:
      return rapidjson.__version__
  @property
  def requests(self):
    try:
      import requests
    except ImportError:
      return
    else:
      return requests.__version__
  @property
  def uvloop(self):
    try:
      import uvloop
    except ImportError:
      return
    else:
      return uvloop.__version__
  @property
  def ujson(self):
    try:
      import ujson
    except ImportError:
      return
    else:
      return ujson.__version__
  def collect(self):
    __packages__ = []

    __packages__.append(f'{self.python_implementation}: {self.python}')
    __packages__.append(f'OS: {self.os}')
    __packages__.append(f'requests: {self.requests}')
    __packages__.append(f'aiohttp: {self.aiohttp}')

    uvloop = self.uvloop
    if uvloop:
      __packages__.append(f'uvloop: {uvloop}')
    rapidjson = self.rapidjson
    if rapidjson:
      __packages__.append(f'rapidjson: {rapidjson}')
    ujson = self.ujson
    if ujson:
      __packages__.append(f'ujson: {ujson}')
    return __packages__
  def __str__(self):
    return '\n'.join(self.collect())

if __name__ == '__main__':
  print(Info())

#from .decorators import *
from .http import *
from .loop import *

__all__ = (
  'auth',
  'decorators',
  'http',
  'loop',
  'num',
  'sys',
  'time',
)
