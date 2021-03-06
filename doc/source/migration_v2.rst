=======================
Migration to v2 version
=======================

- ``Neuron`` object now extends ``morphio.Morphology``.
- NeuroM does not remove unifurcations on load. Unifurcation is a section with a single child. Such
  sections are possible in H5 and ASC formats. Now, in order to remove them on your morphology, you
  would need to call ``remove_unifurcations()`` right after the morphology is constructed.

  .. code-block:: python

      import neurom as nm
      nrn = nm.load_neuron('some/data/path/morph_file.asc')
      nrn.remove_unifurcations()

- Soma is not considered as a section anymore. Soma is skipped when iterating over neuron's
  sections. It means that section indexing offset needs to be adjusted by
  ``-(number of soma sections)`` which is usually ``-1``.
- drop ``benchmarks``
- drop ``neurom.check.structural_checks`` as MorphIO does not allow to load invalid morphologies,
  and it does not give access to raw data.
- drop ``Tree`` class. Use ``Section`` instead as it includes its functionality but if you need
  ``Tree`` separately then copy-paste ``Tree`` code from v1 version to your project.
- ``Section`` and ``Neurite`` class can't be copied anymore because their underlying MorphIO
  objects can't be copied (pickled). Only copying of ``Neuron`` is preserved.
- drop ``FstNeuron``. It functionality is included in ``Neuron`` class. Use ``Neuron`` instead of
  ``FstNeuron``.
- Validation of morphologies changed.
    The following is not an invalid morphology anymore:

    - 2 point soma
    - non-sequential ids
- script ``morph_check`` and ``morph_stats`` changed to ``neurom check`` and ``neurom stats``
    correspondingly.