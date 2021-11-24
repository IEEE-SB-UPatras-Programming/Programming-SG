#ifndef INDEX_BUFFER_HPP
#define INDEX_BUFFER_HPP

#include <GL/eglew.h>

class EBO
{
public:
    EBO(GLuint* indices, GLsizeiptr size);

    void Bind();
    void Unbind();
    void Delete();

    GLuint id;

};

#endif
