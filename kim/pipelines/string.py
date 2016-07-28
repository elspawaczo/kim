# kim/pipelines/string.py
# Copyright (C) 2014-2015 the Kim authors and contributors
# <see AUTHORS file>
#
# This module is part of Kim and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import six

from .base import pipe, is_valid_choice
from .marshaling import MarshalPipeline
from .serialization import SerializePipeline


@pipe()
def is_valid_string(session):
    """pipe used to determine if a value can be coerced to a string

    :param session: Kim pipeline session instance

    """

    try:
        return six.text_type(session.data)
    except ValueError:
        raise session.field.invalid(error_type='type_error')


class StringMarshalPipeline(MarshalPipeline):

    validation_pipes = \
        [is_valid_string, is_valid_choice] + MarshalPipeline.validation_pipes


class StringSerializePipeline(SerializePipeline):
    pass