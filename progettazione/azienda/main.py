from beartype.claw import beartype_package      # <-- hype comes
from beartype import beartype
from azienda.test import test

beartype_package("azienda")                               # <-- hype goes

test(False)