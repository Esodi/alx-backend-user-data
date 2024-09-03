#!/usr/bin/env python3
""" The module containing auth class
"""


from flask import request
from typing import List, TypeVar


class Auth:
    ''' Class itself
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' authenticating method
        '''
        return False

    def authorization_header(self, request=None) -> str:
        ''' authenticating header
        '''
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        ''' current user
        '''
        return request
