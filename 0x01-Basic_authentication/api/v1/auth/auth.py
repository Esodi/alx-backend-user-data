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
        if path is None or excluded_paths is None:
            return True
        if path and excluded_paths:
            if path in excluded_paths or path + '/' in excluded_paths:
                return False
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        ''' authenticating header
        '''
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        ''' current user
        '''
        return request
