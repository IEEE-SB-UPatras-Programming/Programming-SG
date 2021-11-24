#ifndef VERTEX_BUFFER_HPP
#define VERTEX_BUFFER_HPP

#include <GL/eglew.h>

class VBO 
{
public:
    VBO(GLfloat* vertices, GLsizeiptr size);

    void Bind();
    void Unbind();
    void Delete();

    GLuint id;
};



#endif//VERTEX_BUFFER_HPP
