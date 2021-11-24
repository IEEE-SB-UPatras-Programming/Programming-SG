#ifndef TEXTURE_CLASS_H
#define TEXTURE_CLASS_H

#include<GL/eglew.h>

#include"Helpers.hpp"
#include"Shader.hpp"

class Texture
{
public:
	GLuint id;
	GLenum type;
	Texture(const char* image, GLenum texType, GLenum slot, GLenum format, GLenum pixelType);

	// Assigns a texture unit to a texture
	void AssignUnit(Shader& shader, const char* uniform, GLuint unit);
	// Binds a texture
	void Bind();
	// Unbinds a texture
	void Unbind();
	// Deletes a texture
	void Delete();
};
#endif
