"""CadQuery - A parametric 3D CAD scripting framework built on top of OCCT.

CadQuery is an intuitive, easy-to-use Python module for building parametric
3D CAD models. It is inspired by OpenSCAD but uses Python instead of a custom
language, and is built on top of the Open CASCADE Technology (OCCT) kernel.

Example usage::

    import cadquery as cq

    result = cq.Workplane("XY").box(10, 10, 10).fillet(1)
    cq.exporters.export(result, "box.step")
"""

from .cq import (
    CQContext,
    CQObject,
    Workplane,
)
from .occ_impl.geom import Vector, Matrix, Plane, BoundBox
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
)
from .occ_impl.assembly import Assembly, ConstraintKind
from .selectors import (
    Selector,
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    DirectionMinMaxSelector,
    RadiusNthSelector,
    CenterNthSelector,
    LengthNthSelector,
    SumSelector,
    SubtractSelector,
    AndSelector,
    InverseSelector,
    StringSyntaxSelector,
)
from . import exporters
from . import importers

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

__all__ = [
    "Assembly",
    "BoundBox",
    "Compound",
    "ConstraintKind",
    "CQContext",
    "CQObject",
    "Edge",
    "Face",
    "Matrix",
    "Plane",
    "Shape",
    "Shell",
    "Solid",
    "Vector",
    "Vertex",
    "Wire",
    "Workplane",
    # Selectors
    "AndSelector",
    "CenterNthSelector",
    "DirectionMinMaxSelector",
    "DirectionSelector",
    "InverseSelector",
    "LengthNthSelector",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "PerpendicularDirSelector",
    "RadiusNthSelector",
    "Selector",
    "StringSyntaxSelector",
    "SubtractSelector",
    "SumSelector",
    "TypeSelector",
    # Modules
    "exporters",
    "importers",
]
