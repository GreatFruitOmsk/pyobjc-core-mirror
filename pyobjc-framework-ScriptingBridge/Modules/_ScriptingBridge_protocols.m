/*
 * This file is generated by objective.metadata
 *
 * Last update: Wed Jan 16 13:11:47 2013
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1006
    p = PyObjC_IdToPython(@protocol(SBApplicationDelegate)); Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1006 */
}
