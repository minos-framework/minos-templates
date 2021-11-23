__author__ = "{{ author }}"
__email__ = "{{ email }}"
__version__ = "{{ version }}"

from .aggregates import (
    {{ aggregate }},
)
from .cli import (
    main,
)
from .commands import (
    {{ aggregate }}CommandService,
)
from .queries import (
    {{ aggregate }}QueryService,
)
