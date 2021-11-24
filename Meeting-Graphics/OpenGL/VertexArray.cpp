#include "VertexArray.hpp"

// Constructor that generates a VAO ID
VAO::VAO()
{
	glGenVertexArrays(1, &id);
}

// Links a VBO to the VAO using a certain layout
void VAO::LinkAttribute(VBO& VBO, GLuint layout, GLuint n_components, GLenum type, GLsizeiptr stride, void* offset)
{
	VBO.Bind();
	glVertexAttribPointer(layout, n_components, type, GL_FALSE, stride, offset);
	glEnableVertexAttribArray(layout);
	VBO.Unbind();
}

// Binds the VAO
void VAO::Bind()
{
	glBindVertexArray(id);
}

// Unbinds the VAO
void VAO::Unbind()
{
	glBindVertexArray(0);
}

// Deletes the VAO
void VAO::Delete()
{
	glDeleteVertexArrays(1, &id);
}
