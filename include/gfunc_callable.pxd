#
# Copyright (C) 2011-14 Mark Wiebe, DyND Developers
# BSD 2-Clause License, see LICENSE.txt
#

cdef extern from "gfunc_callable_functions.hpp" namespace "pydynd":
    void add_ndt_type_names_to_dir_dict(ndt_type&, object) except +translate_exception
    object get_ndt_type_dynamic_property(ndt_type&, object) except +translate_exception

    void add_array_names_to_dir_dict(ndarray&, object) except +translate_exception
    object get_array_dynamic_property(ndarray&, object) except +translate_exception
    void set_array_dynamic_property(ndarray&, object, object) except +translate_exception

    # Function properties
    cdef cppclass ndt_type_callable_wrapper:
        pass
    object ndt_type_callable_call(ndt_type_callable_wrapper&, object, object) except +translate_exception
    object call_ndt_type_constructor_function(ndt_type&, object, object) except +translate_exception

    void init_w_ndt_type_callable_typeobject(object)
    cdef struct ndt_type_callable_placement_wrapper:
        pass
    void placement_new(ndt_type_callable_placement_wrapper&)
    void placement_delete(ndt_type_callable_placement_wrapper&)
    # ndarray placement cast
    ndt_type_callable_wrapper& GET(ndt_type_callable_placement_wrapper&)

    # Function property of nd::array
    cdef cppclass array_callable_wrapper:
        pass
    object array_callable_call(array_callable_wrapper&, object, object) except +translate_exception

    void init_w_array_callable_typeobject(object)
    cdef struct array_callable_placement_wrapper:
        pass
    void placement_new(array_callable_placement_wrapper&)
    void placement_delete(array_callable_placement_wrapper&)
    # ndarray placement cast
    array_callable_wrapper& GET(array_callable_placement_wrapper&)

cdef extern from "dynd/func/arrfunc.hpp" namespace "dynd":
    cdef cppclass ndarrfunc "dynd::nd::arrfunc":
        ndarrfunc() except +translate_exception

cdef extern from "arrfunc_from_pyfunc.hpp" namespace "pydynd":
    ndarrfunc arrfunc_from_pyfunc(object, object) except +translate_exception

cdef extern from "arrfunc_functions.hpp" namespace "pydynd":
    void init_w_arrfunc_typeobject(object)
    object arrfunc_call(object, object, object) except +translate_exception
    object arrfunc_rolling_apply(object, object, object, object) except +translate_exception
    object dynd_get_published_arrfuncs "pydynd::get_published_arrfuncs" () except +translate_exception
