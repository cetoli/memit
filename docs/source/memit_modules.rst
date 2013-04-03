.. _memit_module:

################
Memit - Core
################

.. seealso::

   Module :mod:`memit`

.. note::
   Aggregates factory, control and interface units in this single module

.. _dialog:

Dialog
====================

Modal support for inquiring screens.

.. seealso::

   Class :class:`memit.Dialog`

.. note::
   Interface Unit.

.. _gui:

GUI
====================

A factory class wrapping and hiding the detais of actual HTML and Scale Vector
Graphics resources required to draw on the top of browser canvas.

.. seealso::

   Class :class:`memit.GUI`

.. note::
   Factory Unit.

.. _marker:

Marker
====================

A projetion of the selected dropping spot on each of three dimensions ortogonal
planes. This projection helps to localize the selection placement by reducing the
dimensionality to a two dimensional surface.

.. seealso::

   Class :class:`memit.Marker`

.. note::
   Interface Unit.

.. _piece:

Piece
====================

Represents the badge to be placed inside the cube. In this cube, it associates
the idea accessed by the badge to a collecion of memetic predicates.

.. seealso::

   Class :class:`memit.Piece`

.. note::
   Interface Unit.

.. _house:

House
====================

A spatial cell representing a three dimentional coordinate system. The cell is
the target where a piece can be dropped. The house determines the final association
of an idea with the corresponding memetic predicates.

.. seealso::

   Class :class:`memit.House`

.. note::
   Interface Unit.

.. _cube:

Cube
====================

The memetic space. Each dimension or wall of the cube is a memetic dimension
divided int three levels of magnitude.

.. seealso::

   Class :class:`memit.Cube`

.. note::
   Interface Unit.

.. _form:

Form
====================

Input screen devised to collect demographic data.

.. seealso::

   Class :class:`memit.Form`

.. note::
   Interface Unit.

.. _phase:

Phase
====================

Fourth memetic dimention. Translate the cube to the next memetic space.

.. seealso::

   Class :class:`memit.Phase`

.. note::
   Control Unit.

.. _board:

Board
====================

Basic game support bindind all the features together.

.. seealso::

   Class :class:`memit.Board`

.. note::
   Interface Unit.



