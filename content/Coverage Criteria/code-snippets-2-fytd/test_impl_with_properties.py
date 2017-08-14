#py.test --cov-report=term --cov=. --cov-config=coverage.rc --cov-fail-under=100

from impl import PhysicalInfo
import pytest
import hypothesis.strategies as st
from hypothesis import given, assume

