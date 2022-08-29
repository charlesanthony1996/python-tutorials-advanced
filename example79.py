from __future__ import annotations

import json
import textwrap
import typing
from timeit import timeit
import attr
import sys


class Code(typing.Protocol):
    name : str
    define : str
    create : str
    getattr : str | None
    setattr : str | None

    supports_mutable: bool | str
    supports_immutable: bool | str
    supports_slots: bool | str
    supports_kw_getset: bool | str
    supports_converters: bool | str
    supports_validators: bool | str
    typesafe: bool | str
    stdlib: bool | str


support_keys = [
    'supports_mutable',
    'supports_immutable',
    'supports_slots',
    'supports_defaults',
    'supports_default_history',
    'supports_kw_getset',
    'supports_converters',
    'supports_validators',
    'typesafe',
    'stdlib',
]

class TupleCode:
    name = 'tuple'
    define = "n, f, s = 42 , 4.5,  'hello'"
    create = "x = n, f ,s"
    getattr = "y = x[0]"
    setattr = None

    supports_mutable = False
    supports_immutable = True
    supports_slots = True
    supports_defaults = False
    supports_default_factory = False
    supports_kw_getset = False
    supports_converters = False
    supports_validators = False
    typesafe = False
    stdlib = False

class CollectionsNamedTupleCode:
    name = 'namedtuple'
    define = textwrap.dedent("""
    from collections import namedtuple
    T = namedtuple('T', ['n', 'f', 's'])
    """)
    create = "x = T(42 , 4.5, 'hello')"
    getattr = 'y = x[0]'
    setattr = None

    supports_mutable = False
    supports_immutable = True
    supports_slots = True
    supports_default_factory = True
    supports_kw_getset = False
    supports_converters = False
    supports_validators = False
    typesafe = False
    stdlib = True


class DataClassCode:
    name = 'dataclass'
    define = textwrap.dedent("""
        from dataclass import dataclass
        @dataclass
        class T:
            n: int
            f: float
            s: str
    """)
    create = "x = T(42, 4.5, 'False')"
    getattr = "y = x.n"
    setattr = "x.n = 0"

    supports_mutable = True
    supports_immutable = True
    supports_defaults = True
    supports_slots = True
    supports_default_factory = True
    supports_kw_getset = False
    supports_converters = False
    supports_validators = False
    typesafe = True
    stdlib = True


class DictCode:
    name = 'dict'
    define = ""
    create = "x = {'n': 42, 'f': 4.5, 's': hello}"
    getattr = "y = x[n]"
    setattr = "x['n'] = 0"

    supports_mutable = False
    supports_immutable = True
    