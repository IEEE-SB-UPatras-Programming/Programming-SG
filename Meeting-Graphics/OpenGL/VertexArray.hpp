#ifndef VERTEX_ARRAY_HPP
#define VERTEX_ARRAY_HPP

#include<GL/eglew.h>
#include "VertexBuffer.hpp"

class VAO
{
public:
	// ID reference for the Vertex Array Object
	// Constructor that generates a VAO ID
	VAO();

	GLuint id;
	// Links a VBO to the VAO using a certain layout
	void LinkAttribute(VBO& VBO, GLuint layout, GLuint n_components, GLenum type, GLsizeiptr stride, void* offset);
	// Binds the VAO
	void Bind();
	// Unbinds the VAO
	void Unbind();
	// Deletes the VAO
	void Delete();
};

#endif
