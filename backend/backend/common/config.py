# coding: utf-8

from enum import Enum


class ErrorCode(Enum):
    success = 0
    not_found = 1
    unauthorized = 2
    bad_request = 3


class ErrorMsg(Enum):
    success = 'success'
    not_found = 'resource not found'
    unauthorized = 'unauthorized access'
    bad_request = 'bad request'
