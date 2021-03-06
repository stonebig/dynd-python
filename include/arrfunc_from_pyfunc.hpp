//
// Copyright (C) 2011-14 Mark Wiebe, DyND Developers
// BSD 2-Clause License, see LICENSE.txt
//

#ifndef _DYND__ARRFUNC_FROM_PYFUNC_HPP_
#define _DYND__ARRFUNC_FROM_PYFUNC_HPP_

#include "type_functions.hpp"

#include <dynd/func/arrfunc.hpp>
#include <dynd/types/arrfunc_type.hpp>

namespace pydynd {

void arrfunc_from_pyfunc(dynd::arrfunc_type_data *out_af, PyObject *pyfunc,
                         const dynd::ndt::type &proto);

inline dynd::nd::arrfunc arrfunc_from_pyfunc(PyObject *pyfunc, const dynd::ndt::type &proto)
{
    dynd::nd::array out_af = dynd::nd::empty(dynd::ndt::make_arrfunc());
    arrfunc_from_pyfunc(reinterpret_cast<dynd::arrfunc_type_data *>(
                            out_af.get_readwrite_originptr()),
                        pyfunc, proto);
    out_af.flag_as_immutable();
    return out_af;
}

inline dynd::nd::arrfunc arrfunc_from_pyfunc(PyObject *pyfunc, PyObject *proto)
{
    return arrfunc_from_pyfunc(pyfunc, make_ndt_type_from_pyobject(proto));
}

} // namespace pydynd

#endif // _DYND__ARRFUNC_FROM_PYFUNC_HPP_
