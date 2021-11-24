#include "Texture.hpp"

#include <cassert>

Texture::Texture(const char* image, GLenum texture_type, GLenum slot, GLenum format, GLenum pixel_type): type(texture_type)
{
    int img_width, img_height, num_col_ch;

    stbi_set_flip_vertically_on_load(true);

    unsigned char * bytes = stbi_load(image, &img_width, &img_height, &num_col_ch, 0);

    glGenTextures(1, &id);
    glActiveTexture(slot);
    glBindTexture(type, id);

    glTexParameteri(type, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
	glTexParameteri(type, GL_TEXTURE_MAG_FILTER, GL_NEAREST);

	// Configures the way the texture repeats (if it does at all)
	glTexParameteri(type, GL_TEXTURE_WRAP_S, GL_REPEAT);
	glTexParameteri(type, GL_TEXTURE_WRAP_T, GL_REPEAT);

    glTexImage2D(type, 0, GL_RGBA, img_width, img_height, 0, format, pixel_type, bytes);
    glGenerateMipmap(type);

    stbi_image_free(bytes);

    Unbind();

}

void Texture::AssignUnit(Shader &shader, const char *uniform, GLuint unit)
{
    GLuint texture_uniform = glGetUniformLocation(shader.id, uniform);

    shader.Activate();

    glUniform1i(texture_uniform, unit);
}

void Texture::Bind()
{
    glBindTexture(type, id);
}

void Texture::Unbind()
{
    glBindTexture(type, 0);
}

void Texture::Delete()
{
    glDeleteTextures(1, &id);
}
