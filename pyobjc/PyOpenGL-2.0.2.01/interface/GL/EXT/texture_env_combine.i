/*
# AUTOGENERATED DO NOT EDIT

# If you edit this file, delete the AUTOGENERATED line to prevent re-generation
# BUILD api_versions [0x001]
*/

%module texture_env_combine

#define __version__ "$Revision: 1.1.2.1 $"
#define __date__ "$Date: 2004/11/15 07:38:07 $"
#define __api_version__ API_VERSION
#define __author__ "PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>"
#define __doc__ ""

%{
/**
 *
 * GL.EXT.texture_env_combine Module for PyOpenGL
 * 
 * Authors: PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>
 * 
***/
%}

%include util.inc
%include gl_exception_handler.inc

%{
#ifdef CGL_PLATFORM
# include <OpenGL/glext.h>
#else
# include <GL/glext.h>
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_EXT_texture_env_combine)

#endif
%}

/* FUNCTION DECLARATIONS */


/* CONSTANT DECLARATIONS */
#define                 GL_COMBINE_EXT 0x8570
#define             GL_COMBINE_RGB_EXT 0x8571
#define           GL_COMBINE_ALPHA_EXT 0x8572
#define               GL_RGB_SCALE_EXT 0x8573
#define              GL_ADD_SIGNED_EXT 0x8574
#define             GL_INTERPOLATE_EXT 0x8575
#define                GL_CONSTANT_EXT 0x8576
#define           GL_PRIMARY_COLOR_EXT 0x8577
#define                GL_PREVIOUS_EXT 0x8578
#define             GL_SOURCE0_RGB_EXT 0x8580
#define             GL_SOURCE1_RGB_EXT 0x8581
#define             GL_SOURCE2_RGB_EXT 0x8582
#define           GL_SOURCE0_ALPHA_EXT 0x8588
#define           GL_SOURCE1_ALPHA_EXT 0x8589
#define           GL_SOURCE2_ALPHA_EXT 0x858A
#define            GL_OPERAND0_RGB_EXT 0x8590
#define            GL_OPERAND1_RGB_EXT 0x8591
#define            GL_OPERAND2_RGB_EXT 0x8592
#define          GL_OPERAND0_ALPHA_EXT 0x8598
#define          GL_OPERAND1_ALPHA_EXT 0x8599
#define          GL_OPERAND2_ALPHA_EXT 0x859A


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_texture_env_combine)

#endif
	NULL
};

#define glInitTextureEnvCombineEXT() InitExtension("GL_EXT_texture_env_combine", proc_names)
%}

int glInitTextureEnvCombineEXT();
DOC(glInitTextureEnvCombineEXT, "glInitTextureEnvCombineEXT() -> bool")

%{
PyObject *__info()
{
	if (glInitTextureEnvCombineEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

