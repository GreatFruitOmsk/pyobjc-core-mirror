/*
 * This file defines the glue code that is needed to access the objc module
 * from other modules.
 *
 * Why would you want to do that?
 * - To wrap native functions that use Objective-C objects as arguments or
 *   return values
 * - To add custom wrappers for troublesome methods in specific classes
 * - To generic support for additional method signatures
 */
#include "pyobjc.h"
#include "py2.2bool.h"
#include "objc_support.h"

#define PYOBJC_BUILD
#include "pyobjc-api.h"

#ifdef PyObjCObject_GetObject
#undef PyObjCObject_GetObject
#endif

static int bool_check(PyObject* obj)
{
	return PyObjCBool_Check(obj);
}

static PyObject* bool_init(long l)
{
	return PyObjCBool_FromLong(l);
}


static id python_to_id(PyObject* object)
{
	id result;
	int err;

	err = depythonify_c_value("@", object, &result);
	if (err == -1) {
		return nil;
	}

	return result;
}

static PyObject* id_to_python(id object)
{
	PyObject* result;

	result = pythonify_c_value("@", &object);
	return result;
}

static Class      sel_get_class(PyObject* sel)
{
	if (!ObjCNativeSelector_Check(sel)) {
		PyErr_SetString(PyExc_TypeError, "Expecting PyObjCSelector");
	}
	return ((ObjCNativeSelector*)sel)->sel_class;
}

static SEL      sel_get_sel(PyObject* sel)
{
	if (!PyObjCSelector_Check(sel)) {
		PyErr_SetString(PyExc_TypeError, "Expecting PyObjCSelector");
	}
	return ((PyObjCSelector*)sel)->sel_selector;
}

static void 	fill_super(struct objc_super* super, Class cls, id receiver)
{
	RECEIVER(*super) = receiver;
	super->class = cls;
}

static void 	fill_super_cls(struct objc_super* super, Class cls, Class self)
{
	RECEIVER(*super) = self;
	super->class = GETISA(cls);
}



struct pyobjc_api objc_api = {
	PYOBJC_API_VERSION,		/* api_version */
	sizeof(struct pyobjc_api),	/* struct_size */
	&PyObjCClass_Type,		/* class_type */
	(PyTypeObject*)&PyObjCObject_Type, /* object_type */
	&PyObjCSelector_Type,		/* select_type */
	PyObjC_RegisterMethodMapping,	/* register_method_mapping */
	PyObjC_RegisterSignatureMapping,	/* register_signature_mapping */
	PyObjCObject_GetObject,		/* obj_get_object */
	PyObjCObject_ClearObject,		/* obj_clear_object */
	PyObjCClass_GetClass,		/* cls_get_class */
	PyObjCClass_New,			/* cls_to_python */
	python_to_id,			/* python_to_id */
	id_to_python,			/* id_to_python */
	PyObjCErr_FromObjC,		/* err_objc_to_python */
	PyObjCErr_ToObjC,			/* err_python_to_objc */
	depythonify_c_value,		/* py_to_objc */
	pythonify_c_value,		/* objc_to_python */
	PyObjC_CallPython,		/* call_to_python */
	objc_sizeof_type,		/* sizeof_type */
	sel_get_class,			/* sel_get_class */
	sel_get_sel,			/* sel_get_sel */
	bool_check,			/* bool_check */
	bool_init,			/* bool_init */
	fill_super,			/* fill_super */
	fill_super_cls,			/* fill_super_cls*/
	PyObjCPointerWrapper_Register	/* register_pointer_wrapper */
};

int ObjCAPI_Register(PyObject* module_dict)
{
	PyObject* API = PyCObject_FromVoidPtr(&objc_api, NULL);

	if (API == NULL) return -1;

	if (PyDict_SetItemString(module_dict, PYOBJC_API_NAME, API) < 0) {
		Py_DECREF(API);
		return -1;
	}
	Py_DECREF(API); 
	return 0;
}
